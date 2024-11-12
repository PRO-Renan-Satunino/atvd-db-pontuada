from repositories.usuario_repositories import UsuarioRepository
from models.usuario import Usuario

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    # Criar usuário
    def criar_usuario(self, nome: str, email: str, idade: int):
        usuario = Usuario(nome=nome, email=email, idade=idade)

        if self.repository.pesquisar_usuario_por_email(email):
            print("Usuário já cadastrado!")
        else:
            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso!")

    # Listar todos os usuários
    def listar_todos_usuarios(self):
        usuarios = self.repository.listar_usuarios()
        if not usuarios:
            print("Nenhum usuário encontrado.")
        else:
            for usuario in usuarios:
                print(usuario.to_dict())

    # Pesquisar um usuário por ID
    def pesquisar_usuario_por_id(self, usuario_id: int):
        usuario = self.repository.pesquisar_usuario_por_id(usuario_id)
        if usuario:
            print(usuario.to_dict())
        else:
            print("Usuário não encontrado.")

    # Pesquisar um usuário por nome
    def pesquisar_usuario_por_nome(self, nome: str):
        usuarios = self.repository.pesquisar_usuario_por_nome(nome)
        if usuarios:
            for usuario in usuarios:
                print(usuario.to_dict())
        else:
            print("Nenhum usuário encontrado com esse nome.")

    # Pesquisar um usuário por email
    def pesquisar_usuario_por_email(self, email: str):
        usuario = self.repository.pesquisar_usuario_por_email(email)
        if usuario:
            print(usuario.to_dict())
        else:
            print("Usuário não encontrado com esse email.")

    # Atualizar dados de um usuário
    def atualizar_usuario(self, usuario_id: int, nome: str = None, email: str = None, idade: int = None):
        usuario = self.repository.atualizar_usuario(usuario_id, nome, email, idade)
        if usuario:
            print("Usuário atualizado com sucesso!")
        else:
            print("Usuário não encontrado.")

    # Excluir um usuário
    def excluir_usuario(self, usuario_id: int):
        usuario = self.repository.deletar_usuario(usuario_id)
        if usuario:
            print(f"Usuário {usuario.nome} excluído com sucesso!")
        else:
            print("Usuário não encontrado.")
