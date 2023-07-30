import openai
import json
import os
from dotenv import load_dotenv
from colorama import init, Fore, Style
init()
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_gpt(messages: list, model: str, temperature: float = 1, presence_penalty: float = 0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        presence_penalty=presence_penalty
    )
    return response

from prompt import prompt

with open("audio.txt", "r") as arquivo:
    texto_transcrito = arquivo.read()
    print("--------------------------------------------------------------")
    inputs = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": json.dumps(texto_transcrito)}
    ]

    results = call_gpt(inputs, 'gpt-3.5-turbo-16k')

    tema = results['choices'][0]['message']['content'].strip()

    print(f"{Fore.GREEN}Tema filtrado:{Style.RESET_ALL} ", tema)
    print("--------------------------------------------------------------")

