#----------- variávies globais ------------
lista_produto = []
codigo_produto = 0

#-----------------------------------------

#-----------cadastrar produtos------------
def cadastra_produto(codigo):
    print('Bem vindo ao menu Cadastrar Produtos.')
    print('Código do produto: {}'.format(codigo))
    nome = input('Entre com o NOME da peça: ')
    fabricante = input('Entre com o FABRICANTE da peça: ')
    preco = int(input('Entre com o PREÇO(R$) da peça: '))
    dicionario_produto = {'codigo':    codigo,
                          'nome':       nome,
                          'fabricante': fabricante,
                          'preco':      preco}
    lista_produto.append(dicionario_produto.copy())
#-----------------------------------------

#-----------consultar produtos------------
def consultar_produto():
    print('Bem vindo ao menu Consultar Produtos.')
    while True:
        opcao_consultar = input('\n Escolha a opção desejada: \n' +
                            '1 - Consultar todos os Produto\n' +
                            '2 - Consultar Produto por Código \n' +
                            '3 - Consultar Produto por Fabricante \n' +
                            '4 - Retornar \n'
                            + '>>')
        if opcao_consultar == '1':
            print('Você escolheu a opção Consultar todos os Produtos')
            for produto in lista_produto: #produto vai varrer toda lista de produto
                print('--------------------------------')
                for key,value in produto.items():
                    print('{} : {}'.format(key,value))
                print('--------------------------------')
        elif opcao_consultar == '2':
            print('Você escolheu a opção Consultar Produto por Código')
            codigo_desejado = int(input('Entre com o Codigo desejado:\n'
                                    + '>>'))
            for produto in lista_produto:
                if produto['codigo'] == codigo_desejado:
                    print('--------------------------------')
                    for key, value in produto.items():
                        print('{} : {}'.format(key, value))
                    print('--------------------------------')
        elif opcao_consultar == '3':
            print('Você escolheu a opção Produto por Fabricante')
            codigo_desejado = input('Entre com o Fabricante desejado:\n'
                                    + '>>')
            for produto in lista_produto:
                if produto['fabricante'] == codigo_desejado:
                    print('--------------------------------')
                    for key, value in produto.items():
                        print('{} : {}'.format(key, value))
                    print('--------------------------------')
        elif opcao_consultar == '4':
            return #sai da função consultar_produto e volta para o main.
        else:
            print('Opção Inválida. Tente Novamente!')

#-----------------------------------------

#-----------Remover produtos------------
def remover_produto():
    print('Bem vindo ao menu Remover Produtos.')
    codigo_desejado = int(input('Entre com o Codigo do Produto que deseja remover:\n'+
                            '>>'))
    for produto in lista_produto:
        if produto['codigo'] == codigo_desejado:
            lista_produto.remove(produto)
            print('Produto removido com sucesso!')

#-----------------------------------------

#-----------Main------------
print('Bem vindo ao Controle de Estoque da Bicicletária do Paulo Cesar Maximiano Ferdin')
while True:
    opcao_menu1 = input('\n Escolha a opção desejada: \n' +
                        '1 - Cadastrar Produto\n' +
                        '2 - Consultar Produto(s) \n' +
                        '3 - Remover Produto \n' +
                        '4 - Sair \n'
                        +'>>')
    if opcao_menu1 == '1':
        codigo_produto = codigo_produto + 1
        cadastra_produto(codigo_produto)
    elif opcao_menu1 =='2':
        consultar_produto()
    elif opcao_menu1 =='3':
        remover_produto()
    elif opcao_menu1 =='4':
        break #encerrerá o laço, ja que é a opção sair!
    else:
        print('Opção Inválida. Tente Novamente!')
        continue #voltará para o inicio do laço!
#-----------------------------------------