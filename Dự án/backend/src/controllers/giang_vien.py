from fastapi import APIRouter, Depends
from src.core.dependencies import get_giang_vien_service
from src.services.giang_vien import GiangVienService
from src.schema.giang_vien import GiangVienCreate, GiangVienUpdate, GiangVienResponse

router = APIRouter(prefix="/api/giang-vien", tags=["Giảng Viên"])


@router.get("/", response_model=list[GiangVienResponse])
def get_all(service: GiangVienService = Depends(get_giang_vien_service)):
    return service.get_all()


@router.get("/{ma_gv}", response_model=GiangVienResponse)
def get_by_id(ma_gv: str, service: GiangVienService = Depends(get_giang_vien_service)):
    return service.get_by_id(ma_gv)


@router.post("/", response_model=GiangVienResponse, status_code=201)
def create(data: GiangVienCreate, service: GiangVienService = Depends(get_giang_vien_service)):
    return service.create(data)


@router.put("/{ma_gv}", response_model=GiangVienResponse)
def update(ma_gv: str, data: GiangVienUpdate, service: GiangVienService = Depends(get_giang_vien_service)):
    return service.update(ma_gv, data)


@router.delete("/{ma_gv}")
def delete(ma_gv: str, service: GiangVienService = Depends(get_giang_vien_service)):
    return service.delete(ma_gv)
