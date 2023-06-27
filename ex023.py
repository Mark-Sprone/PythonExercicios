# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número entre 0 e 9999: '))

milhar = numero // 1000 % 10
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = numero // 1 % 10

print('Analisando o número: {}'.format(numero))

print('Milhar: {}'.format(milhar))
print('Centena: {}'.format(centena))
print('Dezena: {}'.format(dezena))
print('Unidade: {}'.format(unidade))



