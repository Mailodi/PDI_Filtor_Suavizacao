from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def suavizar_imagem(imagem, raio_vizinhanca):
    imagem_array = np.array(imagem)
    largura, altura, canais = imagem_array.shape
    nova_imagem_array = np.copy(imagem_array)
    
    for x in range(raio_vizinhanca, largura - raio_vizinhanca):
        for y in range(raio_vizinhanca, altura - raio_vizinhanca):
            vizinhanca = imagem_array[x - raio_vizinhanca:x + raio_vizinhanca + 1,
                                      y - raio_vizinhanca:y + raio_vizinhanca + 1]
            media = np.mean(vizinhanca, axis=(0, 1))
            nova_imagem_array[x, y] = media.astype(int)
    
    nova_imagem = Image.fromarray(nova_imagem_array)
    return nova_imagem

imagem_entrada = Image.open("C:/Users/Win10/Documents/VisualStudio Projetos/PDI_FILTRO_Suavização/FILTRO_Suavizacao/Lena2.png")

plt.figure(figsize=(15, 5))

# Plot da imagem original
plt.subplot(1, 5, 1)
plt.title("Original")
plt.imshow(imagem_entrada)
plt.axis('off')

# Valores da mascara de tamanhos
Val_mascaras = [1, 3, 5, 7]

# Aplique o filtro de suavização para diferentes valores de mascara_vizinhanca
for i, mascara in enumerate(Val_mascaras):
    imagem_suavizada = suavizar_imagem(imagem_entrada, mascara)
    
    # Plot da imagem suavizada
    plt.subplot(1, 5, i + 2)
    plt.title(f"Mascara {mascara}")
    plt.imshow(imagem_suavizada)
    plt.axis('off')

plt.tight_layout()
plt.show()
