from fastapi import APIRouter, Depends
from src.core.dependencies import get_lop_hp_service
from src.services.lop_hp import LopHPService
from src.schema.lop_hp import LopHPCreate, LopHPUpdate, LopHPResponse, LopHPDetailResponse

router = APIRouter(prefix="/api/lop-hp", tags=["Lớp Học Phần"])


@router.get("/", response_model=list[LopHPDetailResponse])
def get_all(service: LopHPService = Depends(get_lop_hp_service)):
    return service.get_all()


@router.get("/{ma_lop}", response_model=LopHPDetailResponse)
def get_by_id(ma_lop: str, service: LopHPService = Depends(get_lop_hp_service)):
    return service.get_by_id(ma_lop)


@router.post("/", response_model=LopHPResponse, status_code=201)
def create(data: LopHPCreate, service: LopHPService = Depends(get_lop_hp_service)):
    return service.create(data)


@router.put("/{ma_lop}", response_model=LopHPResponse)
def update(ma_lop: str, data: LopHPUpdate, service: LopHPService = Depends(get_lop_hp_service)):
    return service.update(ma_lop, data)


@router.delete("/{ma_lop}")
def delete(ma_lop: str, service: LopHPService = Depends(get_lop_hp_service)):
    return service.delete(ma_lop)
