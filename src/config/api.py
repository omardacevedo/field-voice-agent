from ninja import NinjaAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from apps.users.api import router as users_router
from apps.reports.api import router as reports_router
from apps.agents.api import router as agents_router

api = NinjaAPI(
    title="FieldVoice API",
    version="1.0.0",
    description="API para el agente de voz conversacional de campo.",
    urls_namespace="api",
)

api.register_controllers(NinjaJWTDefaultController)

api.add_router("/technicians", users_router, tags=["Technicians"])
api.add_router("/reports", reports_router, tags=["Reports"])
api.add_router("/sessions", agents_router, tags=["Agent Sessions"])
