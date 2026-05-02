import uuid
from ninja import Schema


class TechnicianOut(Schema):
    id: uuid.UUID
    email: str
    employee_id: str
    specialty: str
    first_name: str
    last_name: str
    phone: str
