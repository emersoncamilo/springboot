import os

restaurantes = [{'nome':'Praca', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizzaria', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'italizano', 'ativo':True}
                ]

def exibir_nome_do_programa():
    print ("""
Ｓａｂｏｒ Ｅｘｐｒｅｓｓ
""")

def finalizar_app():
    exibir_subtitulo ('Finalizando APP')


def exibir_opcoes():
    print ('1. Cadastrar restaurante')
    print ('2. Listar Restaurante')
    print ('3. Alternar estado do Restaurante')
    print ('4. Sair')

def opcao_invalida():
    print('Opcao Invalida! \n')
    voltar_menu_principal()


def cadastrar_novo_restaurante():
    '''
    Essa funcao e responsavel por cadastrar novo restaurante.

    Inputs:
    - Nome do restaurante (str)
    - Categoria (str)

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
   
    '''

    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do Restaurante que deseja cadastrar: ')
    categoria = input('Digite o nome da categoria do Restaurante: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)


    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu_principal()



def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do Restaurante'.ljust(22)}| {'Categoria'.ljust(20)}| {'Status'.ljust(20)}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)}| {categoria.ljust(20)}| {ativo.ljust(10)}')

    voltar_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do Restaurante')
    nome_restaurante = input('Deseje o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print ('O restaurante nao foi encontrado')

    voltar_menu_principal()


def voltar_menu_principal():
    input('\nDigite uma tecla para voltar para o menu principal ')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        print(f'voce escolheu a opcao {opcao_escolhida}!')

        if opcao_escolhida == 1:
           cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) +1)
    print(linha)
    print(texto)
    print(linha)
    print()
    # os.system('clear')


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()




def escolher_match():
    opcao_escolhida = int(input('Escolha uma opção: '))
    match opcao_escolhida:
        case 1:
            print('Adicionar restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurante')
        case 4:
            print('Finalizar app')
        case _:
            print('Opção inválida!')


if __name__ == '__main__':
    main()