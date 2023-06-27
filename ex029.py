# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade que estava o veículo? '))


if velocidade > 80:
    print('Você foi multado, você excedeu o limite permitido de 80Km. Você deve pagar uma multa no valor de R${}'.format((velocidade - 80) * 7))
else:
    print('Você não foi multado, parabéns!!!')