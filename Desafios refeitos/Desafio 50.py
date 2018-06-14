soma = 0
cont = 0
for c in range(1, 7):
    número = int(input('Digite o {}º número: '.format(c)))
    if número % 2 == 0:
        soma += número
        cont += 1
print('Você informou {} números pares e a soma deles é {}. '.format(cont,soma))