print('Vou pedir que digite números separadamente para ver se formam um triângulo:')
a = float(input('Digite um número:'))
b = float(input('Digite outro número:'))
c = float(input('Digite outro número:'))
if (a+b>c) and (a+c>b) and (b+c>a):
    print('Os lados {}, {} e {} formam um triângulo.'.format(a,b,c))
else:
    print ('Não foi possível fazer um triângulo.') 