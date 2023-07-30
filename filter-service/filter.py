import openai
import json

openai.api_key = 'CHAVE_ENV'

def call_gpt(messages: list, model: str, temperature: float = 1, presence_penalty: float = 0):
    """This function will call the OpenAI API and return the response"""
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        presence_penalty=presence_penalty
    )
    return response

from prompt import prompt

texto_transcrito = 'Quero trocar minha placa'

inputs = [
    {"role": "system", "content": prompt},
    {"role": "user", "content": json.dumps(texto_transcrito)}
]

results = call_gpt(inputs, 'gpt-3.5-turbo-16k')

tema = results['choices'][0]['message']['content'].strip()

print('Tema filtrado: ',tema)