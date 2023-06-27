# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$'))
desconto = preco * 5 / 100
precoNovo = preco - desconto

print('Este produto com 5% de desconto fica no valor de R${:.2f}'.format(precoNovo))

