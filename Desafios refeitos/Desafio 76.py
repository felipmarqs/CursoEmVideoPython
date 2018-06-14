print('-'*40)
print(f'{"Listagem de preços":^40}')
print('-'*40)
listagem = ('Pão', 1,
            'Leite', 3.5,
            'Arroz', 2.99,
            'Café', 5.67,
            'Refrigerante', 3.99,
            'Fralda', 59.99,
            'Caneta', 22.30,
            'Compasso', 9.99,
            'Livro', 34.90)

for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end = '')
    else:
        print(f'R${listagem[pos]:>7}')
print('-'*40)