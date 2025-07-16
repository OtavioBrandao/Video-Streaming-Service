# Parental Control Settings: Implementing parental controls for content filtering;
from user_management import User

def activate_parental_control(usuario):
    while True:
        lista_perfis = usuario.listar_perfis()
        print("Digite o nome do perfil para ativar o controle parental:")
        nome_perfil = input("Nome do perfil: ")

        if nome_perfil in usuario.perfis:
            usuario.ativar_controle_parental(nome_perfil)
            print(f"Controle parental ativado para o perfil: {nome_perfil}\n")
            break

def restringir_conteudo(usuario):
    pass
