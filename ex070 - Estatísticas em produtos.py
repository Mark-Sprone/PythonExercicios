'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''


precoMaior = 0
total = 0
produtoBarato = 0
cont = 0
barato = ''

while True:
    print('------------------------------PRODUTOS----------------------------')
    nome = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço do produto: R$'))
    
    cont += 1
    if preco > 1000:
        precoMaior += 1
    total += preco
   
    if cont == 1:
        produtoBarato = preco
        barato = nome
    else:
        if preco < produtoBarato:
            produtoBarato = preco
    
    pergunta = ' '
    while pergunta not in 'SN':
       pergunta = str(input('Tem mais Produtos? [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        break
print('-----------------------------------------------------------------------')
print(f'O valor total gasto na compra foi de R${total:.2f}')
print(f'{precoMaior} produtos custam mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${produtoBarato:.2f}')   