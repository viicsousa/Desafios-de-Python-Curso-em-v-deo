n = int(input("Digite um número inteiro:"))
c = int(input("Para converter {} para binário digite 1; para octal digite 2; para hexadecimal digite 3;".format(n)))

if c == 1:
    print('O número {} convertido para binário é {}.'.format(n, bin(n)[2:]))
elif c==2:
    print ('O número {} convertido para octal é {}.'.format(n, oct(n)[2:]))
elif c ==3:
    print ('O número {} convertido para hexadecimal é {}.' .format (n , hex(n)[2:]))
else:
    print('Opção inválida.') 