import uuid
from datetime import datetime
from typing import Optional
from ninja import Schema, FilterSchema

from apps.users.schemas import TechnicianOut


class CoordinatesSchema(Schema):
    lat: float
    lng: float


class LocationSchema(Schema):
    address: str = ""
    city: str = ""
    site_code: Optional[str] = None
    coordinates: Optional[CoordinatesSchema] = None


class MaterialSchema(Schema):
    name: str
    quantity: float
    unit: str
    unit_cost: Optional[float] = None


class ServiceReportIn(Schema):
    work_order: str
    client_name: str
    intervention_type: str
    location: LocationSchema
    description: str = ""
    materials_used: list[MaterialSchema] = []
    observations: str = ""


class ServiceReportPatch(Schema):
    status: Optional[str] = None
    client_name: Optional[str] = None
    location: Optional[LocationSchema] = None
    description: Optional[str] = None
    materials_used: Optional[list[MaterialSchema]] = None
    observations: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class ServiceReportOut(Schema):
    id: uuid.UUID
    work_order: str
    client_name: str
    status: str
    intervention_type: str
    technician: TechnicianOut
    session_count: int
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def resolve_session_count(obj) -> int:
        return obj.sessions.count()


class ServiceReportDetail(ServiceReportOut):
    location: LocationSchema
    description: str
    materials_used: list[MaterialSchema]
    observations: str
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class ReportFilters(FilterSchema):
    status: Optional[str] = None
    intervention_type: Optional[str] = None
