peso = float(input('Qual seu peso em kilos?'))
altura = float(input('Qual sua altura em centímetros?'))
imc = (peso / altura / altura) * 10000
if imc < 18.5:
    print('Seu IMC é {:.1f} e você está abaixo do peso.'.format(imc))
elif imc > 18.5 and imc < 25:
    print('Seu IMC é {:.1f} e você está no peso ideal.'.format(imc))
elif imc > 25 and imc < 30:
    print('Seu IMC é {:.1f} e você está com sobrepeso.'.format(imc))
elif imc > 30 and imc < 40:
    print('Seu IMC é {:.1f} e você está com obesidade.'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.1f} e você está com obesidade mórbida'.format(imc))