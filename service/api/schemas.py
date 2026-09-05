from posixpath import dirname
from uuid import UUID

from django.utils.timezone import activate
from ninja import Schema

from service.application.dtos import ServiceInDTO, ServiceOutDTO, ServiceUpdateDTO

class ServiceIn(Schema):
    name: str
    description: str
    duration: int
    value: int

    def to_dto(self):
        return ServiceInDTO(
            name=self.name,
            description=self.description,
            duration=self.duration,
            value=self.value
        )

class ServiceOut(Schema):
    id: UUID
    name: str
    description: str
    duration: int
    value: int
    activate: bool

    @classmethod
    def from_domain(cls, dto: ServiceOutDTO):
        return cls(
            id=dto.id,
            name=dto.name,
            description=dto.description,
            duration=dto.duration,
            value=dto.value,
            activate=dto.activate
        )

class ServiceUpdate(Schema):
    name: str | None = None
    description: str | None = None
    duration: int | None = None
    value: int | None = None
    activate: bool | None = None

    def to_dto(self) -> ServiceUpdateDTO:
        return ServiceUpdateDTO(
            name = self.name,
            description = self.description,
            duration= self.duration,
            value = self.value,
            activate = self.activate
        )