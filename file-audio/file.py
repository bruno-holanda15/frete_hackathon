import openai
import os

def process(filepath):
    audio_path = os.path.join("./audio", filepath)
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Arquivo de áudio não encontrado: {audio_path}")
    
    with open(audio_path, "rb") as audio:
        my_key = "CHAVE"
        openai.api_key = my_key
        transcript = openai.Audio.transcribe("whisper-1", audio)
    
    return transcript["text"]

nome_do_arquivo = 'audio.ogg'

try:
    resultado = process(nome_do_arquivo)
    print(resultado)
except FileNotFoundError as e:
    print(e)
