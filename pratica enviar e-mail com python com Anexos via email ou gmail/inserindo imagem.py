from tkinter import *

janela = Tk()

img = PhotoImage(file="livro.jpeg")
livro = Label(janela, image= img)
livro.place(x=50,y=50)