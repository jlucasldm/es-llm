# ES-LLM

## Introudção
Como trabalho da disciplina de Tópicos em Engenharia de Software cujo objetivo é a aplicação de LLM a geração de testes,
propomos o uso da API da OpenAi, utilizando o modelo gpt-4o-mini, para gerar casos de teste para questões de programação
para os cursos de programação básico e intermediário ministrados pelo professor Rubisley.

Através de engenharia de prompt, vamos construir uma aplicação que seja capaz de interpretar enunciados das questões e 
gerar pares de entradas e saídas como casos de teste. Esses conjuntos seriam então utilizados como recurso de avaliação 
se uma dada solução para uma questão está correta.

## Estrutura
A gente tem o main, a aplicação principal, onde é definido uns exemplos de `enunciado`, `entrada`, `saida` e 
`casos_exemplo` de uma questão. Por enquanto, é algo arbitrário mesmo, somente para controle. Essa questão foi utilizada
recentemente no curso de programação intermediária.

No main também definimos o prompt na variável `MESSAGES`, que recebe intrução a nível de sistema e nível de usuário.
Mexer no prompt deve ser nossa prioridade agora, a fim de gerar testes coerentes para cada questão.

Criei umas classes de provider da openai e de questão. Estruturas auxiliares mesmo, nada demais. Se ficar esquisito pra 
entender a implementação, eu dou uma documentada.

### Discussão pós aula
É importante que as respostas do modelo sejam submetidas a um avalidação. Já deu para perceber que existe um ganho no
entendimento do modelo ao submeter também a resolução, refinando a interpretação do modelo sobre a questão e, portanto.
No entanto, o melhor entendimento sobre o a questão não se refletiu, necessariamente, na geração de melhores e 
consistentes casos de teste. 

Em função do que discutimos em aula, é mt jogo tentar valildar os casos de teste gerados pelo modelo utilizando a 
execução da resolução. No caso, criaríamos um agnte validador, um executável compilado pelo código de resolução, e
submeteríamos a ele os casos de entrada, validando os casos gerados pelo modelo. Se houver a ocorrência de uma entarda
que não correspondeu à saída do validador, voltamos a informar ao cliente o que ocorreu e pedimos para que ele o corrija.
Faremos isso até ter uma cobertura de casos de teste suficiente (criterios de suficiência a definir).

Usaremos um banco de dados vetorial como uma estrutura comunicacional intermediária entre o modelo e o agente validador.
Os casos de teste certos e errados serão tratados e armazenados nesse banco de dados vetorial de forma a informar ao
modelo o que corrigir e ao validador o que validar. (Isso eh basicamente RAG viu fellas).

## Considerações
No momento, estamos fazendo uma consulta ao modelo `gpt-4o-mini` usando o prompt definido por `MESSAGES` em `main.py`.
É através do prompt que definimos que tipo de tarefa o modelo performará e suas restrições.

A ideia é, uma vez o usuário inserindo para cada questão o `enunciado`, `entrada`, `saida` e `casos_exemplo` 
correspondentes, o modelo possa processar essas informações a fim de gerar os casos testes para a questão dada. Algo em 
torno de uns 15 conjuntos por enquanto.

O coração desse projeto reside no tratamento dessas informações das questões e no polimento do prompt. O modelo está 
pronto para uso, basta a gente saber como utilizá-lo para performar a tarefa que queremos, identificando que tipo de 
recursos são necessários para tal e que tipo de instrução (prompt) deve ser desenvolvida.

Sobre o formato de saída, podemos ver depois. O importante agora é mexer com o prompt e botar a geração de teste por 
questões para funcionar.


## Proximos passos
Depois da discussão em aula, acho que o foco é o RAG.

1. Vamos mexer na comunicação do script com o client, possibilitando enviar vários prompts em uma sessão. Dessa forma, 
conseguimos processar várias respostas de um mesmo client. Um mesmo client é importante para aproveitar o contexto de 
cada questão submetida nos prompts anteriores. 

2. Ajeitando isso, vamos criar essa estrutura do agente verificador que consegue executar um conjunto de entradas e saídas.
Disso, precisamos ter uma forma de armazenar e associar a esses conjuntos de entradas e saídas valores de sucesso ou 
falha da execução.

3. Construindo esse agente, bora mexer no banco de dados vetorial para se comunicar entre o modelo e o agente validador. 
Os casos de teste gerados pelo modelo e o sucesso da validação pelo agente validador serão registrados lá. O modelo deve
continuar gerando os casos teste até que uma quantidade X de casos teste tenham sido gerados corretamente.

4. Depois a gente vê um framework de comunicação melhor, um formato maneiro de input do usuário e de saída do modelo e
do sistema.

## Como executar
- Baixe o poetry
- No diretório raiz do projeto, instale as dependências rodando ``poetry install``
- No diretório raiz do projeto, crie um arquivo ``.secrets.toml`` cujo conteúdo seja: 
```
[openai]
API_KEY="chave_da_api_da_openai"
```
- Execute o main.py