print('Gerador de PA')
primeiro = int(input('Insira o primeiro termo: '))
razão = int(input('Insira a razão:'))
contador = 0
termo = primeiro
while contador <= 10:
    print('{}'.format(termo),end ='→ ')
    termo += razão
    contador += 1
print('FIM')