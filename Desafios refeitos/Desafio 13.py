#Faça um algoritmo que leiao salário de um funcionário e mostre seu novo salário, com 15% de aumento.
print('Bom dia, trabalhador!')
salário = float(input('Poderia me informar seu salário? R$'))
aumento = (salário * 15/100) + salário
print('PARABÉNS!!!! Você recebeu um aumento de 15%, seu salário agora é R${aumento.:2f}.')