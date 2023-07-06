# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0 #Acumula
cont = 0 #Contador
for intervalo in range(1, 501, 2):
    multiplos = intervalo % 3
    if multiplos == 0:
        soma = soma + intervalo #acumula valor
        cont =  cont + 1 #conta valor

print('A soma de todos os {} valores é: {}'.format(cont, soma))