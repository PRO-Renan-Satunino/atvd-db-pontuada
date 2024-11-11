from config.connection import Session
from repositories.usuario_repositories import UsuarioRepository
from services.usuario_services import UsuarioService

def main():
    db = Session()
    usuario_repository = UsuarioRepository(db)
    usuario_service = UsuarioService(usuario_repository)

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
            usuario_service.criar_usuario(nome, email, idade)

        elif opcao == '2':
            usuario_id = int(input("Informe o ID do usuário: "))
            usuario_service.pesquisar_usuario(usuario_id)

        elif opcao == '3':
            usuario_id = int(input("Informe o ID do usuário a ser atualizado: "))
            nome = input("Novo nome (deixe vazio para não alterar): ")
            email = input("Novo email (deixe vazio para não alterar): ")
            idade = input("Nova idade (deixe vazio para não alterar): ")
            idade = int(idade) if idade else None
            usuario_service.atualizar_usuario(usuario_id, nome, email, idade)

        elif opcao == '4':
            usuario_id = int(input("Informe o ID do usuário a ser excluído: "))
            usuario_service.excluir_usuario(usuario_id)

        elif opcao == '5':
            usuario_service.listar_todos_usuarios()

        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
