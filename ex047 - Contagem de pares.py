#  Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

#---------------------------------------------------------------------------------------------------------

for numero in range(1, 51):
    par = numero % 2
    if par == 0:
        print(numero, end=' ')
print('Acabou!')