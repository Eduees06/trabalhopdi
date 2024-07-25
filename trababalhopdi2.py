import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def gerar_fatia(face, i):
    if face < 1 or face > 6:
        raise ValueError("A face deve ser um valor entre 1 e 6.")
    if i < 0 or i > 255:
        raise ValueError("O valor de i deve estar entre 0 e 255.")
    
    fatia = np.zeros((256, 256, 3), dtype=np.uint8)
    
    # Cria gradientes que variam de 0 a 255 ao longo das dimensões
    gradiente = np.arange(256)
    gradiente_r, gradiente_g = np.meshgrid(gradiente, gradiente)
    gradiente_b = gradiente_r[:, ::-1]  # Inverte horizontalmente o gradiente

    # Define a fatia de acordo com a face escolhida
    if face == 1:
        fatia[:, :, 0] = i  # Canal R fixo
        fatia[:, :, 1] = gradiente_g  # Canal G variável
        fatia[:, :, 2] = gradiente_b  # Canal B variável
    elif face == 2:
        fatia[:, :, 1] = i  # Canal G fixo
        fatia[:, :, 0] = gradiente_r  # Canal R variável
        fatia[:, :, 2] = gradiente_b  # Canal B variável
    elif face == 3:
        fatia[:, :, 2] = i  # Canal B fixo
        fatia[:, :, 0] = gradiente_r  # Canal R variável
        fatia[:, :, 1] = gradiente_g  # Canal G variável
    elif face == 4:
        fatia[:, :, 0] = 255 - i  # Canal R invertido
        fatia[:, :, 1] = gradiente_g  # Canal G variável
        fatia[:, :, 2] = gradiente_b  # Canal B variável
    elif face == 5:
        fatia[:, :, 1] = 255 - i  # Canal G invertido
        fatia[:, :, 0] = gradiente_r  # Canal R variável
        fatia[:, :, 2] = gradiente_b  # Canal B variável
    elif face == 6:
        fatia[:, :, 2] = 255 - i  # Canal B invertido
        fatia[:, :, 0] = gradiente_r  # Canal R variável
        fatia[:, :, 1] = gradiente_g  # Canal G variável
    
    return fatia

def mostrar_fatia(face, i):
    fatia = gerar_fatia(face, i)
    plt.imshow(fatia)
    plt.title(f"Fatia do Cubo RGB - Face {face}, i = {i}")
    plt.axis('off')
    plt.show()

def salvar_fatia(face, i, caminho):
    fatia = gerar_fatia(face, i)
    imagem_rgb = Image.fromarray(fatia, 'RGB')
    imagem_rgb.save(caminho)

if __name__ == "__main__":
    for face in range(1, 7):
        for i in [0, 128, 255]:
            mostrar_fatia(face, i)
            salvar_fatia(face, i, f"fatia_{face}_{i}.png")