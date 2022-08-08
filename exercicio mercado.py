estoque_mercado = {
'legumes': '15,99',
'mistura': '60,00',
'arroz': '8,00',
'feijão': '10,00',
'salada': '4,99',
'salgados': '20,00',
'doces': '10,00',
}

#valores
print(estoque_mercado.values())

print(estoque_mercado.get("legumes","mistura"))
