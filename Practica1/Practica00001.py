from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter.font import Font
import math
import random

def Euclides(m, n):
	r=0
	while (n!=0):
		r=m%n
		m=n
		n=r
	return m

def Inverse(y,p):
    (b,z,x)=ExtEuclidean(y,p)
    if(z<0):
        z=z+p
    return z

def ExtEuclidean(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    numiteraciones = 0
    while a:
        (q, a), b = (b // a, b % a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
        numiteraciones += 1
    return b, x0, y0

#Numero que se pueden usar, Pd: no hace nada , checarlo
def generar(n):
    probables=[]
    a=1
    b=n
    for i in range (a,b+1):
        if math.gcd(i,b)==1:
            probables.append(i)
    print("Números que se pueden usar: ",probables)
    #generar alpha
    alpha,beta=random.sample(probables,2)
    #print(alpha,beta)
    return alpha,beta
    #generar betha

def num_to_char(n):
    m = chr(n + 97)
    return m

def char_to_num(k):
    z = (ord(k.lower()) - 97)
    return z

def InversoAditivo(beta,n):
    if beta > 0:
        addInv=n - beta
    else:
        addInv = n + beta
    return addInv

#Funcion para validar Alpha
def validaciondealpha():
    a=int(espacioDeEntradaParaAlpha.get())
    n=int(espacioDeEntradaParaN.get())
    if(Euclides(a,n)==1):
        messagebox.showinfo("Alpha","El valor de Alpha es valido")
    else:
        messagebox.showinfo("Alpha","El valor de Alpha no es valid. Introduzca un nuevo valor para Alpha")

#Funcion para validar Beta
def validaciondebeta():
    b=int(espacioDeEntradaParaBeta.get())
    n=int(espacioDeEntradaParaN.get())
    if(Euclides(b,n)==1):
        messagebox.showinfo("Beta","El valor de Beta es valido")
    else:
        messagebox.showinfo("Beta","El valor de Beta no es valido. Introduzca un nuevo valor para Beta")

#Creación de la ventana
ventana=Tk()
ventana.title("Práctica 1 AE y AEE")
ventana.resizable(0,0)
ventana.geometry("800x500")
ventana.config(bg="black")
mediumFont = Font( family="Arial",size=20,weight="bold", )
#Cración de los textos de Ingresar
textoAlpha=Label(ventana, text = "Ingrese Alpha:",bg="white",font=mediumFont)
textoAlpha.place(x=90,y=150)
textoBeta=Label(ventana, text = "Ingrese Beta:",bg="white",font=mediumFont)
textoBeta.place(x=320,y=150)
textoN=Label(ventana, text = "Ingrese n:",bg="white",font=mediumFont)
textoN.place(x=540,y=150)
#Espacios de Entrada de los valores
espacioDeEntradaParaAlpha = Entry(ventana)
espacioDeEntradaParaAlpha.place(x=130,y=220)
espacioDeEntradaParaBeta = Entry(ventana)
espacioDeEntradaParaBeta.place(x=350,y=220)
espacioDeEntradaParaN = Entry(ventana)
espacioDeEntradaParaN.place(x=550,y=220)

botonValidarAlpha=Button(ventana, text="Validar Alpha",command=validaciondealpha,bg="white",font=mediumFont)
botonValidarAlpha.place(x=170,y=350)
botonValidarBeta=Button(ventana, text="Validar Beta",command=validaciondebeta,bg="white",font=mediumFont)
botonValidarBeta.place(x=450,y=350)

t=int(input("Ingresa el valor de alpha: "))
u=int(input("Ingresa el valor de n: "))
print("GCD: ",Euclides(t,u))
if(Euclides(t,u)==1):
    print("Inverso Multiplicativo: ",Inverse(t,u))
else:
    print("Error vuelva a ingresar los datos\n")

ventana.mainloop()