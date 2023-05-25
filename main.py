print('Bem Vindo a Loja do Paulo Cesar Maximiano Ferdin')
preco = int(input('Qual o valor do produto?'))
quantidade = int(input('Qual a quantidade?'))
#acima os input para poder captar os dados, em baixo o calculo do total do valor.
valor = preco * quantidade
#foram criados os descontos a serem aplicados em cada caso.
descontoum = valor - (valor * 0.05)
descontodois = valor - (valor * 0.10)
descontotres = valor - (valor * 0.15)

print('O valor sem o desconto é R${:.2f}!'.format(valor))

if (quantidade <= 9):
    print('O valor não tem desconto!')
elif (quantidade <= 99):
    print('O valor com o desconto é R${:.2f}! (desconto de 5%)'.format(descontoum))
elif (quantidade <= 999):
    print('O valor com o desconto é R${:.2f}! (desconto de 10%)'.format(descontodois))
elif (quantidade >= 1000):
    print('O valor com o desconto é R${:.2f}! (desconto de 15%)'.format(descontotres))
#acima, levando em relação a quantidade de produto será dado o desconto como pedido no exercicios.
