import asyncio
import subprocess

from sqlalchemy import select
from db.weyes_db import WeyesAsyncSession, CasoTeste, VaidationStatusEnum, Questao


class ValidatorAgent:
    def __init__(self, questao: Questao):
        self.questao = questao

    # Criar executável sobre um código em c++. Consultar Questao.resolucao para obter o código
    async def create_executable(self):
        try:
            with open("main.cpp", "w+") as f:
                f.write(self.questao.resolucao)

            process = await asyncio.create_subprocess_shell(
                "g++ main.cpp -o main",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            await process.communicate()

            print("Executable created successfully")

        except Exception as e:
            print("Error creating executable", e)

    # Consultar os casos de teste pendentes para a questão e validar a saída gerada pelo código do usuário
    async def validate_test_cases(self):
        try:
            await self.create_executable()

            async with WeyesAsyncSession() as session:
                casos_teste = (
                    await session.scalars(
                        select(CasoTeste)
                        .where(CasoTeste.questao_id == self.questao.id)
                        .where(
                            CasoTeste.validation_status != VaidationStatusEnum.PASSED
                        )
                    )
                ).all()

                print(f"Validating {len(casos_teste)} test cases")

                for caso_teste in casos_teste:
                    process = subprocess.Popen(
                        ["./main.exe"],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,  # Garante que a comunicação seja em texto, não bytes
                    )

                    # Envia a entrada e captura a saída padrão (out) e erros (err)
                    out, err = process.communicate(caso_teste.entrada)

                    if err:
                        print("Error executing test case", err)
                        continue

                    if out.strip() == caso_teste.saida.strip():
                        caso_teste.validation_status = VaidationStatusEnum.PASSED
                        print("Test case passed")
                    else:
                        caso_teste.validation_status = VaidationStatusEnum.FAILED
                        print("Test case failed")

                    await session.commit()

        except Exception as e:
            print("Error validating test cases", e)
