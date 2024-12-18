import os
import json

from sqlalchemy import insert, select

from db.weyes_db import WeyesAsyncSession, Questao, Exemplo

import asyncio


async def build_weyes() -> None:
    for file in os.listdir("../sources/questoes"):
        if file.endswith(".json") and file != "banco_questoes.json":
            with open(f"../sources/questoes/{file}", "r+", encoding="utf-8") as f:
                questao = json.load(f)

                async with WeyesAsyncSession() as session:
                    await session.execute(
                        insert(Questao).values(
                            codigo=questao["codigo"],
                            enunciado=questao["enunciado"],
                            entrada=questao["entrada"],
                            saida=questao["saida"],
                            resolucao=questao["resolucao"],
                        )
                    )

                    inserted_questao = (
                        (
                            await session.execute(
                                select(Questao).where(
                                    Questao.codigo == questao["codigo"]
                                )
                            )
                        )
                        .scalars()
                        .first()
                    )

                    for exemplo in questao["casos_exemplo"]:
                        await session.execute(
                            insert(Exemplo).values(
                                questao_id=inserted_questao.id,
                                entrada=exemplo["entrada"],
                                saida=exemplo["saida"],
                            )
                        )

                    await session.commit()

                f.close()


if __name__ == "__main__":
    asyncio.run(build_weyes())
