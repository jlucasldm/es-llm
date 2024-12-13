from openai import OpenAI
from openai.types.chat import ChatCompletion
from config import settings
from model.questao import Questao

API_KEY = settings.openai.API_KEY


class OpenAIProvider:
    def __init__(self, model: str, max_tokens: int, temperature: float):
        self.client = OpenAI(api_key=API_KEY)
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    def get_prompt(self, questao: dict) -> list[dict]:
        prompt = [
            {
                "role": "system",
                "content": """
            Você é um modelo especializado em programação competitiva. Sua tarefa é interpretar enunciados de problemas
            computacionais, implementar soluções corretas e gerar casos de teste válidos, diversificados e relevantes,
            garantindo conformidade total com as especificações do problema.
        """,
            },
            {
                "role": "user",
                "content": f"""
            Considere o seguinte problema de programação competitiva:

            <enunciado>: "{questao['enunciado']}"
            <entrada>: "{questao['entrada']}"
            <saida>: "{questao['saida']}"
            <casos_de_exemplo>: "{questao['casos_exemplo']}"

            **Tarefa 1:** Com base no <enunciado>, analise e identifique:
            - Todas as regras explícitas descritas no problema.
            - Restrições implícitas que podem ser inferidas do contexto ou exemplos fornecidos.
            - Condições excepcionais que podem impactar a lógica, como limites de entrada, casos extremos ou
              comportamentos fronteiriços.

            Ao analisar, preste atenção em **nuances lógicas**, como:
            - Sequência de operações que devem ser aplicadas de forma específica.
            - Regras condicionais que dependem de características da entrada.
            - Diferenças entre processamento total (global) e individual (local) de elementos.

            **Tarefa 2:** Desenvolva um programa funcional que implemente a lógica descrita no <enunciado>. Submeta as
            entradas dos <casos_de_exemplo> à sua solução e verifique se os resultados correspondem ao esperado. Caso a
            implementação não esteja correta, ajuste-a até que a saída seja válida para todos os casos.
            Apenas prossiga quando sua solução for validada com sucesso.

            **Tarefa 3:** Gere 15 novos casos de teste com base no seguinte critério:
            - **Casos Simples:** Entradas mínimas para validar funcionalidades básicas.
            - **Casos Médios:** Entradas intermediárias que testam cenários mais comuns.
            - **Casos Complexos:** Entradas que atingem o limite máximo permitido pelo problema.
            - **Casos Especiais:** Entradas que explorem nuances do problema, como padrões inusitados ou condições
              fronteiriças, exemplo: casos que podem falhar devido a restrições implícitas.

            Para cada caso, calcule a saída utilizando sua implementação funcional. Garanta que:
            - As entradas sigam rigorosamente o formato descrito no <enunciado>.
            - As saídas correspondam ao comportamento esperado para as entradas geradas.

            **Tarefa 4:** Valide os casos de teste gerados submetendo-os novamente à implementação. Certifique-se de que:
            - **Diversidade:** Os casos cobrem uma ampla gama de cenários e restrições.
            - **Relevância:** Exploraram nuances específicas e condições críticas do problema.
            - **Cobertura:** Testam todas as possíveis saídas esperadas.

            **Formato para os Casos de Teste Gerados:**
            - Apresente cada caso de teste no formato especificado abaixo:
            Entrada:
            [Dados de entrada]
            Saída:
            [Resultado esperado]

            **Nota Importante:** Certifique-se de que a análise do problema, a implementação da solução e a geração
            dos casos de teste sejam sensíveis a todos os detalhes do problema. Exemplos como:
            - Processamento individual versus global de elementos.
            - Condições especiais derivadas de restrições de entrada.
            - Padrões que surgem de valores extremos ou interações únicas nas entradas.

            Apenas continue quando tiver certeza de que:
            1. A implementação está correta e validada.
            2. Os casos de teste gerados são válidos e cobrem todas as condições descritas no problema.
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
    def save_response(completion: ChatCompletion, nome: str) -> None:
        f = open(f"model_response/{nome}.txt", "w+", encoding="utf-8")
        f.write(completion.choices[0].message.content)
        f.close()
