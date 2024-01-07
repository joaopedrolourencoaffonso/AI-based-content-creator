# Gerador de vídeo de Música com IA

Este script Python gera imagens baseadas nas letras de um arquivo de texto e as associa a um arquivo de áudio. As imagens geradas podem ser utilizadas para a criação de vídeos com letras ("_lyrics_"). O script utiliza a API da OpenAI para gerar as imagens e a biblioteca Pillow para manipulação de imagens.

## Características

- **Geração de imagens:** utiliza a API OpenAI para gerar imagens com base em prompts de texto fornecidos, representando diferentes segmentos de letras.
  
- **Adição de texto em imagem:** Adiciona o texto gerado às imagens, criando uma representação visual das letras.

- **Manipulação de arquivos:** Baixa imagens dos URLs gerados e as salva no diretório especificado. Além disso, salva links e legendas em um arquivo de texto para referência.

## Pré-requisitos

- **Chave de API OpenAI:** Obtenha uma chave de API da OpenAI e substitua o espaço reservado no script pela sua chave real.

- **Bibliotecas Python:** Instale as bibliotecas Python necessárias usando o seguinte comando:
   ```bash
   pip install openai pillow
   ```

## Uso

1. Execute o script e forneça as entradas necessárias:
     - Nome do Projeto
     - Caminho para o arquivo de texto contendo as letras
     - Caminho para o arquivo de áudio

2. O script irá gerar imagens, adicionar texto a elas e salvar as imagens modificadas junto com as originais em diretórios separados.

3. Acesse as imagens no diretório `com_texto` para obter as imagens finais com texto adicionado.

## Exemplo

```bash
python musicVideoCreator.py
```

## Notas

- O script usa o modelo `dall-e-3` da OpenAI para geração de imagens. Certifique-se de que sua conta OpenAI tenha acesso a este modelo.

- As imagens geradas são salvas no diretório `imagens`, com diretórios adicionais para imagens originais e modificadas.

- Para cada imagem gerada, o link e a legenda correspondentes são salvos em um arquivo `links.txt` para referência futura.

Fique à vontade para customizar o script de acordo com as necessidades do seu projeto!
