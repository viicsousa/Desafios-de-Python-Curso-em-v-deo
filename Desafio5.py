from time import sleep
salario=float(input('Qual o seu salário atual?'))
print('Seu salário atual é {:.2f}'.format(salario))
print('Com o aumento seu salário atual será de...')
print('Processando...')
sleep(3)
if salario>1250:
    aumento= (salario*10/100)+salario
    print('Seu salário atual é de R${:.2f}.'.format(aumento))
else:
    aumento= (salario*15/100)+salario
    print('Seu salário atual é de {:.2f}.'.format(aumento))