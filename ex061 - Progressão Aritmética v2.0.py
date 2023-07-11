# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('GERADOR DE PA')
print('-=' * 10)
primeiroTermo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

c = 1
termo = primeiroTermo

print('Os dez primeiros termos da PA são: ')

while c <= 10:
    print('{} - '.format(termo), end='')
    c += 1
    termo += razao
print('FIM!')
    