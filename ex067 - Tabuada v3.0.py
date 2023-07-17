'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.'''


numero = 0

while True:
    print('---------------------------------------------------')
    numero = int(input('Quer ver a tabuada de qual valor: '))
    if numero < 0:
        print('Tabuada encerrada, Volte Sempre!')
        break
    for valor in range(1, 11):
        tabuada = numero * valor
        print(f'{numero} x {valor} = {tabuada}')
