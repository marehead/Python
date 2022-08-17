import os
import smtplib
from email.message import EmailMessage
from secrets import senha
from tkinter import *

janela = Tk()

img = PhotoImage(file="livro.jpeg")
livro = Label(janela, image= img)
livro.place(x=50,y=50)

#configurar emai e senha
EMAIL_ADRESS = 'marilopezlr@gmail.com'
EMAIL_PASSWORD = senha

#criar um email
msg = EmailMessage()
msg['Subject'] = 'seu produto chegou!!'
msg['from'] = 'marilopezlr@gmail.com'
msg['To'] = 'mbluesfera@gmail.com'
msg.set_content('Favor buscar o envio do produto que acabou de chegar ao seu destinho')


#enviar um e-mail
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)