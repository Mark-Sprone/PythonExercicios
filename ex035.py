# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.


r1 = float(input('Comprimento da 1º reta: '))
r2 = float(input('Comprimento da 2º reta: '))
r3 = float(input('Comprimento da 3º reta: '))

if r3 < r1 + r2 and r2 < r1 + r3 and r1 < r2 + r3:
    print('Pode formar um triângulo!')
else:
    print('Não pode formar um triângulo!')