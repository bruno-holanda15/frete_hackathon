# frete_hackathon

# Setup
Whisper
Usamos Python 3.9.9 para treinar e testar nossos modelos, mas espera-se que a base de código seja compatível com Python 3.8-3.11 e versões recentes do Python. A base de código também depende de alguns pacotes Python, principalmente o tiktoken da OpenAI para sua rápida implementação do tokenizador. Você pode baixar e instalar (ou atualizar) a versão mais recente do Whisper com o seguinte comando:

pip install -U openai-whisper

Alternativamente, o seguinte comando irá extrair e instalar o commit mais recente deste repositório, junto com suas dependências do 
pip install git+https://github.com/openai/whisper.git
