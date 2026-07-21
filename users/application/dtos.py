from pydantic import BaseModel

class UserInDTO(BaseModel):
    email: str
    password: str

class UserOutDTO(BaseModel):
    id: int
    name: str
    email: str

    @classmethod
    def from_domain(cls, model):
        id = model.id
        name = model.name
        email = model.email

class UserResponseDTO(BaseModel):
    user: UserOutDTO
    acess_token: str

class UserUpdateDTO(BaseModel):
    id: int | None = None
    name: str | None = None
    email: str | None = None
    password: str | None = None