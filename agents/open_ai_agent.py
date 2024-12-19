from openai import OpenAI
from openai.types.chat import ChatCompletion
from config import settings
from db.weyes_db import Questao

API_KEY = settings.openai.API_KEY


class OpenAiAgent:
    def __init__(self, model: str, max_tokens: int, temperature: float):
        self.client = OpenAI(api_key=API_KEY)
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    def get_prompt(self, questao: Questao) -> list[dict]:

        exemplos = {exemplo.entrada: exemplo.saida for exemplo in questao.exemplos}

        prompt = [
            {
                "role": "system",
                "content": """
                            Você é um modelo especializado em programação competitiva. Sua tarefa é interpretar enunciados de problemas
                            computacionais, utilizar resoluções fornecidas como base para validar e compreender a lógica do problema,
                            e gerar casos de teste válidos, diversificados e relevantes, garantindo conformidade total com as
                            especificações do problema. Todos os casos de teste gerados devem seguir rigorosamente as restrições
                            e padrões descritos.
                        """,
            },
            {
                "role": "user",
                "content": f"""
                            Considere o seguinte problema de programação competitiva:

                            <enunciado>: "{questao.enunciado}"
                            <entrada>: "{questao.entrada}"
                            <saida>: "{questao.saida}"
                            <casos_de_exemplo>: "{exemplos}"
                            <resolucao>: "{questao.resolucao}"

                            **Tarefa:** Sua missão é interpretar a <resolucao> em função do <enunciado> e dos <casos_de_exemplo>.
                            Após isso, você deve gerar casos de teste novos, diversificados e alinhados com o enunciado e a
                            resolução fornecida.

                            **Passo 1: Compreensão e Análise do Problema**
                            1. Interprete o <enunciado> e a <resolucao> para compreender a lógica do problema.
                            2. Extraia as nuances lógicas do problema, prestando atenção em:
                               - Sequência específica de operações descritas no enunciado.
                               - Diferença entre processamento total (global) e individual (local).
                               - Condições especiais, como limites extremos, padrões inusitados ou fronteiras lógicas.
                            3. Utilize os <casos_de_exemplo> e a <resolucao> para validar sua análise e garantir que:
                               - As saídas da resolução fornecida correspondem aos resultados esperados para os <casos_de_exemplo>.
                               - Sua análise reflete corretamente a lógica implementada na resolução.

                            **Passo 2: Validação da Análise e Correção**
                            - Se qualquer inconsistência for encontrada durante a validação dos <casos_de_exemplo>, revise sua análise
                              e interprete novamente a resolução até que todas as saídas estejam alinhadas com os resultados esperados.
                            - Confirme que sua interpretação final é coesa com o <enunciado>, <casos_de_exemplo> e a <resolucao>.

                            **Passo 3: Geração de Novos Casos de Teste**
                            Com base na sua interpretação do problema e na resolução fornecida, gere 15 casos de entrada
                            diversificados e relevantes, com base nos seguintes critérios:
                            - **Casos Simples:** Entradas mínimas para validar comportamentos básicos.
                            - **Casos Médios:** Entradas intermediárias representando cenários típicos.
                            - **Casos Complexos:** Entradas que atingem o limite superior permitido pelo problema.
                            - **Casos Especiais:** Cenários que explorem condições críticas, como restrições implícitas, padrões raros
                              ou valores que possam desafiar a lógica do problema.

                            Para cada caso de entrada, faça o seguinte:
                            1. Valide a conformidade do caso de entrada com as restrições especificadas no <enunciado>.
                            2. Gere a saída esperada utilizando a <resolucao> fornecida como base.
                            3. Verifique novamente se as saídas geradas correspondem às especificações do problema e se as entradas
                               obedecem às restrições do <enunciado>.

                            **Passo 4: Validação e Revisão dos Casos de Teste**
                            - Submeta cada caso gerado à <resolucao> e certifique-se de que:
                              - **Conformidade:** As entradas seguem rigorosamente o formato e as restrições especificadas.
                              - **Correção:** As saídas geradas estão corretas e alinhadas com a lógica validada.
                              - **Diversidade:** Os casos cobrem uma ampla gama de cenários e restrições.
                              - **Relevância:** Exploraram nuances específicas e condições críticas descritas no problema.
                              - **Cobertura:** Testam todas as possíveis saídas esperadas.

                            **Formato de Saída para os Casos de Teste Gerados:**
                            - Apresente cada caso no seguinte formato:
                            Entrada:
                            [Dados de entrada]
                            Saída:
                            [Resultado esperado]

                            **Nota Importante:**
                            - A resolução fornecida deve ser utilizada como base para validar os casos de teste e compreender a lógica
                              do problema.
                            - Apenas continue quando estiver certo de que os casos de teste gerados são válidos, seguem rigorosamente
                              as restrições do problema, e cobrem amplamente as especificações do <enunciado>.
                        """,
            },
        ]

        return prompt

    def get_response(self, prompt: list[dict]) -> ChatCompletion:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=prompt,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )

        return completion

    @staticmethod
    def save_response(completion: ChatCompletion, nome: str, dir: str) -> None:
        f = open(f"{dir}/{nome}.txt", "w+", encoding="utf-8")
        f.write(completion.choices[0].message.content)
        f.close()
