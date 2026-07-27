import bcrypt

class HashPasswordService:
    def encode_password(self, senha: str, senha_hash:str ) -> bool:
        senha_bytes = senha.encode('utf-8')

        if bcrypt.checkpw(senha_bytes, senha_hash):
            return True
        else:
            return False

    def hash_password(self, senha: str) -> str:
        senha_bytes = senha.encode('utf-8')

        salt = bcrypt.gensalt()

        senha_hash = bcrypt.hashpw(senha_bytes, salt)

        return senha_hash