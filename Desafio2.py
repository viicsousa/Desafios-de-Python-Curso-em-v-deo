vel= float(input('Em qual velocidade seu carro pecorreu o curso?'))
multa= (vel-80)*7.00
if vel>80:
    print('Você foi multado. O valor a se para é R$ {:.2f}'.format (multa))
else:
    print('Bom trabalho! Continue respeitando as leis de trânsito.') 