#  Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#  Calcule e mostre o comprimento da hipotenusa.


import math

catOposto = float(input('Digite o comprimento do cateto oposto: '))
catAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.pow(catAdjacente, 2) + math.pow(catOposto, 2)

print('O valor da hipotenusa é de: {:.2f}'.format(math.sqrt(hipotenusa)))


# Existe a função math.hypot que faz o calculo da hipotenusa
