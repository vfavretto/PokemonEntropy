# Importar bibliotecas
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage.filters import sobel
from skimage.feature import canny
from google.colab import files

# Upload de arquivos
print("Faça o upload das imagens dos Pokémons:")
uploaded = files.upload()

# Inicializar listas para armazenar resultados
results = []
names = []

# Processar cada imagem enviada
for filename in uploaded.keys():
    # Ler a imagem usando PIL e converter para escala de cinza com transparência preservada
    img_pil = Image.open(filename).convert("RGBA")
    arr = np.array(img_pil)
    alpha_channel = arr[:, :, 3]  # Canal alfa para transparência

    # Manter apenas pixels com transparência baixa (não transparentes)
    gray_img = np.dot(arr[:, :, :3], [0.2989, 0.587, 0.114]).astype(np.uint8)
    gray_img[alpha_channel == 0] = 255  # Tornar fundo transparente branco

    # Operar com a imagem convertida para escala de cinza
    img = gray_img

    # Operações morfológicas
    kernel = np.ones((4,4), np.uint8)
    dilation = cv2.dilate(img, kernel, iterations=1)
    diff = cv2.subtract(dilation, img)
    negaposi = 255 - diff

    # Calcular número total de pixels do Pokémon
    total_pokemon_pixels = np.where((img < 250) & (alpha_channel > 0), 1, 0).sum()

    # Calcular número de pixels da linha principal
    main_line_pixels = np.where((negaposi.flatten() < 250) & (alpha_channel.flatten() > 0), 1, 0).sum()

    # Calcular a proporção de informação
    informacao_total = main_line_pixels / total_pokemon_pixels

    # Armazenar resultados
    results.append(informacao_total)
    names.append(filename)

    # Visualizações para cada imagem
    plt.figure(figsize=(15,5))

    plt.subplot(131)
    plt.title('Imagem Original')
    plt.imshow(img, cmap='gray')

    plt.subplot(132)
    plt.title('Dilatação')
    plt.imshow(dilation, cmap='gray')

    plt.subplot(133)
    plt.title('Negaposi')
    plt.imshow(negaposi, cmap='gray')

    plt.tight_layout()
    plt.show()

    # Imprimir resultados para a imagem atual
    print(f"Imagem: {filename}")
    print(f"Número total de pixels do Pokémon: {total_pokemon_pixels}")
    print(f"Número de pixels da linha principal: {main_line_pixels}")
    print(f"Proporção de informação (total de pixels / linha principal): {informacao_total:.4f}\n")

# Gráfico comparativo dos resultados
plt.figure(figsize=(10, 6))
plt.plot(names, results, marker='o')
plt.title('Proporção de Informação por Imagem')
plt.xlabel('Imagem')
plt.ylabel('Proporção de Informação')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()