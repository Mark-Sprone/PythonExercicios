# Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número: '))
ant = num - 1
suc = num + 1

print('O antecessor é {} e o sucessor é {}'.format(ant, suc))
