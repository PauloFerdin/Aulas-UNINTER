print('Bem Vindo a Lanchonete do Paulo Cesar Maximiano Ferdin')
print('****************Cardápio****************')
print('| Código |        Descriçao        | Valor | ')
print('|  100   |     Cachorro Quente     |  9,00 | ')
print('|  101   |  Cachorro Quente Duplo  | 11,00 | ')
print('|  102   |          X-Egg          | 12,00 | ')
print('|  103   |        X-Salada         | 12,00 | ')
print('|  104   |         X-Bacon         | 14,00 | ')
print('|  105   |         X-Tudo          | 17,00 | ')
print('|  200   |    Refrigerante Lata    |  5,00 | ')
print('|  201   |        Chá Gelado       |  4,00 | ')

acumulador = 0 #colocar o 0 na frente do acumulador faz com que nas proximas vezes que ele for chamado, este então sera somado para que o resultado final saia o valor correto.

while True:#while utilizado para que fosse criado o laço!
    item = input('Entre com o código desejado:')
    if item != '100' and item != '101' and item != '102' and item != '103' and item != '104' and item != '105' and item != '200' and item != '201':
        print('Opção Inválida!')
        continue

    elif item == ('100'):
        print('Você pediu um Cachorro Quente no valor de R$9,00.')
        acumulador = acumulador + 9

    elif item == ('101'):
        print('Você pediu um Cachorro Quente Duplo no valor de R$11,00.')
        acumulador = acumulador + 11

    elif item == ('102'):
        print('Você pediu um X-Egg no valor de R$12,00.')
        acumulador = acumulador + 12

    elif item == ('103'):
        print('Você pediu um X-Salada no valor de R$12,00.')
        acumulador = acumulador + 12

    elif item == ('104'):
        print('Você pediu um X-Bacon no valor de R$14,00.')
        acumulador = acumulador + 14

    elif item == ('105'):
        print('Você pediu um X-Tudo no valor de R$17,00.')
        acumulador = acumulador + 17

    elif item == ('200'):
        print('Você pediu um Refrigerante Lata no valor de R$5,00.')
        acumulador = acumulador + 5

    elif item == ('201'):
        print('Você pediu um Chá Gelado no valor de R$4,00.')
        acumulador = acumulador + 4


    pedido = input('Deseja pedir mais alguma coisa?  \n' + '1 - Sim\n'+'2 - Não\n''>>') #\n foi usado para quebrar a linha, e o uso de >> foi para que facilitasse na hora de observar a posição em que o usuario deveria digitar o 1 ou 2.
    if (pedido == '1'):
        continue
    else:
        break
print('O valor total da sua compra é:R${:.2f}!'.format(acumulador))