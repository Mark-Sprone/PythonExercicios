# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

valor = int(input('Digite o número: '))

for n in range(1, 11):
    n1 = n * valor
    print('{} x {} = {}'.format(valor, n, n1))