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
        return cls(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            duration=entity.duration,
            value=entity.value,
            entity=entity.activate
        )

class ServiceUpdateDTO(Schema):
    name: str | None = None
    description: str | None = None
    duration: int | None = None
    value: int | None = None
    activate: bool | None = None