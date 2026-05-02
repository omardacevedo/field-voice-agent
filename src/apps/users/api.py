from ninja import Router
from ninja_jwt.authentication import JWTAuth

from .schemas import TechnicianOut

router = Router()


@router.get("/me", auth=JWTAuth(), response=TechnicianOut)
def get_me(request):
    return request.auth
