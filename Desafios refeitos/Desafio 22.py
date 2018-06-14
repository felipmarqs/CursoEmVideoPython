#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas;
#O nome com todas minúsculas
#Quantas letras ao todo(sem considerar espaços).
#quantas letras tem o primeiro nome.
nome = str(input('Qual seu nome ? ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}.')
print(f'Seu nome em minúsculas é {nome.lower()}.')
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras. '.format(nome.find(' ')))
