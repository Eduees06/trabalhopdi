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
        # Face 1: Canal R, valor fixo de G e B variando
        fatia[:, :, 0] = i
        fatia[:, :, 1] = np.arange(256).reshape(1, 256).repeat(256, axis=0)
        fatia[:, :, 2] = np.arange(256).reshape(256, 1).repeat(256, axis=1)
    elif face == 2:
        # Face 2: Canal G, valor fixo de R e B variando
        fatia[:, :, 1] = i
        fatia[:, :, 0] = np.arange(256).reshape(1, 256).repeat(256, axis=0)
        fatia[:, :, 2] = np.arange(256).reshape(256, 1).repeat(256, axis=1)
    elif face == 3:
        # Face 3: Canal B, valor fixo de R e G variando
        fatia[:, :, 2] = i
        fatia[:, :, 0] = np.arange(256).reshape(1, 256).repeat(256, axis=0)
        fatia[:, :, 1] = np.arange(256).reshape(256, 1).repeat(256, axis=1)
    elif face == 4:
        # Face 4: Canal R invertido, valor fixo de G e B variando
        fatia[:, :, 0] = 255 - i
        fatia[:, :, 1] = np.arange(256).reshape(1, 256).repeat(256, axis=0)
        fatia[:, :, 2] = np.arange(256).reshape(256, 1).repeat(256, axis=1)
    elif face == 5:
        # Face 5: Canal G invertido, valor fixo de R e B variando
        fatia[:, :, 1] = 255 - i
        fatia[:, :, 0] = np.arange(256).reshape(1, 256).repeat(256, axis=0)
        fatia[:, :, 2] = np.arange(256).reshape(256, 1).repeat(256, axis=1)
    elif face == 6:
        # Face 6: Canal B invertido, valor fixo de R e G variando
        fatia[:, :, 2] = 255 - i
        fatia[:, :, 0] = np.arange(256).reshape(1, 256).repeat(256, axis=0)
        fatia[:, :, 1] = np.arange(256).reshape(256, 1).repeat(256, axis=1)
    
    return fatia

def mostrar_fatia(face, i):
    fatia = gerar_fatia(face, i)
    plt.imshow(fatia)
    plt.title(f"Fatia do Cubo RGB - Face {face}, i = {i}")
    plt.axis('off')
    plt.show()

def salvar_fatia(face, i, caminho):
    fatia = gerar_fatia(face, i)
    cv2.imwrite(caminho, cv2.cvtColor(fatia, cv2.COLOR_RGB2BGR))

if __name__ == "__main__":
    option = 0
    
    while option != 2:
        print("Escolha uma opção:")
        print("1 - Gerar face")
        print("2 - Sair")
        option = int(input())
        
        if(option == 1):
            print("Escolha a face de 1 a 6:")
            face = int(input())
            print("Escolha a intensidade de 0 a 255:")
            i = int(input())
            mostrar_fatia(face, i)
            salvar_fatia(face, i, f"fatia_{face}_{i}.png")
            
        if(option != 1 and option != 2):
            print("Escolha uma opção válida!")
        