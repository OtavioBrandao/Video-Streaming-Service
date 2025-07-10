import os
import sys
import time


def inicializar():
    print("==========================")
    print("VIDEO STREAMING SERVICE")
    print("==========================")

def limpar_tela():
    # Limpa a tela do terminal
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def menu_inicial():
    print("Bem-vindo ao Video Streaming Service!\n")
    print("Deseja criar uma conta ou fazer login?\n")
    print("===========================")
    print("1. Criar conta\n")
    print("2. Fazer login\n")
    print("3. Continuar como convidado\n")
    print("4. Sair")
    print("===========================")

    opcao = input("Escolha uma opção (1-4):\n ")
    if opcao == "1":
        limpar_tela()
        #criar_conta()
        print("Função de criação de conta ainda não implementada.\n")
        menu_principal()
    elif opcao == "2":
        limpar_tela()
        #fazer_login()
        print("Função de login ainda não implementada.\n")
        menu_principal()
    elif opcao == "3":
        limpar_tela()
        menu_principal_convidado()
    elif opcao == "4":
        print("Saindo do Video Streaming Service. Até logo!\n")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        menu_inicial()

def menu_config_usuario():
    while True:
        print("Configurações de usuário:\n")
        print("===========================")
        print("1. Gerenciar meus perfis")
        print("2. Gerenciar meu plano de assinatura")
        print("3. Configurações de controle parental")
        print("4. Voltar ao menu principal")
        print("===========================")

        opcao_usuario = input("Escolha uma opção (1-4):\n ")
        if opcao_usuario == "1":
            print("Não implementado\n")
            time.sleep(2)
            limpar_tela()
        elif opcao_usuario == "2":
            print("Não implementado\n")
            time.sleep(2)
            limpar_tela()
        elif opcao_usuario == "3":
            print("Não implementado\n")
            time.sleep(2)
            limpar_tela()
        elif opcao_usuario == "4":
            limpar_tela()
            break
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            limpar_tela()



def menu_principal_convidado():
    print("Bem-vindo, convidado!\n"
          "Você pode explorar o conteúdo, porém o resto das funcionalidades estão limitadas. Crie uma conta para ter acesso completo aos nossos serviços.\n"
          "O que você gostaria de fazer?\n"
          )
    print("===========================")
    print("1. Consultar biblioteca de conteúdo\n")
    print("2. Configurações de usuário\n")
    print("3. Recomendações personalizadas\n")
    print("4. Streaming em múltiplos dispositivos\n")
    print("5. Otimização de banda larga\n")
    print("6. Marcar conteúdo e histórico de visualização\n")
    print("7. Revisões e avaliações de conteúdo\n")
    print("8. Integração com anúncios\n")
    print("9. Voltar ao menu inicial")
    print("===========================")

    opcao = input("Escolha uma opção (1-9):\n ")
    if opcao == "1":
        limpar_tela()
        print("Consultando biblioteca de conteúdo...\n")
        time.sleep(2)
        limpar_tela()
        menu_principal_convidado()
        #implementar funcao consultar_biblioteca()
    elif opcao == "2":
        limpar_tela()
        print("Configurações de usuário não disponíveis para convidados.\n")
        time.sleep(2)
        limpar_tela()
        menu_principal_convidado()
    elif opcao == "3":
        limpar_tela()
        print("Recomendações personalizadas não disponíveis para convidados.\n")
        time.sleep(2)
        limpar_tela()
        menu_principal_convidado()
    elif opcao == "4":
        limpar_tela()
        print("Streaming em múltiplos dispositivos não disponível para convidados.\n")
        time.sleep(2)
        limpar_tela()
        menu_principal_convidado()
    elif opcao == "5":
        limpar_tela()
        print("Otimização de banda larga não disponível para convidados.\n")
        time.sleep(2)
        limpar_tela()
        menu_principal_convidado()
    elif opcao == "6":
        limpar_tela()
        print("Marcar conteúdo e histórico de visualização não disponível para convidados.\n")
        time.sleep(2)
        limpar_tela()
        menu_principal_convidado()
    elif opcao == "7":
        limpar_tela()
        print("Revisões e avaliações de conteúdo não disponíveis para convidados.\n")
        time.sleep(2)
        limpar_tela()
        menu_principal_convidado()
    elif opcao == "8":
        limpar_tela()
        print("Integração com anúncios não disponível para convidados.\n")
        time.sleep(2)
        limpar_tela()
        menu_principal_convidado()
    elif opcao == "9":
        limpar_tela()
        menu_inicial()
    else:
        print("Opção inválida. Tente novamente.")
        time.sleep(2)
        limpar_tela()
        menu_principal_convidado()


def menu_principal():
    print("Bem-vindo ao Video Streaming Service, Usuário!\n"
          "O que você gostaria de fazer?\n"
          )
    print("===========================")
    print("1. Consultar biblioteca de conteúdo\n")
    print("2. Configurações de usuário\n")
    print("3. Recomendações personalizadas\n")
    print("4. Streaming em múltiplos dispositivos\n")
    print("5. Otimização de banda larga\n")
    print("6. Marcar conteúdo e histórico de visualização\n")
    print("7. Revisões e avaliações de conteúdo\n")
    print("8. Integração com anúncios\n")
    print("9. Logout")
    print("===========================") 

    opcao = input("Escolha uma opção (1-9):\n ")

    if opcao == "1":
        limpar_tela()
        print("Consultando biblioteca de conteúdo...\n")
        time.sleep(2)
        limpar_tela()
        #implementar funcao consultar_biblioteca()
    elif opcao == "2":
        limpar_tela()
        menu_config_usuario()
        menu_principal()

    elif opcao == "3":
        #implementar funcao recomendacoes_personalizadas()
        print("Não implementado\n")
        time.sleep(2)
        limpar_tela()
        menu_principal()
    elif opcao == "4":
        #implementar funcao streaming_multiplos_dispositivos()
        print("Não implementado\n")
        time.sleep(2)
        limpar_tela()
        menu_principal()
    elif opcao == "5":
        #implementar funcao otimizacao_banda_larga()
        print("Não implementado\n")
        time.sleep(2)
        limpar_tela()
        menu_principal()
    elif opcao == "6":
        #implementar funcao marcar_conteudo()
        print("Não implementado\n")
        time.sleep(2)
        limpar_tela()
        menu_principal()
    elif opcao == "7":
        #implementar funcao revisoes_avaliacoes()
        print("Não implementado\n")
        time.sleep(2)
        limpar_tela()
        menu_principal()
    elif opcao == "8":
        
        #implementar funcao integracao_anuncios()
        print("Não implementado\n")
        time.sleep(2)
        limpar_tela()
        menu_principal()
    elif opcao == "9":
        limpar_tela()
        print("Você escolheu sair.\n")
        print("Tem certeza de que deseja sair?\n"
              "1. Sim\n"
              "2. Não\n")
        opcao_logout = input("")
        if opcao_logout == "1":
            print("Desconectando...\n")
            time.sleep(2)
            limpar_tela()
            menu_inicial()
        elif opcao_logout == "2":
            print("Retornando ao menu principal...\n")
            time.sleep(2)
            limpar_tela()
            menu_principal()
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            limpar_tela()
            menu_principal()

if __name__ == "__main__":
    inicializar()
    menu_inicial()
