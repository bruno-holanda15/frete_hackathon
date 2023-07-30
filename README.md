# Fala Parceiro!

O objetivo principal deste projeto é criar um sistema de transcrição de áudios enviados via WhatsApp, visando aprimorar a comunicação dentro do nosso chatbot. Com a transcrição do áudio, poderemos direcionar de forma mais eficiente o atendimento ao cliente, evitando a necessidade de várias etapas e processos.

O funcionamento do projeto será estruturado em duas etapas fundamentais:

1. **Transcrição do áudio:** O serviço será capaz de receber áudios no formato .ogg enviados pelo WhatsApp e, por meio da ferramenta de transcrição do openai, converterá o conteúdo desses áudios em texto, armazenando-o em um arquivo .txt.

2. **Treinamento do modelo:** O serviço de filtragem possui um modelo que faz a filtragem do tema solicitado no áudio. Utilizamos um prompt com algumas perguntas mais corriqueiras que podem ser feitas durante o atendimento e induzimos o modelo a trazer a resposta que se encaixa melhor com o contexto.

## Dicas inicias

- Instale o python na sua máquina
- Rode o comando pip install openai
- Para testar o serviço, crie um .env e adicione a variável *OPENAI_API_KEY* com sua chave de acesso.


# Como rodar

Para testar o serviço de transcrição de áudio, rode o comando:

```
make transcript
```

Para testar o serviço de filtragem, rode o comando:

```
make filter
```
