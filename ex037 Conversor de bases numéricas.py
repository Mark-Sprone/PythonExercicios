# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.


numero = int(input('Digite o número que deseja converter: '))
print('''Escola uma das bases para conversão:
[ 1 ] Converter para Binário.
[ 2 ] Converter para Octal.
[ 3 ] Converter para Hexadecimal.''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('O número {} convertido em binário é: {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {} convertido em Octal é: {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} convertido em Hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida, tente novamente!')
