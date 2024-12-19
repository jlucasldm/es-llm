import asyncio
import sys
import subprocess

from sqlalchemy import select
from db.weyes_db import WeyesAsyncSession, CasoTeste, VaidationStatusEnum

# TODO: Implementar a classe do agente validador
# - O agente validador deve ser capaz de executar os casos de teste pendentes
# - O agente validador deve comparar a saída gerada pelo código do usuário com a saída esperada
# - O agente validador deve atualizar o status de validação dos casos de teste
# - O agente validador deve persistir as atualizações no banco de dados
# - O agente validador deve ser executado com o caminho para o executável do usuário como argumento
# - O agente validador deve ser executado em um processo separado

async def validate_test_cases(executable_path):
    async with WeyesAsyncSession() as session:
        test_cases = await session.execute(
            select(CasoTeste).filter(CasoTeste.validation_status == VaidationStatusEnum.PENDING)
        )
        test_cases = test_cases.scalars().all()

        for test_case in test_cases:
            # Execute the user's solution with the input data
            process = subprocess.Popen(
                [executable_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate(input=test_case.input_data)

            # Compare the actual output with the expected output
            actual_output = stdout.strip()
            validation_status = VaidationStatusEnum.PASSED if actual_output == test_case.expected_output else VaidationStatusEnum.FAILED
            test_case.actual_output = actual_output
            test_case.validation_status = validation_status
            await session.add(test_case)

        await session.commit()

if __name__ == "__main__":
    executable_path = sys.argv[1]
    asyncio.run(validate_test_cases(executable_path))