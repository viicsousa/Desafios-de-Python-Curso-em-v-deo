import random
nusu=int(input('O computador vai escolher um número, escolha um número de 0 á 5 para tentar acertar o número do computador:'))
lista = [0,1,2,3,4,5]
npc = random.choice(lista)
print ('O número que o computador escolheu foi {}'.format (npc))
if npc==nusu:
    print ('Parabéns, você venceu!')
else:
    print ('Você perdeu! Tente novamente.')
print('--FIM--') 