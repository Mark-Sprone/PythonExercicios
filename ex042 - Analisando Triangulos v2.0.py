# Refaça o exercicio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
# – EQUILÁTERO: todos os lados iguais
#
# – ISÓSCELES: dois lados iguais, um diferente
#
# – ESCALENO: todos os lados diferentes

#---------------------------------------------------------------------------------------------------------------------


r1 = float(input('Comprimento da 1º reta: '))
r2 = float(input('Comprimento da 2º reta: '))
r3 = float(input('Comprimento da 3º reta: '))

if r3 < r1 + r2 and r2 < r1 + r3 and r1 < r2 + r3:
    print('Os segmentos acima podem formar um triângulo.')
    if r1 == r2 == r3:
        print('Forma um triângulo EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('Forma um triângulo ISÓSCELES!')
    else:
        print('Forma um triângulo ESCALENO!')
else:
    print('Não pode formar um triângulo!')