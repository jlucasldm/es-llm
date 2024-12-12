from openai import OpenAI
from openai.types.chat import ChatCompletion
from config import settings

API_KEY = settings.openai.API_KEY

class OpenAIProvider:
    def __init__(self, model: str, max_tokens: int, temperature: float):
        self.client = OpenAI(API_KEY)
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    def get_response(self, messages: list[dict]) -> ChatCompletion:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )

        return completion

    @staticmethod
    def save_response(completion: ChatCompletion):
        f = open("resp.txt", "w+", encoding="utf-8")
        f.write(completion.choices[0].message.content)
        f.close()
