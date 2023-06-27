#  Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#  A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('Seja Bem Vindo ao Banco Soluções!\n')

valorCasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))

parcela = valorCasa / (anos * 12)

print('Para pagar uma casa de R${:.2f} em {} anos a parcela será de R${}\n'.format(valorCasa, anos, parcela ))

if parcela > salario * 0.3:
    print('Sinto muito! A parcela de R${:.2f} excede 30% do seu salário, empréstimo negado.'.format(parcela))
else:
    print('Parabéns!!! Empréstimo liberado!!')