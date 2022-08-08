import os
import smtplib
from email.message import EmailMessage
from segredos import senha

#configurar email, senha
EMAIL_ADDRESS = 'marilopezlr@gmail.com'
EMAIL_PASSWORD = senha

msg = EmailMessage()
msg['Subject'] = 'estoque_mercado = {
'legumes': '15,99',
'mistura': '60,00',
'arroz': '8,00',
'feijao': '10,00',
'salada': '4,99',
'salgados': '20,00',
'doces': '10,00',
'frutas': '25,00',
'roupas': '100,00',
'utensilho': '33,00',
}
#valores
print(estoque_mercado.values())
print(estoque_mercado.get("legumes","mistura",))
print(estoque_mercado.get("salada",))'
msg['From'] = 'marilopezlr@gmail.com'
msg['To'] = 'iroquoisfunky@gmail.com'
msg.set_content('dict_values(['15,99', '60,00', '8,00', '10,00', '4,99', '20,00', '10,00', '25,00', '100,00', '33,00'])
15,99
4,99')
#enviar um e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
   smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
   smtp.send_message(msg)
