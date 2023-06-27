# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m².

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
ar = l * a
t = ar / 2

print('A área desta parede é de {:.2f}m²'.format(ar))
print('A quantidade de tinta necessária será de {:.2f} litros'.format(t))
