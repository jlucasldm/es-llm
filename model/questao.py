class Questao:
    def __init__(self, enunciado: str, entrada: str, saida: str, casos_exemplo: list[dict]):
        self.enunciado = enunciado
        self.entarda = entrada
        self.saida = saida
        self.casos_exemplo = casos_exemplo

class BancoDeQuestoes:
    def __init__(self):
        self.questoes = []

    def adicionar_questao(self, questao: Questao):
        self.questoes.append(questao)

    def remover_questao(self, questao: Questao):
        self.questoes.remove(questao)