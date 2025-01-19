from sqlalchemy import select
from sqlalchemy.orm import selectinload

from agents.open_ai_agent import OpenAiAgent
from agents.validator_agent import ValidatorAgent
from db.weyes_db import WeyesAsyncSession, Questao, CasoTeste, VaidationStatusEnum


class Blood:
    def __init__(
        self,
        model: str,
        max_tokens: int = 5000,
        temperature: float = 0,
        test_cases: int = 30,
    ):
        self.openai_provider = OpenAiAgent(
            model=model, max_tokens=max_tokens, temperature=temperature
        )
        self.test_cases = test_cases

    async def process_questions(self):
        async with WeyesAsyncSession() as session:
            # Consultar todas as questões do banco de dados
            questoes = (
                await session.scalars(
                    select(Questao)
                    .options(selectinload(Questao.exemplos))
                    .order_by(Questao.id)
                )
            ).all()

            # Iterar sobre todas as questões
            for questao in questoes:
                self.openai_provider.chat_history = []
                print("Gerando resposta para a questão:", questao.codigo)

                # Obter o prompt do sistema e o prompt de geração de casos de teste
                system_prompt_test_gerenation = (
                    self.openai_provider.get_system_prompt_test_gerenation()
                )
                user_prompt_test_gereation = (
                    self.openai_provider.get_user_prompt_test_gereation(
                        questao, self.test_cases
                    )
                )

                # Adicionar os prompts ao histórico de conversa
                self.openai_provider.add_message_to_history(
                    system_prompt_test_gerenation["role"],
                    system_prompt_test_gerenation["content"],
                )
                self.openai_provider.add_message_to_history(
                    user_prompt_test_gereation["role"],
                    user_prompt_test_gereation["content"],
                )

                # Obter a resposta do modelo para os prompts fornecidos
                completion = self.openai_provider.get_response(
                    self.openai_provider.chat_history
                )
                self.openai_provider.add_message_to_history(
                    "assistant",
                    completion.choices[0].message.content,
                )

                # Salvar a resposta do modelo no banco de dados
                await self.openai_provider.save_response(completion, questao, session)

                # Validar os casos de teste gerados
                validation_agent = ValidatorAgent(questao)
                await validation_agent.validate_test_cases()

                casos_teste_reprovados = (
                    (
                        await session.execute(
                            select(CasoTeste).where(
                                CasoTeste.questao_id == questao.id,
                                CasoTeste.validation_status
                                == VaidationStatusEnum.FAILED,
                            )
                        )
                    )
                    .scalars()
                    .all()
                )

                casos_teste_aprovados = (
                    (
                        await session.execute(
                            select(CasoTeste).where(
                                CasoTeste.questao_id == questao.id,
                                CasoTeste.validation_status
                                == VaidationStatusEnum.PASSED,
                            )
                        )
                    )
                    .scalars()
                    .all()
                )

                while len(casos_teste_aprovados) < self.test_cases:
                    # system_prompt_test_validation = (
                    #     self.openai_provider.get_system_prompt_test_validation()
                    # )
                    # user_prompt_test_validation = (
                    #     self.openai_provider.get_user_prompt_test_validation(
                    #         questao,
                    #         casos_teste_aprovados,
                    #         casos_teste_reprovados,
                    #         self.test_cases,
                    #     )
                    # )

                    user_prompt_test_gereation = (
                        self.openai_provider.get_user_prompt_test_gereation(
                            questao, self.test_cases
                        )
                    )

                    self.openai_provider.add_message_to_history(
                        user_prompt_test_gereation["role"],
                        user_prompt_test_gereation["content"],
                    )

                    # self.openai_provider.add_message_to_history(
                    #     system_prompt_test_validation["role"],
                    #     system_prompt_test_validation["content"],
                    # )
                    # self.openai_provider.add_message_to_history(
                    #     user_prompt_test_validation["role"],
                    #     user_prompt_test_validation["content"],
                    # )

                    completion = self.openai_provider.get_response(
                        self.openai_provider.chat_history
                    )
                    self.openai_provider.add_message_to_history(
                        "assistant",
                        completion.choices[0].message.content,
                    )

                    await self.openai_provider.save_response(
                        completion, questao, session
                    )

                    # Validar os casos de teste gerados
                    validation_agent = ValidatorAgent(questao)
                    await validation_agent.validate_test_cases()

                    # Verificar se há casos de teste reprovados
                    casos_teste_reprovados = (
                        (
                            await session.execute(
                                select(CasoTeste).where(
                                    CasoTeste.questao_id == questao.id,
                                    CasoTeste.validation_status
                                    == VaidationStatusEnum.FAILED,
                                )
                            )
                        ).scalars()
                    ).all()

                    casos_teste_aprovados = (
                        (
                            await session.execute(
                                select(CasoTeste).where(
                                    CasoTeste.questao_id == questao.id,
                                    CasoTeste.validation_status
                                    == VaidationStatusEnum.PASSED,
                                )
                            )
                        ).scalars()
                    ).all()

        print("Finished processing all questions")
