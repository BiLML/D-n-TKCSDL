from fastapi import APIRouter, Depends
from src.core.dependencies import get_kqht_service
from src.services.kqht import KQHTService
from src.schema.kqht import KQHTCreate, KQHTUpdate, KQHTResponse, KQHTDetailResponse

router = APIRouter(prefix="/api/kqht", tags=["Kết Quả Học Tập"])


@router.get("/", response_model=list[KQHTDetailResponse])
def get_all(service: KQHTService = Depends(get_kqht_service)):
    return service.get_all()


@router.get("/sinh-vien/{ma_sv}", response_model=list[KQHTDetailResponse])
def get_by_sinh_vien(ma_sv: str, service: KQHTService = Depends(get_kqht_service)):
    return service.get_by_sinh_vien(ma_sv)


@router.get("/{ma_sv}/{ma_lop}", response_model=KQHTDetailResponse)
def get_by_id(ma_sv: str, ma_lop: str, service: KQHTService = Depends(get_kqht_service)):
    return service.get_by_id(ma_sv, ma_lop)


@router.post("/", response_model=KQHTResponse, status_code=201)
def create(data: KQHTCreate, service: KQHTService = Depends(get_kqht_service)):
    return service.create(data)


@router.put("/{ma_sv}/{ma_lop}", response_model=KQHTResponse)
def update(ma_sv: str, ma_lop: str, data: KQHTUpdate, service: KQHTService = Depends(get_kqht_service)):
    return service.update(ma_sv, ma_lop, data)


@router.delete("/{ma_sv}/{ma_lop}")
def delete(ma_sv: str, ma_lop: str, service: KQHTService = Depends(get_kqht_service)):
    return service.delete(ma_sv, ma_lop)
