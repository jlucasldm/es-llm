import json

from model.questao import Questao
from provider.api_provider import OpenAIProvider

openai_provider = OpenAIProvider(model='gpt-4o-mini', max_tokens=3000, temperature=0)
questoes = json.load(open('questoes/banco_questoes.json', 'r', encoding='utf-8'))

for questao in questoes:
    print("Gerando resposta para a questão:", questao['nome'])

    prompt = openai_provider.get_prompt(questao)
    completion = openai_provider.get_response(prompt)
    openai_provider.save_response(completion, questao['nome'])

print("Respostas geradas com sucesso!")
