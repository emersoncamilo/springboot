import os



def exibir_nome_do_programa():
    print ("""
Ｓａｂｏｒ Ｅｘｐｒｅｓｓ
""")

def finalizar_app():
    clear_screen()
    print ('Finalizando APP\n')

def exibir_opcoes():
    print ('1. Cadastrar restaurante')
    print ('2. Listar Restaurante')
    print ('3. Ativar Restaurante')
    print ('4. Sair')

def opcao_invalida():
    print('Opcao Invalida! \n')
    input('Digite uma tecla para voltar ao menu principal\n')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        print(f'voce escolheu a opcao {opcao_escolhida}!')

        if opcao_escolhida == 1:
           cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print ('Listar restaurantes')
        elif opcao_escolhida == 3:
            print ('Ativar restaurantes')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


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




def clear_screen():
    os.system('cls')
    # os.system('clear')


def main():
    clear_screen()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()