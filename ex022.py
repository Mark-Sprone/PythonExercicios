#  Crie um programa que leia o nome completo de uma pessoa e mostre:
#  O nome com todas as letras maiúsculas e minúsculas.
#  Quantas letras ao todo sem considerar espaços
# – Quantas letras tem o primeiro nome.

#--------------------------------------------------------------------------------------------------------------


nome = str(input('Digite seu nome completo: ')).strip()

nome.upper()
nome.lower()
primeiro = nome.split()

print('Seu nome em letras maiusculas é {}'.format(nome.upper()))

print('Seu nome em letras minusculas é {}'.format(nome.lower()))

print('Total de letras sem os espaços é {}'.format(len(nome) - nome.count(' ')))

print('Quantidade de letras do primeiro nome é {}'.format(len(primeiro[0])))