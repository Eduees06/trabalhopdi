import numpy as np
import cv2
import matplotlib.pyplot as plt

def gerar_fatia(face, i):
    if face < 1 or face > 6:
        raise ValueError("A face deve ser um valor entre 1 e 6.")
    if i < 0 or i > 255:
        raise ValueError("O valor de i deve estar entre 0 e 255.")
    
    fatia = np.zeros((256, 256, 3), dtype=np.uint8)
    
    # Define a fatia de acordo com a face escolhida
    if face == 1:
        fatia[:, :, 0] = i
    elif face == 2:
        fatia[:, :, 1] = i
    elif face == 3:
        fatia[:, :, 2] = i
    elif face == 4:
        fatia[:, :, 0] = 255 - i
    elif face == 5:
        fatia[:, :, 1] = 255 - i
    elif face == 6:
        fatia[:, :, 2] = 255 - i
    
    # Preenche as outras dimensões com valores de 0 a 255
    fatia[:, :, 1] = np.arange(256).reshape(1, 256).repeat(256, axis=0)
    fatia[:, :, 2] = np.arange(256).reshape(256, 1).repeat(256, axis=1)
    
    return fatia

def mostrar_fatia(face, i):
    fatia = gerar_fatia(face, i)
    plt.imshow(fatia)
    plt.title(f"Fatia do Cubo RGB - Face {face}, i = {i}")
    plt.axis('off')
    plt.show()

def salvar_fatia(face, i, caminho):
    fatia = gerar_fatia(face, i)
    cv2.imwrite(caminho, fatia)

if __name__ == "__main__":
    face = 6
    i = 33
    mostrar_fatia(face, i)
    salvar_fatia(face, i, f"fatia_{face}_{i}.png")