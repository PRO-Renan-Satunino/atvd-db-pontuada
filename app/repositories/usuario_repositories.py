from sqlalchemy.orm import Session
from models.usuario import Usuario

class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session

    # Salvar usuário
    def salvar_usuario(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()

    # Buscar usuário por email
    def pesquisar_usuario_por_email(self, email: str):
        return self.session.query(Usuario).filter_by(email=email).first()
    
     # Buscar usuário por nome
    def pesquisar_usuario_por_nome(self, nome: str):
        return self.session.query(Usuario).filter(Usuario.nome.ilike(f"%{nome}%")).all()

    # Deletar usuário
    def deletar_usuario(self, usuario_id: int):
        usuario = self.session.query(Usuario).filter_by(id=usuario_id).first()
        if usuario:
            self.session.delete(usuario)
            self.session.commit()
        return usuario

    # Listar todos os usuários
    def listar_usuarios(self):
        return self.session.query(Usuario).all()

    # Buscar usuário por id
    def pesquisar_usuario_por_id(self, usuario_id: int):
        return self.session.query(Usuario).filter_by(id=usuario_id).first()

    # Atualizar dados do usuário
    def atualizar_usuario(self, usuario_id: int, nome: str = None, email: str = None, idade: int = None):
        usuario = self.session.query(Usuario).filter_by(id=usuario_id).first()
        if usuario:
            if nome: usuario.nome = nome
            if email: usuario.email = email
            if idade: usuario.idade = idade
            self.session.commit()
        return usuario
