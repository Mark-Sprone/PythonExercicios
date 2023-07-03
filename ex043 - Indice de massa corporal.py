# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
# -------------------------------------------------------------------------------------------------------------------

peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.1f}, você está abaixo do peso'.format(imc))
elif imc == 18.5 or imc < 25:
    print('Seu IMC é {:.1f}, você está no peso ideal'.format(imc))
elif imc == 25 or imc < 30:
    print('Seu IMC é {:.1f}, você está com Sobrepeso'.format(imc))
elif imc == 30 or imc < 40:
    print('Seu IMC é {:.1f}, você está com Obesidade'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.1f}, você está Obesidade Mórbida'.format(imc))
