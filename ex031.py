# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.


viagem = float(input('Qual a distância em Km da viagem? '))

if viagem <= 200:
    print('O preço da sua passagem é de R${:.2f}'.format(viagem * 0.50))
else:
    print('O preço da sua passagem é de R${:.2f}'.format(viagem * 0.45))