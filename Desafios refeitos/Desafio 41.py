from datetime import date
nasc = int(input('Qual o ano do seu nascimento?'))
idade = date.today().year - nasc
print('O atleta tem {} anos'.format(idade))
if idade <=9:
    print('Você se encaixa na categoria MIRIM')
elif idade <= 14:
    print('Você se encaixa na categoria INFANTIL')
elif idade <= 19:
    print('Você se encaixa na categoria JUNIOR')
elif idade <= 25:
    print('Você se encaixa na categoria SÊNIOR')
else:
    print('Você se encaixa na categoria MASTER')