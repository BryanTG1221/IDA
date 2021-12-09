from tkinter import *
import os
import tkinter as tk

root = Tk()
fondo = PhotoImage(file = "D:\Imagenes\Saved Pictures\logo.png")
root.geometry("520x200")
root.resizable(False,False)
root.title("I.D.A")


class App:
    def __init__(self,master):
        self.frame = Frame(master)
        self.b = Button(self.frame,text = "IDA MANUAL",command = self.openfile)
        self.b.grid(row = 1)
        self.b = Button(self.frame,text = "IDA AUTOMÁTICO",command = self.openfile2)
        self.b.grid(row = 2)
        self.b = Button(self.frame,text = "DETECCION HOTWORD",command = self.openfile3)
        self.b.grid(row = 3)
        self.b = Button(self.frame,text = "CERRAR HOTWORD",command = self.CerrarArchivo)
        self.b.grid(row = 4)

        self.frame.grid()

    def openfile(self):
        os.startfile('C:\\Program Files (x86)\\IDA\\rougue-studios\\IDA\\scripts\\ida.py')
    def openfile2(self):
        os.startfile('C:\\Program Files (x86)\\IDA\\rougue-studios\\IDA\\scripts\\ida_automatico.py')
    def openfile3(self):
        os.startfile('C:\\Program Files (x86)\\IDA\\rougue-studios\\IDA\\scripts\\icon.py')
    def CerrarArchivo(self):
        Archivo = ('icon.py')
        Archivo.close()


app = App(root)
root.mainloop()