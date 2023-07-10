# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = str(input('Digite o Sexo [M/F]:' )).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Opção invalida! Digite o Sexo [M/F]: ')).upper().strip()

print('Sexo {} registrado'.format(sexo))