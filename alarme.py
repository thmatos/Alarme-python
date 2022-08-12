from time import localtime
import winsound

h = input("coloque o horário desejado: ")
m = input("coloque o minuto desejado: ")

while True: 
    if localtime().tm_hour == int(h) and localtime().tm_min == int(m):
        print("Acooooooooorda...")
        winsound.PlaySound("samsung.wav", winsound.SND_FILENAME)
        break 
    
