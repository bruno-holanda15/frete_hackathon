# frete_hackathon

# Setup

OpenAI Library
Fornece acesso conveniente à API OpenAI a partir de aplicativos escritos na linguagem Python. Ele inclui um conjunto predefinido de classes para recursos de API que se inicializam dinamicamente a partir de respostas de API, o que o torna compatível com uma ampla variedade de versões da API OpenAI. Comando:
pip install --upgrade openai

Whisper
Usamos Python 3.9.9 para treinar e testar nossos modelos, mas espera-se que a base de código seja compatível com Python 3.8-3.11 e versões recentes do Python. A base de código também depende de alguns pacotes Python, principalmente o tiktoken da OpenAI para sua rápida implementação do tokenizador. Você pode baixar e instalar (ou atualizar) a versão mais recente do Whisper com o seguinte comando:

pip install -U openai-whisper

Alternativamente, o seguinte comando irá extrair e instalar o commit mais recente deste repositório, junto com suas dependências do 
pip install git+https://github.com/openai/whisper.git
