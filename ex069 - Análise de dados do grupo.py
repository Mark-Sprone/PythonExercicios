'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''


maior = 0
homem = 0
mulheresMenor = 0


while True:
    print('-----------------------------------------------------------------')
    print('----------------CADASTRE A PESSOA--------------------------------')
    print('-----------------------------------------------------------------')
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        mulheresMenor += 1
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
print('--------------------------------------------------------------------')
print(f'O total de {maior} pessoas tem mais de 18 anos\n')
print(f'Total de {homem} homens cadastrados\n')
print(f'{mulheresMenor} mulheres tem menos de 20 anos\n')
print('-----------------PROGRAMA ENCERRADO!--------------------------------')