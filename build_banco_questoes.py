# iterar sobre todas as questões e criar um banco de questões
# com as questões e suas respectivas respostas

import os
import json


def get_questoes():
    questoes = []
    for file in os.listdir("questoes"):
        if file.endswith(".json"):
            with open(f"questoes/{file}", "r+", encoding="utf-8") as f:
                questoes.append(json.load(f))
    return questoes


def build_banco_questoes():
    questoes = get_questoes()
    banco = []
    for questao in questoes:
        banco.append(
            {
                "nome": questao["nome"],
                "codigo": questao["codigo"],
                "enunciado": questao["enunciado"],
                "entrada": questao["entrada"],
                "saida": questao["saida"],
                "casos_exemplo": questao["casos_exemplo"],
            }
        )
    with open("questoes/banco_questoes.json", "w+", encoding="utf-8") as f:
        json.dump(banco, f, indent=4)


if __name__ == "__main__":
    build_banco_questoes()
