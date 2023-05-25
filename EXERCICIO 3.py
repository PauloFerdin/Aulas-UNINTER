print('Bem vindo a Companhia de Logistica Paulo Cesar Maximiano Ferdin S.A!')

def dimensõesObjeto():#aqui foi feito a primeira função, usada para dimensionar o volume do objeto!
    while True:#criado o primeiro laço
        try:#lembrando que deveria ser testado, como o item a frente necessita de um int porque vai ser usado um numero.
            comprimento = int(input('Digite o comprimento do Objeto em cm:'))
            tamanho = int(input('Digite a altura do Objeto em cm:'))
            largura = int(input('Digite a largura do Objeto em cm:'))

            volume = (comprimento * tamanho * largura)
            print('O volume do objeto em cm³:{}cm³!'.format(volume))

            if (volume <= 1000):
                return 10
            if (volume < 10000):
                return 20
            if (volume < 30000):
                return 30
            if (volume < 100000):
                return 50
            if (volume >= 100000):#Aqui é onde colocamos o limite do volume do produto.
                print('Não aceitamos objetos tão grandes!')
                print('Por favor, digite dimensões aceitaveis!')
                continue
            break



        except:
            print('Você digitou um valor não numerico!')
            print('Por favor, digite novamente as dimensões desejadas!')
            continue



def pesoObjeto():#segunda função, que será utilizado para determinar o peso do objeto.
    while True:
        try:
            peso = int(input('Digite o peso do Objeto em Kg:'))
            print('O peso do Objeto é: {} Kg'.format(peso))
            if (peso >= 30): #assim como limitamos o volume, também limitamos o peso.
                print('Peso acima do aceito, não aceitamos 30 kg ou mais.')
                continue
            if (peso <= 0.1):
                return 1
            if (peso < 1):
                return 1.5
            if (peso < 10):
                return 2
            if (peso < 30):
                return 3



            break
        except:
            print('Você digitou um valor não numerico!')
            print('Por favor, digite novamente as dimensões desejadas!')
            continue

def rotaObjeto():#terceira função, utilizado para a rota desejada pelo cliente.
    while True:
            print('RS - Rio de Janeiro a São Paulo')
            print('SR - São Paulo até o Rio de Janeiro')
            print('SB - De São Paulo até Brasília')
            print('BR - De Brasília até Rio de Janeiro')
            print('RB - Rio de Janeiro até Brasília')
            print('BS - De Brasília até São Paulo')
            rota = input('>>')#>> adicionado para facilitar a visualizacão do cliente.
            if rota != 'RS' and rota != 'SR' and rota != 'SB' and rota != 'BR' and rota != 'RB' and rota !='BS':
                print('Opção invalida!')
                print('Por favor escolha uma das opções corretas. (RS,SR,SB,BR,RB,BS)')
                continue
            elif rota == ('RS'):
                return 1
            elif rota == ('SR'):
                return 1
            elif rota == ('SB'):
                return 1.2
            elif rota == ('BR'):
                return 1.5
            elif rota == ('RB'):
                return 1.5
            elif rota == ('BS'):
                return 1.2
            break



tamanho = dimensõesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()

total = tamanho * peso * rota
print('O preço total da entrega será de R${:.2f}! (tamanho:{} * peso:{} * rota:{})'.format(total,tamanho,peso,rota))
print('Obrigado pela preferência!')