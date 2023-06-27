# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# (considere U$$1,00 = 3,27 reais)


n = float(input('Quanto em dinheiro você tem na carteira? R$'))
d = n / 4.88

print('Você tem em carteira',n,'reais')
print('Este valor em dólares corresponde á {:.2f} dólares'.format(d))

