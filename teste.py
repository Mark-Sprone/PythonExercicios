continuar = True

while continuar:
    print('''-------MENU-------
[ 1 ] - SOMAR
[ 2 ] - MULTIPLICAR
[ 3 ] - MAIOR
[ 4 ] - NOVOS NÚMEROS
[ 5 ] - SAIR DO PROGRAMA''')

opcao = int(input('Digite sua opção: '))

if opcao == 1:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    soma = valor1 + valor2
    print('O resultado da soma dos valor {} e {} é de {}'.format(valor1,valor2,soma))

elif opcao == 2:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    multi = valor1 * valor2
    print('O resultado da multiplicação entre {} e {} é de {}'.format(valor1, valor2, multi))

elif opcao == 3:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    maior = max(valor1, valor2)
    print('O maior valor entre {} e {} é de {}'.format(valor1,valor2,maior))

elif opcao == 4:
    continuar = True

elif opcao == 5:
    continuar == False
    print('Saindo do programa!!')

else:
    print('Opção inválida, digite novamente.')