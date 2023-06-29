# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
#-----------------------------------------------------------------------------------------------------------------------

import datetime
ano = int(input('Digite o ano de nascimento do candidato: '))

idade = datetime.date.today().year - ano

print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, datetime.date.today().year))

if idade == 18:
    print('Está na hora exata de você se alistar!')
elif idade > 18:
    print('Já passou do tempo do seu alistamento! Você deveria ter se alistado há {} anos'.format(idade - 18))
else:
    print('Ainda faltam {} anos para o seu alistamento, seu alistamento será em {}.'.format(18 - idade, datetime.date.today().year + (18 - idade)))






