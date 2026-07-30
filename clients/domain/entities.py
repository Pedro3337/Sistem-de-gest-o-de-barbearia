from dataclasses import dataclass,field
from datetime import datetime
from uuid import UUID, uuid4

@dataclass
class ClientEntity:
    id: UUID = field(default_factory=uuid4)
    user_id: UUID | None = field(default=None)
    date_register: datetime = field(default=datetime)
 