import json

from openai import OpenAI
from openai.types.chat import ChatCompletion
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from db.weyes_db import Questao, WeyesAsyncSession, CasoTeste

API_KEY = settings.openai.API_KEY


class OpenAiAgent:
    def __init__(self, model: str, max_tokens: int, temperature: float):
        self.client = OpenAI(api_key=API_KEY)
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.chat_history = []

    def add_message_to_history(self, role: str, message: str) -> None:
        self.chat_history.append(
            {
                "role": role,
                "content": message,
            }
        )

    @staticmethod
    def get_system_prompt_test_gerenation() -> dict:
        prompt = {
            "role": "system",
            "content": """
                            Você é um modelo especializado em programação competitiva. Sua tarefa é interpretar 
                            enunciados de problemas computacionais, utilizar resoluções fornecidas como base para 
                            validar e compreender a lógica do problema, e gerar casos de teste válidos, diversificados 
                            e relevantes, garantindo conformidade total com as especificações do problema. Todos os 
                            casos de teste gerados devem seguir rigorosamente as restrições e padrões descritos.

                            **Importante:** Sua resposta deve ser uma lista no formato JSON contendo apenas os casos de 
                            teste gerados, sem explicações adicionais ou texto fora do formato solicitado. 
                            A resposta não deve incluir nenhum tipo de justificativa ou explicação sobre como os casos 
                            foram gerados. 
                            Caso contrário, a resposta será considerada inválida.
                        """,
        }

        return prompt

    @staticmethod
    def get_user_prompt_test_gereation(questao: Questao, test_cases: int) -> dict:
        exemplos = {exemplo.entrada: exemplo.saida for exemplo in questao.exemplos}

        prompt = {
            "role": "user",
            "content": f"""
                                    Considere o seguinte problema de programação competitiva:

                                    <enunciado>: "{questao.enunciado}"
                                    <entrada>: "{questao.entrada}"
                                    <saida>: "{questao.saida}"
                                    <casos_de_exemplo>: "{exemplos}"
                                    <resolucao>: "{questao.resolucao}"

                                    **Tarefa:** Sua missão é interpretar a <resolucao> em função do <enunciado> e dos 
                                    <casos_de_exemplo>. Após isso, você deve gerar casos de teste novos, diversificados
                                    e alinhados com o enunciado e a resolução fornecida.

                                    **Passo 1: Compreensão e Análise do Problema**
                                    1. Interprete o <enunciado> e a <resolucao> para compreender a lógica do problema.
                                    2. Extraia as nuances lógicas do problema, prestando atenção em:
                                       - Sequência específica de operações descritas no enunciado.
                                       - Diferença entre processamento total (global) e individual (local).
                                       - Condições especiais, como limites extremos, padrões inusitados ou fronteiras lógicas.
                                    3. Utilize os <casos_de_exemplo> e a <resolucao> para validar sua análise e garantir que:
                                       - As saídas da resolução fornecida correspondem aos resultados esperados para os 
                                       <casos_de_exemplo>.
                                       - Sua análise reflete corretamente a lógica implementada na resolução.

                                    **Passo 2: Geração de Novos Casos de Teste**
                                    Com base na sua interpretação do problema e na resolução fornecida, gere **somente** {test_cases} 
                                    casos de entrada no formato JSON, obedecendo aos seguintes critérios:
                                    - **Casos Simples:** Entradas mínimas para validar comportamentos básicos.
                                    - **Casos Médios:** Entradas intermediárias representando cenários típicos.
                                    - **Casos Complexos:** Entradas que atingem o limite superior permitido pelo problema.
                                    - **Casos Especiais:** Cenários que explorem condições críticas, como restrições implícitas, 
                                    padrões raros ou valores que possam desafiar a lógica do problema.

                                    **Formato da resposta (exemplo):**
                                    [
                                        {{
                                            "entrada": "<entrada_do_caso>",
                                            "saida": "<saida_esperada>"
                                        }},
                                        ...
                                    ]
                                    Lembre-se: a resposta deve ser estritamente no formato JSON acima, sem explicações ou 
                                    comentários adicionais.
                                """,
        }

        return prompt

    @staticmethod
    def get_system_prompt_test_validation() -> dict:
        prompt = {
            "role": "system",
            "content": """
                        Você é um modelo especializado em programação competitiva. Sua tarefa é gerar casos de teste 
                        para problemas de programação, garantindo conformidade total com as especificações do problema 
                        e atendendo às correções necessárias com base em validações anteriores.

                        **Importante:**
                        - Utilize como referência as informações da questão de programação competitiva das mensagens
                        anteriores.
                        - Analise o resultado da validação dos casos teste da questão gerados por você anteriormente e 
                        identifique padrões ou erros nos casos marcados como inválidos.
                        - Gere novos casos de teste corrigidos e alinhados ao problema, garantindo que todos os casos
                        sejam válidos e atendam às especificações do problema.
                        - Sua resposta deve conter **apenas casos de teste novos** no formato JSON, corrigidos e 
                        alinhados ao problema, sem explicações ou comentários adicionais.
                    """,
        }

        return prompt

    @staticmethod
    def get_user_prompt_test_validation(
        questao: Questao,
        casos_teste_aprovados: list[CasoTeste],
        casos_teste_reprovados: list[CasoTeste],
        test_cases: int,
    ) -> dict:
        aprovados = []
        reprovados = []

        for caso in casos_teste_aprovados:
            aprovados.append(
                {
                    "entrada": caso.entrada,
                    "saida": caso.saida,
                    "valido": True,
                }
            )

        for caso in casos_teste_reprovados:
            reprovados.append(
                {
                    "entrada": caso.entrada,
                    "saida_gerada": caso.saida,
                    "saida_esperada": caso.validated_result,
                    "valido": False,
                }
            )

        prompt = {
            "role": "user",
            "content": f"""
                        Nem todos os casos de teste gerados estavam corretos. Os casos de teste validados e reprovados
                        estão listados abaixo:

                        <casos_validados>: "{aprovados}"
                        <casos_reprovados>: "{reprovados}" 

                        **Tarefa:** Sua missão é analisar os casos de teste fornecidos, utilizando as informações 
                        sobre quais foram considerados válidos ou inválidos, e gerar **apenas novos casos de teste 
                        corretos** no formato JSON. Se atente também ao uso de espaços em branco, novas linhas e demais
                        detalhes sintáticos. Gere {test_cases} casos de teste novos, corrigidos e alinhados ao
                        problema, sem explicações ou comentários adicionais.

                        **Passos para a Geração dos Casos de Teste:**
                        1. Analise o enunciado, a resolução fornecida e os casos de exemplo para compreender a lógica 
                        do problema.
                        2. Identifique os erros ou falhas nos casos inválidos com base no histórico submetido.
                        3. Garanta que todos os casos novos gerados sejam válidos e obedeçam às regras descritas no 
                        problema.
                        4. Inclua uma diversidade de casos, conforme os critérios a seguir:
                           - **Casos Simples:** Testes que validem cenários básicos.
                           - **Casos Médios:** Testes intermediários para validar situações típicas.
                           - **Casos Complexos:** Testes que desafiem os limites superiores das especificações.
                           - **Casos Especiais:** Testes que explorem cenários críticos ou padrões raros.

                        **Formato da Resposta (Exemplo):**
                        [
                            {{
                                "entrada": "<entrada_do_caso>",
                                "saida": "<saida_esperada>"
                            }},
                            ...
                        ]

                        **Requisitos Adicionais:**
                        - Não repita casos de teste previamente gerados, mesmo os válidos.
                        - Certifique-se de que todos os novos casos estejam em conformidade com o problema e a lógica 
                        da resolução fornecida.
                    """,
        }

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
    async def save_response(
        completion: ChatCompletion, questao: Questao, session: AsyncSession
    ) -> None:
        response = completion.choices[0].message.content
        test_cases = json.loads(response)

        async with session:
            for test_case in test_cases:
                await session.execute(
                    insert(CasoTeste).values(
                        questao_id=questao.id,
                        entrada=test_case["entrada"],
                        saida=test_case["saida"],
                    )
                )

            await session.commit()
