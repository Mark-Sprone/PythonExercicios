#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('GERADOR DE PA')
print('-=' * 10)
primeiroTermo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

c = 1
termo = primeiroTermo
total = 0
mais = 10

print('Os dez primeiros termos da PA são: ')
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} - '.format(termo), end='')
        c += 1
        termo += razao
    print('PAUSA')
    mais = int(input('Quantos termos voçê quer mostrar a mais: '))
print('Progressão finalizada com {} termos mostrados'.format(total))

