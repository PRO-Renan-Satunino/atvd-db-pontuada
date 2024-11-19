from config.connection import Session
from repositories.usuario_repositories import UsuarioRepository
from services.usuario_services import UsuarioService
import os

def main():
    db = Session()
    usuario_repository = UsuarioRepository(db)
    usuario_services = UsuarioService(usuario_repository)

    while True:
        print("\n=== SENAI SOLUTION ===")
        print("1 - Adicionar usuário")
        print("2 - Pesquisar um usuário")
        print("3 - Atualizar dados de um usuário")
        print("4 - Excluir um usuário")
        print("5 - Exibir todos os usuários cadastrados")
        print("0 - Sair")
        
        opcao = input("Informe a opção desejada: ")

        if opcao == '1':
            nome = input("Nome do usuário: ")
            email = input("Email do usuário: ")
            idade = int(input("Idade do usuário: "))
            usuario_services.criar_usuario(nome, email, idade)
            os.system("clear || cls")

        elif opcao == '2':
            os.system("clear || cls")
            print("Como você deseja pesquisar o usuário?")
            print("1 - Por ID")
            print("2 - Por Nome")
            print("3 - Por Email")
            pesquisa_opcao = input("Informe a opção desejada: ")

            if pesquisa_opcao == '1':
                usuario_id = int(input("Informe o ID do usuário: "))
                usuario_services.pesquisar_usuario_por_id(usuario_id)
            elif pesquisa_opcao == '2':
                nome = input("Informe o nome do usuário: ")
                usuario_services.pesquisar_usuario_por_nome(nome)
            elif pesquisa_opcao == '3':
                email = input("Informe o email do usuário: ")
                usuario_services.pesquisar_usuario_por_email(email)
            else:
                print("Opção inválida!")
            

        elif opcao == '3':
            usuario_id = int(input("Informe o ID do usuário a ser atualizado: "))
            nome = input("Novo nome (deixe vazio para não alterar): ")
            email = input("Novo email (deixe vazio para não alterar): ")
            idade = input("Nova idade (deixe vazio para não alterar): ")
            idade = int(idade) if idade else None
            usuario_services.atualizar_usuario(usuario_id, nome, email, idade)
            os.system("clear || cls")

        elif opcao == '4':
            usuario_id = int(input("Informe o ID do usuário a ser excluído: "))
            usuario_services.excluir_usuario(usuario_id)
            os.system("clear || cls")

        elif opcao == '5':
            os.system("clear || cls")
            usuario_services.listar_todos_usuarios()

        elif opcao == '0':
            os.system("clear || cls")
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
