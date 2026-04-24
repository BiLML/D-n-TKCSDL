from fastapi import APIRouter, Depends
from src.core.dependencies import get_dashboard_service
from src.services.dashboard import DashboardService
from src.schema.dashboard import DashboardStats

router = APIRouter(prefix="/api/dashboard", tags=["Dashboard"])


@router.get("/stats", response_model=DashboardStats)
def get_stats(service: DashboardService = Depends(get_dashboard_service)):
    return service.get_stats()
