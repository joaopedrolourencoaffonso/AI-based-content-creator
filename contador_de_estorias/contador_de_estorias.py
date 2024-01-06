from openai import OpenAI
from random import randint
import os
import requests

# Gera narração de áudi
def narration(client, titulo, story):
    try:
        # chama a API para gerar um áudio a partir da estória
        response = client.audio.speech.create(
            model="tts-1",
            voice="shimmer",
            input=story
        )
        
        # Salva o áudio em um arquivo mp3
        response.stream_to_file(f".\\estoria\\{titulo}\\{titulo}.mp3")
        
        # Retorna 1 indicando sucesso
        return 1
    
    except Exception as e:
        # Retorna a mensagem de erro
        return str(e)

# Function to append a string to a file
def append_string_to_file(file_path, content):
    try:
        # Open the file in 'append' mode ('a')
        with open(file_path, 'a') as file:
            # Write the provided content to the file, followed by a newline character
            file.write(content + '\n')
    except Exception as e:
        # If an exception occurs during the process, print an error message
        print(f'Error appending string to {file_path}: {str(e)}')


def download_and_save_image(url, titulo, image_name):
    # Create the "imagens" folder if it doesn't exist
    folder_path = f".\\estoria\\{titulo}\\imagens"
    os.makedirs(folder_path, exist_ok=True)

    # Build the file path with the random name and original file extension
    file_path = os.path.join(folder_path, f"{image_name}.png")

    try:
        # Make a request to download the image
        response = requests.get(url)
        response.raise_for_status()

        # Save the image to the specified file path
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"Image downloaded and saved: {file_path}")
    except Exception as e:
        print(f"Error downloading or saving the image: {str(e)}")

# Gera prompts para o dalle-3 com base nos parágrafos de texto providos
def prompt_generator(client, scene):
  try:
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": f"Based on the following scene, create a prompt for a (safe for all family) ai generated image: '{scene}' #illustration #drawing #wordless #SFW"}
      ]
    )

    return str(completion.choices[0].message.content)

  except Exception as e:
    return str(e);

# Lê o arquivo com a estória
def reader(titulo):
  try:
    story = open(f".\\estoria\\{titulo}\\{titulo}.txt","r").read();

    return story, 1;

  except Exception as e:
    return 0, str(e)

# Envia uma requisição à API e salva a resposta em um arquivo
def story_creator(client, premissa, titulo):
  try:
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "Você é um escritor que adora criar mundos de fantasia e terras distantes."},
        {"role": "user", "content": "Escreva uma história de fantasia com o seguinte título e premissa. Não divida a história em capítulos: \n" + premissa}
      ]
    )
    
    filepath = os.path.join('.\\estoria', titulo, titulo + ".txt")
    
    f = open(filepath, "w")
    f.write(str(completion.choices[0].message.content))
    f.close()

    return 1

  except Exception as e:
    return str(e);

# Função principal para executar o processo de criação de histórias, geração de imagens e narração
def main():
  # Entrada do usuário para título e premissa da história
  titulo = input("Título da estória\n-> ")
  premissa = input("Premissa da estória (só aperte enter para submeter)\n-> ")

  # Cria diretórios com base na entrada do usuário
  os.makedirs(".\\estoria\\" + titulo, exist_ok=True);

  #inicializa o cliente da API
  try:
    client = OpenAI(
      api_key='SUA_CHAVE_DA_API_AQUI'
    )
  except Exception as e:
    print(e)
    exit();

  #concatena título e premissa
  premissa = f"Title: {titulo} - Premisse: {premissa}"
  
  #Chama a função story_creator para criar a história e salvá-la em um arquivo de texto
  retorno = story_creator(client,premissa, titulo)

  # Lida com erros durante a criação da história
  if retorno != 1:
    print(retorno)
    exit();

  # 'Limpa' o texto da estória
  story, retorno = reader(titulo);
  
  if retorno != 1:
    print(retorno)
    exit();

  # Divide a história em cenas
  story = story.split("\n\n");

  i = 0;
  for scene in story:
    
    # Gera um prompt para geração de imagem IA com base na cena
    prompt = prompt_generator(client, scene)

    # Gera uma imagem usando a API OpenAI Images
    response = client.images.generate(
      model="dall-e-3",
      prompt=prompt,
      size="1024x1024",
      quality="standard",
      n=1,
    )
    # pegando a URL da imagem
    image_url = response.data[0].url

    # Baixe e salve a imagem gerada
    download_and_save_image(image_url,titulo,i)

    # Anexa o prompt usado a um arquivo
    append_string_to_file(f".\\estoria\\{titulo}\\prompts_usados.txt",f"scene {i}: {prompt}");
    
    i = i + 1;

  # Concatena as cenas em uma única história
  story = ' '.join(story)
  retorno = narration(client,titulo, story);

  # Lida com erros durante a narração
  if retorno != 1:
    print(retorno)

  print(f"'{titulo}' foi escrita, desenhada e narrada com sucesso!")

if __name__ == "__main__":
  main();
