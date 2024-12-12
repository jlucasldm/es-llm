# ES-LLM

## Introudção
Como trabalho da disciplina de Tópicos em Engenharia de Software cujo objetivo é a aplicação de LLM a geração de testes,
propomos o uso da API da OpenAi, utilizando o modelo gpt-4o-mini, para gerar casos de teste para questões de programação
para os cursos de programação básico e intermediário ministrados pelo professor Rubisley.

Através de engenharia de prompt, vamos construir uma aplicação que seja capaz de interpretar enunciados das questões e 
gerar pares de entradas e saídas como casos de teste. Esses conjuntos seriam então utilizados como recurso de avaliação 
se uma dada solução para uma questão está correta. Caso o programa submetido pelos alunos forneça sempre as mesmas 
saídas para as entradas correspondentes, então o teste é bem sucedido e o programa é entendido como correto.

## Estrutura
A gente tem o main, a aplicação principal, onde é definido uns exemplos de `enunciado`, `entrada`, `saida` e 
`casos_exemplo` de uma questão. Por enquanto, é algo arbitrário mesmo, somente para controle. Essa questão foi utilizada
recentemente no curso de programação intermediária.

No main também definimos o prompt na variável `MESSAGES`, que recebe intrução a nível de sistema e nível de usuário.
Mexer no prompt deve ser nossa prioridade agora, a fim de gerar testes coerentes para cada questão.

Criei umas classes de provider da openai e de questão. Estruturas auxiliares mesmo, nada demais. Se ficar esquisito pra 
entender a implementação, eu dou uma documentada.

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

## Como executar
- Baixe o poetry
- No diretório raiz do projeto, instale as dependências rodando ``poetry install``
- No diretório raiz do projeto, crie um arquivo ``.secrets.toml`` cujo conteúdo seja: 
```
[openai]
API_KEY="chave_da_api"
```
- Execute o main.py