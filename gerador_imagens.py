import openai
import requests
import os
from io import BytesIO
from PIL import Image

def gerar_imagem(prompt):
    openai.api_key = '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'
    response = openai.Image.create(
        prompt = prompt,
        n=1,
        size = '1024x1024',
        response_format = 'url'
    )
    image_url = response['data'][0]['url']
    image_data = requests.get(image_url).content
    #converter a imagem para objeto pillow
    image = Image.open(BytesIO(image_data))
    #Exibir imagem
    image.show()

entrada = input('O que você quer que a IA gere?')
gerar_imagem(entrada) 
