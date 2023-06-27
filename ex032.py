# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import datetime

ano = int(input('Qual ano quer analisar? Ou coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = datetime.date.today().year    #pega o ano atual da maquina

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} não é Bissexto!'.format(ano))

