tot18 = homens = mulheres20= 0
while True:
    print('-'*20)
    print(str('CADASTRE UMA PESSOA'))
    print('-'*20)
    idade = int(input('Idade: '))
    if idade >= 18:
        tot18 += 1
    sexo = str(input('Sexo:[M,F] ')).upper().strip()[0]
    while sexo not in 'FM':
        sexo = str(input('Sexo:[M,F] ')).upper().strip()[0]
    if sexo in 'M':
        homens += 1
    elif sexo in 'F' and idade >= 20:
        mulheres20 += 1
    print('-'*20)
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
print('=======FIM DO PROGRAMA=======')
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres20} mulheres com menos de 20 anos.')