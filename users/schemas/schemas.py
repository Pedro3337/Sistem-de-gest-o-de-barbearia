from ninja import Schema
from ..application.dtos import UserInDTO,UserOutDTO,UserUpdateDTO

class UserIn(Schema):
    email: str
    passowrd: str

    def to_dto(self) -> UserInDTO:
        return UserInDTO(
            email=self.email,
            password=self.passowrd
        )

class UserOut(Schema):
    id: int
    name: str
    email: str
    password: str
    acess_token: str
    refresh_token: str

    @classmethod
    def from_domain(self, dto: UserOutDTO) -> UserOutDTO:
        id = dto.id
        name = dto.name
        email = dto.email
        password = dto.password
        acess_token = dto.acess_token
        refresh_token = dto.refresh_token

class UserUpdate(Schema):
    id: int | None = None
    name: str | None = None
    email: str | None = None
    password: str | None = None

    def to_dto(self) -> UserUpdateDTO:
        return UserUpdateDTO(
            id=self.id,
            name=self.name,
            email=self.email,
            password=self.password
        )