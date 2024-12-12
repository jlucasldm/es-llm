from model.questao import Questao
from provider.api_provider import OpenAIProvider

ENUNCIADO = """ Durante sua aventura pelas Terras-Selváticas,
     Bilbo Bolseiro  e seus amigos anões precisarão
     enfrentar a Trevamata para chegar na Montanha
     Solitária. Porém, sabemos que essa não é uma tarefa
     fácil. Para conseguir atravessar a floresta eles não
     devem, em hipótese alguma, sair da trilha. Por isso,
     Gandalf convocou os alunos de programação da
     UFBA para ajudar Bilbo e seus amigos.
     A Trevamata é  terreno traiçoeiro e sua trilha,
     em alguns trechos, tem o caminho sendo galhos de
     grandes árvores, que tem um limite de peso. Assim,
     terão que passar um por um por esses trechos de
     galhos. Mas, se excedido, quebrado, desloca todos os
     viajantes para fora do percurso. Precisamos então que, dado o peso dos amigos de Bilbo, você diga se
     eles estão aptos para passar pela trilha com segurança. O peso do Bilbo será ignorado"""

ENTRADA = """ A primeira linha de entrada é composta por um inteiro ‘N’ (1 <= N <= 13), indicando a
     quantidade de amigos de Bilbo. As ‘N’ linhas seguintes contêm, cada uma, uma String Nome e um
     inteiro ‘K’ (50 <= K <= 150), que representam, respectivamente, o nome e o peso de cada amigo de
     Bilbo. Por fim, a última linha contém um inteiro ‘C’ (50 <= C <= 250), indicando a capacidade máxima
     de peso suportado por um determinado galho da estrada"""

SAIDA = """Caso a capacidade da estrada não seja excedida, o programa deve imprimir a frase “Vamos
     todos encontrar a montanha!”, caso contrário, o programa deve imprimir a frase “Vamos virar
     almoço de aranhas gigantes!”, seguida, dos nomes dos amigos de Bilbo que causaram a tragédia.
     Imprima, nesse caso, um nome por linha após a frase inicial, seguindo a ordem de leitura dada dos
     nomes"""

CASOS_EXEMPLO = [
        {
            "entrada": "6\nThorin 60\nBalin 55\nDwalin 59\nFili 68\nKili 53\nDori 6\n 250",
            "saida": "Vamos todos encontrar a montanha!",
        },
        {
            "entrada": "7\nNori 50\nOri 57\nOin 52\nGloin 58\nBifur 55\nBofur 53\nBombur 63\n57",
            "saida": "Vamos virar almoço de aranhas gigantes!\nGloin\nBombur",
        },
    ]

MESSAGES = [
        {
            "role": "system",
            "content": """
                    Você é um modelo especializado em programação competitiva. Sua tarefa é gerar casos de teste válidos 
                    para problemas computacionais, garantindo que as saídas correspondam exatamente ao resultado correto 
                    de uma implementação funcional do problema.
                    """,
        },
        {
            "role": "user",
            "content": f"""
                    Uma questão de programação competitiva é composta por um enunciado, formato de entarda, formato de saída
                    e pares de exemplos de entrada e saída. Processe as seguintes informações de uma questão de programação
                    competitiva:
                    \n
                    Enunciado: {ENUNCIADO}\n
                    Entrada: {ENTRADA}\n
                    Saída: {SAIDA}\n
                    Casos de exemplo: {CASOS_EXEMPLO}\n
                    \n
                    Com base nas informações fornecidas sobre e levando em consideração uma resolução ideal da questão, 
                    gere 15 casos de teste variados, incluindo entradas e as saídas esperadas.

                    Certifique-se de que:
                    1. As entradas sigam exatamente o formato descrito no enunciado.
                    2. As saídas sejam calculadas corretamente com base nas regras descritas.
                    3. Inclua:   
                        - **Casos simples:** Entradas mínimas para testar a funcionalidade básica.
                        - **Casos médios:** Entradas de tamanho intermediário para verificar a consistência
                        - **Casos grandes:** Entradas no limite máximo permitido pelo problema para avaliar desempenho.
                        - **Casos especiais:** Cenários como valores extremos, padrões repetitivos e casos críticos 
                            descritos no enunciado.

                    Apresente cada caso de teste no formato:
                        Entrada:[Dados de entrada]
                        Saída:[Resultado esperado]

                    Tente ao máximo cobrir casos diversos de teste.
                    """,
        },
    ]

if __name__ == "main":
    questao = Questao(ENUNCIADO, ENTRADA, SAIDA, CASOS_EXEMPLO)
    api_provider = OpenAIProvider("gpt-4o-mini", 3000, 0.3)
    response = api_provider.get_response(MESSAGES)
    api_provider.save_response(response)
