from fastapi import APIRouter, Depends
from src.core.dependencies import get_sinh_vien_service
from src.services.sinh_vien import SinhVienService
from src.schema.sinh_vien import SinhVienCreate, SinhVienUpdate, SinhVienResponse

router = APIRouter(prefix="/api/sinh-vien", tags=["Sinh Viên"])


@router.get("/", response_model=list[SinhVienResponse])
def get_all(service: SinhVienService = Depends(get_sinh_vien_service)):
    return service.get_all()


@router.get("/{ma_sv}", response_model=SinhVienResponse)
def get_by_id(ma_sv: str, service: SinhVienService = Depends(get_sinh_vien_service)):
    return service.get_by_id(ma_sv)


@router.post("/", response_model=SinhVienResponse, status_code=201)
def create(data: SinhVienCreate, service: SinhVienService = Depends(get_sinh_vien_service)):
    return service.create(data)


@router.put("/{ma_sv}", response_model=SinhVienResponse)
def update(ma_sv: str, data: SinhVienUpdate, service: SinhVienService = Depends(get_sinh_vien_service)):
    return service.update(ma_sv, data)


@router.delete("/{ma_sv}")
def delete(ma_sv: str, service: SinhVienService = Depends(get_sinh_vien_service)):
    return service.delete(ma_sv)
