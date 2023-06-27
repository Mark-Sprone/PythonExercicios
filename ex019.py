#  Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#  Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
a1 = input('Digite o nome do 1º aluno: ')
a2 = input('Digite o nome do 2° aluno: ')
a3 = input('Digite o nome do 3º aluno: ')
a4 = input('Digite o nome do 4° aluno? ')

lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)

print('O aluno sorteado é {}'.format(sorteio))