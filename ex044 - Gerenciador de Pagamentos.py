'''  Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
--------------------------------------------------------------------------------------------------------------------------------------'''

preco = float(input('Preço do produto: R$'))

print('''FORMAS DE PAGAMENTO:
[1] À vista dinheiro ou cheque - Possui 10% de desconto
[2] À vista no cartão - Possui 5% de desconto
[3] 2x no cartão
[4] 3x ou mais no cartão - Possui juros de 20%''')
opcao = int(input('Qual a sua opção? '))

if opcao == 1:
    print('O produto de R${:.2f} a vista em dinheiro, tem 10% de desconto. Fica no valor de R${:.2f}'.format(preco, preco - (preco * 0.1)))
elif opcao == 2:
    print('O produto de R${:.2f} a vista no cartão, tem 5% de desconto. Fica no valor de R${:.2f}'.format(preco, preco - (preco * 0.05)))
elif opcao == 3:
    print('O produto de R${:.2f} em 2x no cartão, não possui desconto. Cada parcela fica no valor de R${:.2f}'.format(preco, preco / 2))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas: '))
    print('Sua compra será parcelada em {}x de R${:.2f} com juros\nSua compra de R${:.2f} vai custar R${:.2f} no final'.format(parcelas, (preco + preco * 0.2) / parcelas, preco, preco + (preco * 0.2)))
else:
    print('Opção inválida de pagamento. Tente novamente.')