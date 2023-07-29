import gradio as gr
import openai
import os
from dotenv import load_dotenv
load_dotenv(".env")


def process(filepath):
    
    audio = open(filepath, "rb")
    my_key = os.getenv ("OPENAI_API_KEY")
    openai.api_key = my_key
    transcript = openai.Audio.transcribe("whisper-1", audio)
    
    return transcript["text"]
    
demo = gr.Interface(
    fn=process, 
    inputs=gr.Audio(source="upload",type="filepath"), 
    outputs="text")
    
demo.launch()   


