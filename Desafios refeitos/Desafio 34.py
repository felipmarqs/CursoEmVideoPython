#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#Para inferiores ou iguais, o aumento é de 15%.

salário = float(input('Qual é o seu salário?'))
if salário > 1250.00:
    a = salário + (salário*0.10)
    print('Seu salário era de {:.2f} e com um aumento de 10% ficará {:.2f}'.format(salário,a))
else:
    b = salário + (salário*0.15)
    print('Seu salário era de {:.2f} e com um aumento de 15% ficará {:.2f}'.format(salário,b))
