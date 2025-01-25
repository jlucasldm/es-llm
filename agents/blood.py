from sqlalchemy import select, func
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
        self.openai_provider.chat_history = []
        self.system_prompt_test_gerenation = (
            self.openai_provider.get_system_prompt_test_gerenation()
        )
        self.user_prompt_test_gereation = None
        self.user_prompt_test_validation = None

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
                validation_round = 0

                print("Gerando resposta para a questão:", questao.codigo)
                self.openai_provider.clear_history()

                self.user_prompt_test_gereation = (
                    self.openai_provider.get_user_prompt_test_gereation(
                        questao, self.test_cases
                    )
                )

                # Adicionar os prompts ao histórico de conversa
                self.openai_provider.add_message_to_history(
                    self.system_prompt_test_gerenation["role"],
                    self.system_prompt_test_gerenation["content"],
                )
                self.openai_provider.add_message_to_history(
                    self.user_prompt_test_gereation["role"],
                    self.user_prompt_test_gereation["content"],
                )

                # Obter a resposta do modelo para os prompts fornecidos
                completion = self.openai_provider.get_response(
                    self.openai_provider.chat_history
                )

                # Salvar a resposta do modelo no banco de dados
                await self.openai_provider.save_response(completion, questao, session, validation_round)

                # Validar os casos de teste gerados
                validation_agent = ValidatorAgent(questao)
                await validation_agent.validate_test_cases()

                # Pegar os casos de teste balanceados
                casos_teste_reprovados, casos_teste_aprovados = (
                    await self.balance_test_cases(questao.id)
                )

                count = (
                    (
                        await session.execute(
                            select(func.count(CasoTeste.id)).where(
                                CasoTeste.questao_id == questao.id,
                                CasoTeste.validation_status
                                == VaidationStatusEnum.PASSED,
                            )
                        )
                    )
                    .scalars()
                    .first()
                )

                while count < self.test_cases:
                    validation_round += 1
                    user_prompt_test_validation = (
                        self.openai_provider.get_user_prompt_test_validation(
                            casos_teste_aprovados,
                            casos_teste_reprovados,
                            self.test_cases,
                        )
                    )

                    self.openai_provider.add_message_to_history(
                        user_prompt_test_validation["role"],
                        user_prompt_test_validation["content"],
                    )

                    completion = self.openai_provider.get_response(
                        self.openai_provider.chat_history
                    )

                    await self.openai_provider.save_response(
                        completion, questao, session, validation_round
                    )

                    # Validar os casos de teste gerados
                    validation_agent = ValidatorAgent(questao)
                    await validation_agent.validate_test_cases()

                    # Pegar os casos de teste balanceados
                    casos_teste_reprovados, casos_teste_aprovados = (
                        await self.balance_test_cases(questao.id)
                    )

                    self.openai_provider.clear_last_message()

                    count = (
                        (
                            await session.execute(
                                select(func.count(CasoTeste.id)).where(
                                    CasoTeste.questao_id == questao.id,
                                    CasoTeste.validation_status
                                    == VaidationStatusEnum.PASSED,
                                )
                            )
                        )
                        .scalars()
                        .first()
                    )

        print("Finished processing all questions")

    @staticmethod
    async def balance_test_cases(
        questao_id: int,
    ) -> tuple[list[CasoTeste], list[CasoTeste]]:
        casos_teste_reprovados = await CasoTeste.get_reprovados(questao_id)
        casos_teste_aprovados = await CasoTeste.get_aprovados(questao_id)

        if not casos_teste_reprovados or not casos_teste_aprovados:
            return casos_teste_reprovados, casos_teste_aprovados

        # Somente retornar 30 casos de teste
        if len(casos_teste_reprovados) + len(casos_teste_aprovados) <= 30:
            total_cases = len(casos_teste_reprovados) + len(casos_teste_aprovados)
            target_count = total_cases // 2
        else:
            target_count = 15

        casos_teste_reprovados = casos_teste_reprovados[-target_count:]
        casos_teste_aprovados = casos_teste_aprovados[-target_count:]

        return casos_teste_reprovados, casos_teste_aprovados
