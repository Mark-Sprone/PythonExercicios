# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


km = float(input('Digite a quantidade de Km percorrido: '))
dias = int(input('Digite a quantidade de dias: '))
calculoDias = dias * 60
calculoKm = km * 0.15

print('O valor a pagar é de R${:.2f}'.format(calculoDias + calculoKm))
