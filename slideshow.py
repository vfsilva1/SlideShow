import glob, os
import cv2
import keyboard
import time

path = r"C:\Users\160098\Pictures\Corongas"
while True:
    if keyboard.is_pressed('q') or keyboard.is_pressed('Q'):
            cv2.destroyAllWindows()
            break
    for img in os.listdir(path):
        caminhoImg = os.path.join(path, img)
        imagem = cv2.imread(caminhoImg)
        roi = imagem[:512, :512]
        cv2.imshow('Coronga', roi)
        time.sleep(5)
            