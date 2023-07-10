'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar / [ 2 ] multiplicar / [ 3 ] maior / [ 4 ] novos números / [ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
--------------------------------------------------------------------------------------------------'''

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))

opcao = 0

while opcao != 5:
    print('''-------MENU-------
    [ 1 ] - SOMAR
    [ 2 ] - MULTIPLICAR
    [ 3 ] - MAIOR
    [ 4 ] - NOVOS NÚMEROS
    [ 5 ] - SAIR DO PROGRAMA''')
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        print('A soma dos valores {} e {} é : {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('O resultado da multiplicação de {} e {} é: {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('Entre os valores {} e {} o maior valor é: {}'.format(n1, n2, n1))
        else:
            print('Entre os valores {} e {} o maior valor é: {}'.format(n1, n2, n2))
    elif opcao == 4:
        print('Informe os números novamente...')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida!!')

print('Fim do Programa! Volte Sempre!')