# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO
#--------------------------------------------------------------------------------------------------------------------------------------------


n1 = float(input('Sua primeira nota: '))
n2 = float(input('Sua segunda note: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('De acordo com suas notas {} e {}.\nSua média é de {:.1f}, você está REPROVADO!!!'.format(n1, n2, media))
elif media >= 5.0 and media <= 6.9:
    print('De acordo com sua notas {} e {}.\nSua média é de {:.1f}, você está de RECUPERAÇÂO!!!'.format(n1, n2, media))
elif media >= 7.0:
    print('De acordo com suas notas {} e {}.\nSua média é de {:.1f}, você está APROVADO!!!'.format(n1, n2, media))


