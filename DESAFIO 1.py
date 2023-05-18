p = input('Qual operação deseja usar? +, -, / , * ou sair? ')
if p == '+' or p == '-' or p == '/' or p == '*':
    x = int(input('Qual o primeiro numero?'))
    y = int(input('Qual o segundo numero?'))

while (p != 'sair'):
    if ( p == '+'):
        print(x + y)
    elif ( p == '-'):
        print(x - y)
    elif ( p == '/'):
        print(x / y)
    elif ( p == '*'):
        print(x * y)
    else:
        print('obrigado por vir!')

    p = input('Qual operação deseja usar? +, -, / , * ou sair? ')
    if p == '+' or p == '-' or p == '/' or p == '*':
        x = int(input('Qual o primeiro numero?'))
        y = int(input('Qual o segundo numero?'))

print('Encerrando o programa...')


