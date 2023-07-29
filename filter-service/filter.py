import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def treinar_modelo(dados_treinamento):
    exemplos = []
    for exemplo in dados_treinamento:
        pergunta = exemplo['pergunta']
        resposta_esperada = exemplo['resposta_esperada']
        role = exemplo['role']
        
        exemplo_formatado = f"{role}: {pergunta}\n{resposta_esperada}\n"
        exemplos.append(exemplo_formatado)
    
    prompt = "\n".join(exemplos)
    
    openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=400,
        stop=["\n"]
    )

    print("Modelo treinado!")

def filtrar_tema(texto):
    prompt = f"Texto: {texto}\nFiltrar o tema:"
    resposta = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=400,
        stop=["\n"]
    )

    tema_filtrado = resposta['choices'][0]['text'].strip()
    return tema_filtrado

from dados_treinamento import dados_treinamento as dados

# Treinar o modelo com os dados de treinamento
treinar_modelo(dados)

# Exemplo de uso
texto_exemplo = "Olá! Estou tentando acessar o sistema de gerenciamento de fretes. Pode me ajudar?"

tema_filtrado = filtrar_tema(texto_exemplo)
print("Tema filtrado:", tema_filtrado)
