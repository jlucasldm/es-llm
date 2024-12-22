import asyncio
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from agents.validator_agent import ValidatorAgent
from db.weyes_db import WeyesAsyncSession, Questao
from agents.open_ai_agent import OpenAiAgent

openai_provider = OpenAiAgent(model="gpt-4o-mini", max_tokens=3000, temperature=0)


async def main():
    last_questao_id = 0

    async with WeyesAsyncSession() as session:
        questoes = (
            await session.scalars(
                select(Questao)
                .where(Questao.id > last_questao_id)
                .options(selectinload(Questao.exemplos))
                .order_by(Questao.id)
                .limit(100)
            )
        ).all()

        for questao in questoes:
            print("Gerando resposta para a questão:", questao.codigo)

            prompt = openai_provider.get_prompt(questao)
            completion = openai_provider.get_response(prompt)
            await openai_provider.save_response(completion, questao)

            validation_agent = ValidatorAgent(questao)
            await validation_agent.validate_test_cases()

    print("Finished processing all questions")


if __name__ == "__main__":
    asyncio.run(main())
