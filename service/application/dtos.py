from uuid import UUID

from ninja import Schema

from service.domain.entities import ServiceEntity

class ServiceInDTO(Schema):
    name: str
    description: str
    duration: int
    value: int

class ServiceOutDTO(Schema):
    id: UUID
    name: str
    description: str
    duration: int
    value: int
    activate: bool

    @classmethod
    def from_domain(cls, entity: ServiceEntity):

        print("ID:", entity.id)
        print("NAME:", entity.name)
        print("DESCRIPTION:", entity.description, type(entity.description))
        print("ACTIVATE:", entity.activate, type(entity.activate))

        return cls(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            duration=entity.duration,
            value=entity.value,
            activate=entity.activate
        )

class ServiceUpdateDTO(Schema):
    name: str | None = None
    description: str | None = None
    duration: int | None = None
    value: int | None = None
    activate: bool | None = None