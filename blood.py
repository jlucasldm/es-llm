from sqlalchemy import select
from sqlalchemy.orm import selectinload

from agents.open_ai_agent import OpenAiAgent
from agents.validator_agent import ValidatorAgent
from db.weyes_db import WeyesAsyncSession, Questao


class Blood:
    def __init__(self, model: str, max_tokens: int = 5000, temperature: float = 0):
        self.openai_provider = OpenAiAgent(
            model=model, max_tokens=max_tokens, temperature=temperature
        )

    async def process_questions(self):
        async with WeyesAsyncSession() as session:
            questoes = (
                await session.scalars(
                    select(Questao)
                    .options(selectinload(Questao.exemplos))
                    .order_by(Questao.id)
                )
            ).all()

            for questao in questoes:
                print("Gerando resposta para a questão:", questao.codigo)

                prompt = self.openai_provider.get_prompt(questao)
                completion = self.openai_provider.get_response(prompt)
                await self.openai_provider.save_response(completion, questao)

                validation_agent = ValidatorAgent(questao)
                await validation_agent.validate_test_cases()

        print("Finished processing all questions")
