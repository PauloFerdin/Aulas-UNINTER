valor = int(input('Qual o valor a ser pago?'))

while True:
    if valor >= 100:
        cedulas100 = valor // 100
        valor = valor - cedulas100 * 100
        print('Você vai precisar de {} cédulas de R$100.'.format(cedulas100))
        if not valor:
            break
    if valor >= 50:
        cedulas50 = valor // 50
        valor = valor - cedulas50 * 50
        print('Você vai precisar de {} cédulas de R$50.'.format(cedulas50))
        if not valor:
            break
    if valor >= 25:
        cedulas25 = valor // 25
        valor = valor - cedulas25 * 25
        print('Você vai precisar de {} cédulas de R$25.'.format(cedulas25))
        if not valor:
            break
    if valor >= 10:
        cedulas10 = valor // 10
        valor = valor - cedulas10 * 10
        print('Você vai precisar de {} cédulas de R$10.'.format(cedulas10))
        if not valor:
            break
    if valor >= 5:
        cedulas5 = valor // 5
        valor = valor - cedulas5 * 5
        print('Você vai precisar de {} cédulas de R$5.'.format(cedulas5))
        if not valor:
            break
    if valor >= 1:
        cedulas1 = valor
        print('Você vai precisar de {} cédulas de R$1.'.format(cedulas1))
        break

print('Obrigado por usar o aplicativo!')