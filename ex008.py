# escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

n = float(input('Digite a distância em metros: '))
c = n * 100
m = n * 1000

print('O valor convertido em centimetros é: {:.0f}cm'.format(c))
print('O valor convertido em milimetros é: {:.0f}mm'.format(m))