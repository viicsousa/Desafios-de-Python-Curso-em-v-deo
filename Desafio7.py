casa = float(input("Qual o valor da casa que quer comprar? R$"))
salario = float (input("Qual o valor do seu salário?R$"))
anos = int (input("Em quantos anos pretender pagar a casa?R$"))
limite = (salario*30)/100
parcela = casa/(anos*12)
if parcela >= limite:
    print ('Seu emprestimo foi negado. O valor da prestação é muito alto.')
else:
    print('Emprestismo concedido. O valor da sua prestação mensal vai ser de R${:.2f}.'.format(parcela)) 