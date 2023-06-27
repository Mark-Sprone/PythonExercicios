# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.

salario = float(input('Digite o valor do salário: R$'))
salarioNovo = salario + (salario * 15 / 100)

print('O seu novo salário com aumento de 15% fica no valor de R${:.2f}'.format(salarioNovo))
