# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Digite o valor do ângulo: '))
rad = math.radians(ang)

cos = math.cos(rad)
sen = math.sin(rad)
tang = math.tan(rad)

print('O ângulo de {} tem o seno de {:.2f}'.format(ang, sen))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang, cos))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ang, tang))

