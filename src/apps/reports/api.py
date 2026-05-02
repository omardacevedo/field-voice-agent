import uuid
from ninja import Router, Query
from ninja.pagination import paginate, PageNumberPagination
from ninja_jwt.authentication import JWTAuth
from django.shortcuts import get_object_or_404

from .models import ServiceReport
from .schemas import (
    ServiceReportIn,
    ServiceReportOut,
    ServiceReportDetail,
    ServiceReportPatch,
    ReportFilters,
)
from apps.agents.schemas import AgentSessionOut

router = Router()


@router.get("/", auth=JWTAuth(), response=list[ServiceReportOut])
@paginate(PageNumberPagination, page_size=20)
def list_reports(request, filters: ReportFilters = Query(...)):
    return filters.filter(
        ServiceReport.objects.select_related("technician").filter(
            technician=request.auth
        )
    )


@router.post("/", auth=JWTAuth(), response={201: ServiceReportOut})
def create_report(request, payload: ServiceReportIn):
    report = ServiceReport.objects.create(
        technician=request.auth,
        **payload.model_dump(),
    )
    return 201, ServiceReport.objects.select_related("technician").get(id=report.id)


@router.get("/{report_id}", auth=JWTAuth(), response=ServiceReportDetail)
def get_report(request, report_id: uuid.UUID):
    return get_object_or_404(
        ServiceReport.objects.select_related("technician"),
        id=report_id,
        technician=request.auth,
    )


@router.patch("/{report_id}", auth=JWTAuth(), response=ServiceReportDetail)
def patch_report(request, report_id: uuid.UUID, payload: ServiceReportPatch):
    report = get_object_or_404(
        ServiceReport, id=report_id, technician=request.auth
    )
    for attr, value in payload.model_dump(exclude_unset=True).items():
        setattr(report, attr, value)
    report.save()
    return ServiceReport.objects.select_related("technician").get(id=report.id)


@router.get("/{report_id}/sessions", auth=JWTAuth(), response=list[AgentSessionOut])
def list_report_sessions(request, report_id: uuid.UUID):
    report = get_object_or_404(ServiceReport, id=report_id, technician=request.auth)
    return list(report.sessions.all())
