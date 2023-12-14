from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem original
img = Image.open("C:/Users/Win10/Documents/VisualStudio Projetos/PDI_FILTRO_Suavização/FILTRO_Suavizacao/pml.png").convert('L')
img_noisy1 = np.array(img)

m, n = img_noisy1.shape

# Processar a imagem
img_new1 = np.zeros([m, n], dtype=np.uint8)

for i in range(1, m-1):
    for j in range(1, n-1):
        temp = [img_noisy1[i-1, j-1],
                img_noisy1[i-1, j],
                img_noisy1[i-1, j + 1],
                img_noisy1[i, j-1],
                img_noisy1[i, j],
                img_noisy1[i, j + 1],
                img_noisy1[i + 1, j-1],
                img_noisy1[i + 1, j],
                img_noisy1[i + 1, j + 1]]
        temp = sorted(temp)
        img_new1[i, j] = temp[4]

plt.figure(figsize=(10, 5))

# Imagem original
plt.subplot(1, 2, 1)
plt.title('Imagem Original')
plt.imshow(img_noisy1, cmap='gray')
plt.axis('off')

# Imagem processada
plt.subplot(1, 2, 2)
plt.title('Imagem Processada')
plt.imshow(img_new1, cmap='gray')
plt.axis('off')


plt.tight_layout()
plt.show()

