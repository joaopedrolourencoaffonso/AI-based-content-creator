# Contando estórias com OpenAI

Este script Python combina o poder da linguagem OpenAI e dos modelos de geração de imagens para criar uma experiência única de contar histórias. Ele permite que os usuários insiram um título e uma premissa para uma história de fantasia, gerando conteúdo textual, áudio e imagens geradas por IA, os quais podem ser utilizados para edição de um vídeo.

## Pré-requisitos
- [Chave de API OpenAI](https://beta.openai.com/signup/)
- [Cliente OpenAI Python](https://github.com/openai/openai-python)
- Python 3.x instalado

## Uso

1. Execute o script executando `python story_maker.py` em seu terminal.
2. Insira o título e a premissa desejados para sua história de fantasia quando solicitado.
3. O script criará diretórios, gerará uma história, limpará o texto e o dividirá em cenas.
4. Para cada cena, ele gera um prompt, solicita uma imagem gerada por IA e baixa/salva a imagem.
5. A história inteira é concatenada e uma narração em áudio é gerada usando a API Text-to-Speech (TTS) da OpenAI.
6. O resultado final inclui uma história escrita, imagens geradas por IA e uma narração em áudio.

## Visão geral das funções

- `narration(client, titulo, story)`: Gera narração em áudio da história usando a API OpenAI TTS.

- `append_string_to_file(file_path, content)`: Acrescenta uma string a um arquivo especificado.

- `download_and_save_image(url, title, image_name)`: Baixa e salva uma imagem de um determinado URL.

- `prompt_generator(client, scene)`: Gera prompts para o modelo DALL-E com base nas cenas de entrada.

- `cleaner(title)`: Limpa a string recebida da API OpenAI.

- `story_creator(client, premissa, title)`: Envia uma solicitação para a API OpenAI, salva a resposta em um arquivo.

- `main()`: A função principal que orquestra todo o processo de contar histórias.

## Observação

1. Certifique-se de ter a chave de API OpenAI necessária e o cliente Python instalados. Lide com quaisquer erros durante a execução e aproveite a jornada criativa da narrativa!
2. Esse projeto é apenas um experimento e não tem fins lucrativos. Os resultados são simplórios, mas servem como prova de conceito para uma aplicação mais complexa no futuro.
3. Em média, cada execução do script me custou, aproximadamente, 54 cents, ou R$ 2,7. Tome cuidado ao executar o script.
