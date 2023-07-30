import openai
import os
from dotenv import load_dotenv
from colorama import init, Fore, Style
init()
load_dotenv()

def process(filepath):
    audio_path = os.path.join("audio-service/audio", filepath)
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Arquivo de áudio não encontrado: {audio_path}")
    
    with open(audio_path, "rb") as audio:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        transcript = openai.Audio.transcribe("whisper-1", audio)
    
    return transcript["text"]

nome_do_arquivo = 'audio-logar.ogg'

try:
    resultado = process(nome_do_arquivo)
    print("--------------------------------------------------------------")
    print(f"{Fore.GREEN}Frase captada:{Style.RESET_ALL} ", resultado)
    print("--------------------------------------------------------------")
    with open("audio.txt", "w") as arquivo:
        arquivo.write(resultado)
except FileNotFoundError as e:
    print(e)
