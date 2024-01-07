from openai import OpenAI
import os
import requests
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def edita_imagem(input_image_path, output_image_path, text_to_add):
    # Abre a imagem
    image = Image.open(input_image_path)

    # Calcula a nova altura da imagem
    original_width, original_height = image.size
    new_height = int(original_height * 1.1)

    # Create uma imagem expandida
    new_image = Image.new("RGB", (original_width, new_height), "white")
    new_image.paste(image, (0, 0))

    # Cria um objeto de desenho
    draw = ImageDraw.Draw(new_image)

    # Especifica a fonte desejada
    font = ImageFont.truetype(os.path.join("C:\Windows\Fonts\Candaral.ttf"), int(new_height*0.05))

    # Calcula a posição do centro da imagem
    text_bbox = draw.textbbox((0, 0), text_to_add, font=font)
    text_position = ((original_width - text_bbox[2]) // 2, original_height)

    # Escreve na imagem
    draw.text(text_position, text_to_add, font=font, fill="black",size=20)

    # Salva a imagem editada
    new_image.save(output_image_path)

def download_and_save_image(url, filename,projeto):
    # Construindo path para o arquvio
    file_path = os.path.join("imagens",projeto, f"{filename}.png")

    try:
        # Faz download da imagem
        response = requests.get(url)
        response.raise_for_status()

        # Salva a imagem no caminho e com o nome especificado
        with open(file_path, 'wb') as file:
            file.write(response.content)

    except Exception as e:
        print(f"Error downloading or saving the image: {str(e)}")
        exit()

def gera_imagem(verso, client,filename,projeto):
    try:
        prompt = " Style: 'Doodle'. " + verso + " #illustration #drawing #cartoonsforadults #story #SFW #safeforwork"""

        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url

        open(f".\\imagens\\{projeto}\\links.txt","a").write(f"\n{verso} - {image_url}")

        download_and_save_image(image_url, filename, projeto);

    except Exception as e:
        print(str(e))
        exit()

if __name__ == "__main__":
    try:
        client = OpenAI(
            api_key='SUA_CHAVE_DA_API_AQUI'
        )

        projeto = input("Nome do projeto: ");
        file = Path(input("\nInsira o path para o arquivo com a letra da música: "))
        audio = input("\nInsira o path para o arquivo de áudio:  ")

        if input("\nDigite 'n' para cancelar, ou aperte ENTER para continuar: ") == 'n':
            exit()

        os.makedirs(f".\\imagens\\{projeto}", exist_ok=True)
        os.makedirs(f".\\imagens\\com_texto\\{projeto}", exist_ok=True)

        musica = open(file,"r", encoding='utf-8').read()
    
        versos = musica.split("\n")

        i = 0
        for verso in versos:
            if verso != " " and verso != "":
                gera_imagem(verso, client,i,projeto)
                edita_imagem(f".\\imagens\\{projeto}\\{i}.png", f".\\imagens\\com_texto\\{projeto}\\{i}.png", verso)
                i = i + 1;

        print(f"As imagens para seu vídeo já estão prontas em imagens\\com_texto\\{projeto} as imagens originais se encontram em imagens\\{projeto}")

    except Exception as e:
        print(str(e))
        exit()
