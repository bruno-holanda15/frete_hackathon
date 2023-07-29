import openai

# Substitua 'YOUR_API_KEY' pelo seu chave de API da OpenAI
openai.api_key = 'SUA_CHAVE'

def filtrar_tema(texto):
    # Defina o prompt para a solicitação ao GPT-3
    prompt = f"Texto: {texto}\nFiltrar o tema:"

    # Faça a solicitação para o GPT-3
    resposta = openai.Completion.create(
        engine="text-davinci-002",  # Use o mecanismo de texto GPT-3
        prompt=prompt,
        max_tokens=100,  # Defina o número máximo de tokens para a resposta
        stop=["\n"]  # Pare a resposta na primeira linha (tema filtrado)
    )

    # Extrai a resposta do GPT-3 e remove qualquer texto adicional
    tema_filtrado = resposta['choices'][0]['text'].strip()

    return tema_filtrado

# Exemplo de uso
texto_exemplo = "Olá! Estou entrando em contato para relatar um problema com o meu pedido. Eu fiz o pedido há uma semana e ainda não recebi nenhuma atualização do status de entrega."

tema_filtrado = filtrar_tema(texto_exemplo)
print("Tema filtrado:", tema_filtrado)
