from fastapi import APIRouter, Depends
from src.core.dependencies import get_giang_day_service
from src.services.giang_day import GiangDayService
from src.schema.giang_day import GiangDayCreate, GiangDayResponse, GiangDayDetailResponse

router = APIRouter(prefix="/api/giang-day", tags=["Giảng Dạy"])


@router.get("/", response_model=list[GiangDayDetailResponse])
def get_all(service: GiangDayService = Depends(get_giang_day_service)):
    return service.get_all()


@router.post("/", response_model=GiangDayResponse, status_code=201)
def create(data: GiangDayCreate, service: GiangDayService = Depends(get_giang_day_service)):
    return service.create(data)


@router.delete("/{ma_gv}/{ma_mon}")
def delete(ma_gv: str, ma_mon: str, service: GiangDayService = Depends(get_giang_day_service)):
    return service.delete(ma_gv, ma_mon)
