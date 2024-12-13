from model.questao import Questao
from provider.api_provider import OpenAIProvider

ENUNCIADO = """Durante sua aventura pelas Terras-Selváticas,
     Bilbo Bolseiro  e seus amigos anões precisarão
     enfrentar a Trevamata para chegar na Montanha
     Solitária. Porém, sabemos que essa não é uma tarefa
     fácil. Para conseguir atravessar a floresta eles não
     devem, em hipótese alguma, sair da trilha. Por isso,
     Gandalf convocou os alunos de programação da
     UFBA para ajudar Bilbo e seus amigos.
     A Trevamata é um terreno traiçoeiro e sua trilha,
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
            "entrada": """
            6
            Thorin 60
            Balin 55
            Dwalin 59
            Fili 68
            Kili 53
            Dori 6
            250
            """,
            "saida": "Vamos todos encontrar a montanha!",
        },
        {
            "entrada": """
            7
            Nori 50
            Ori 57
            Oin 52
            Gloin 58
            Bifur 55
            Bofur 53
            Bombur 63
            57
            """,
            "saida": """
            Vamos virar almoço de aranhas gigantes!
            Gloin
            Bombur
            """,
        },
    ]

MESSAGES = MESSAGES = [
    {
        "role": "system",
        "content": """
            Você é um modelo especializado em programação competitiva. Sua tarefa é interpretar corretamente
            enunciados de problemas computacionais, implementar soluções baseadas nas regras fornecidas e
            gerar casos de teste válidos e relevantes para avaliar a qualidade e a diversidade da implementação.
        """
    },
    {
        "role": "user",
        "content": f"""
            Considere a seguinte questão de programação competitiva, que será descrita com um enunciado, formato
            de entrada, formato de saída e exemplos fornecidos:

            Enunciado: "{ENUNCIADO}"
            Entrada: "{ENTRADA}"
            Saída: "{SAIDA}"
            Casos de exemplo: "{CASOS_EXEMPLO}"

            **Tarefa 1:** Processe cuidadosamente o enunciado, identificando todas as nuances e especificidades 
            das regras descritas. Avalie, especialmente, as condições mencionadas que podem alterar a forma como 
            o problema deve ser solucionado.
            
            **Tarefa 2:** Desenvolva um programa que implemente uma solução para a questão, seguindo rigorosamente 
            as regras e condições identificadas. Submeta os casos de exemplo fornecidos ao programa e valide se a saída 
            gerada corresponde ao resultado esperado. Se houver discrepâncias, revise cuidadosamente a implementação 
            para corrigir qualquer erro.

            **Tarefa 3:** Após validar que a implementação está correta, gere quinze novos casos de teste. Certifique-se 
            de que esses casos sejam válidos e cubram diferentes cenários, incluindo:
            - Casos simples: Entradas mínimas para validar o comportamento básico.
            - Casos médios: Entradas intermediárias para testar consistência.
            - Casos complexos: Entradas no limite superior permitido pelo problema.
            - Casos especiais: Cenários específicos que exploram nuances do enunciado.

            **Tarefa 4:** Submeta os casos de teste gerados ao programa implementado pela primeira tarefa e valide se a 
            saída gerada corresponde ao resultado esperado utilizando. Avalie a qualidade dos casos com base em:
            1. Diversidade: Os casos cobrem uma ampla gama de cenários e restrições?
            2. Relevância: Os casos destacam nuances e condições particulares do problema?
            3. Cobertura: Os casos testam todas as possíveis saídas do programa?

            **Formato dos Casos de Teste Gerados:** 
            Retorne cada caso no seguinte formato:
            Entrada:
            [Dados de entrada]
            Saída:
            [Saída esperada]

            **Atenção:** Certifique-se de que sua interpretação e implementação sejam sensíveis a todos os detalhes do 
            enunciado. Qualquer interpretação incorreta resultará em uma solução inválida.

            Apenas continue quando estiver seguro de que a solução, os casos de teste gerados e a validação final estão 
            corretos e de acordo com as especificações do problema.
        """
    }
]

questao = Questao(ENUNCIADO, ENTRADA, SAIDA, CASOS_EXEMPLO)
api_provider = OpenAIProvider("gpt-4o", 3000, 0.3)
response = api_provider.get_response(MESSAGES)
api_provider.save_response(response)
