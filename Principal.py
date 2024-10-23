import random as r
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import time as t
#Método que aplica el Método de montecarlo
def montecarlo(lista):
    while(True):
        valor = r.random()
        if(valor < 0.076 and lista.__contains__(1)):
            lista.remove(1)
            return 1
        elif(valor < 0.153 and lista.__contains__(2)):
            lista.remove(2)
            return 2
        elif(valor < 0.23 and lista.__contains__(3)):
            lista.remove(3)
            return 3
        elif(valor < 0.30 and lista.__contains__(4)):
            lista.remove(4)
            return 4
        elif(valor < 0.38 and lista.__contains__(5)):
            lista.remove(5)
            return 5
        elif(valor < 0.46 and lista.__contains__(6)):
            lista.remove(6)
            return 6
        elif(valor < 0.53 and lista.__contains__(7)):
            lista.remove(7)
            return 7
        elif(valor < 0.61 and lista.__contains__(8)):
            lista.remove(8)
            return 8
        elif(valor < 0.69 and lista.__contains__(9)):
            lista.remove(9)
            return 9
        elif(valor < 0.76 and lista.__contains__(10)):
            lista.remove(10)
            return 10
        elif(valor < 0.84 and lista.__contains__(11)):
            lista.remove(11)
            return 11
        elif(valor < 0.92 and lista.__contains__(12)):
            lista.remove(12)
            return 12
        elif(lista.__contains__(13)):
            lista.remove(13)
            return 13

def main():    
    numero_blackjacks = 0 
    for i in range(num):
        corazones = [1,2,3,4,5,6,7,8,9,10,11,12,13] #11 = J | 12 = Q | 13 = K
        diamantes = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        treboles =  [1,2,3,4,5,6,7,8,9,10,11,12,13]
        rombos =    [1,2,3,4,5,6,7,8,9,10,11,12,13]
        x1 = 0
        x2 = 0
        print(f'simulacion numero: {i+1}')
        while((len(corazones) == 0 and len(diamantes) == 0 and len(treboles) == 0 and len(rombos) == 0) == False):
            global imagenx1p1
            global imagenx2p1
            global imagenx1p2
            global imagenx2p2
            global imagenx1p3
            global imagenx2p3
            global imagenx1p4
            global imagenx2p4 
            #reparte las cartas 1 vez entre los 4 jugadores
            for k in range(4):
                if(len(corazones) == 0 and len(diamantes) == 0 and len(treboles) == 0 and len(rombos) == 0):
                    break
                j = 0
                #reparte dos cartas usando el metodo de montecarlo
                while(j != 2):
                    valor = r.random()
                    if(valor < 0.25 and len(diamantes) != 0):
                        j += 1
                        if( j == 1):
                            x1 = montecarlo(diamantes)
                            imgx1 =  f"{x1}diamantes.png"
                        else:
                            x2 = montecarlo(diamantes)
                            imgx2 = f"{x2}diamantes.png"
                    elif(valor < 0.50 and len(corazones) != 0):
                        j += 1
                        if( j == 1):
                            x1 = montecarlo(corazones)
                            imgx1 =  f"{x1}corazones.png"
                        else:
                            x2 = montecarlo(corazones)
                            imgx2 =  f"{x2}corazones.png"
                    elif(valor < 0.75 and len(treboles) != 0):
                        j += 1
                        if( j == 1):
                            x1 = montecarlo(treboles)
                            imgx1 = f"{x1}treboles.png"
                        else:
                            x2 = montecarlo(treboles)
                            imgx2 =  f"{x2}treboles.png"
                    elif(len(rombos) != 0 ):
                        j += 1
                        if( j == 1):
                            x1 = montecarlo(rombos)
                            imgx1 = f"{x1}rombos.png"
                        else:
                            x2 = montecarlo(rombos)
                            imgx2 = f"{x2}rombos.png"
                #valida los 4 jugadores 
                if(k == 0 ):
                    imagenx1p1 = ImageTk.PhotoImage(Image.open(imgx1).resize((65, 95)))
                    imagenx2p1 = ImageTk.PhotoImage(Image.open(imgx2).resize((65, 95)))
                    tablero.create_image(150,5,image=imagenx1p1, anchor='n')
                    tablero.create_image(215,5,image=imagenx2p1, anchor='n')
                elif(k == 1):
                    imagenx1p2 = ImageTk.PhotoImage(Image.open(imgx1).resize((65, 95)))
                    imagenx2p2 = ImageTk.PhotoImage(Image.open(imgx2).resize((65, 95)))
                    tablero.create_image(70,250,image=imagenx1p2, anchor='e')
                    tablero.create_image(135,250,image=imagenx2p2, anchor='e')
                elif(k == 2):
                    imagenx1p3 = ImageTk.PhotoImage(Image.open(imgx1).resize((65, 95)))
                    imagenx2p3 = ImageTk.PhotoImage(Image.open(imgx2).resize((65, 95)))
                    tablero.create_image(245,250,image=imagenx1p3, anchor='w')
                    tablero.create_image(310,250,image=imagenx2p3, anchor='w')
                else:
                    imagenx1p4 = ImageTk.PhotoImage(Image.open(imgx1).resize((65, 95)))
                    imagenx2p4 = ImageTk.PhotoImage(Image.open(imgx2).resize((65, 95)))
                    tablero.create_image(150,450,image=imagenx1p4)
                    tablero.create_image(215,450,image=imagenx2p4)
                ventana.update() 
                t.sleep(0.1)
                #si uno tiene blackjack se imprime y almacena
                if(x1 > 10 or x2 > 10):
                    if(x1 == 1 or x2 == 1):
                        print("BlackJack!!!!")
                        numero_blackjacks += 1
    total_lanzamientos = 26*num
    porcentaje_victorias = int((numero_blackjacks/total_lanzamientos)*100)
    messagebox.showinfo(title='Pocentaje de blackjacks', message=f'de las {total_lanzamientos} veces en las que se repartieron 2 cartas, se tuvo {numero_blackjacks} blackjacks, lo que representa el {porcentaje_victorias}% de todas las simulaciones')
    print(f"numero blackjacks {numero_blackjacks}")

num = int(input("Cuantas veces quiere hacer la simulación: "))
ventana = tk.Tk()
ventana.title("BlackJack")
ventana.geometry("460x680")
boton = tk.Button(ventana, text= "Empzar", command=main)
tablero = tk.Canvas(ventana, bg="green", height="500")
tablero.pack()
boton.pack()
boton.place(x=210, y=640)
ventana.mainloop()

