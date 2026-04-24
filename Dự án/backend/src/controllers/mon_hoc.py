from fastapi import APIRouter, Depends
from src.core.dependencies import get_mon_hoc_service
from src.services.mon_hoc import MonHocService
from src.schema.mon_hoc import MonHocCreate, MonHocUpdate, MonHocResponse

router = APIRouter(prefix="/api/mon-hoc", tags=["Môn Học"])


@router.get("/", response_model=list[MonHocResponse])
def get_all(service: MonHocService = Depends(get_mon_hoc_service)):
    return service.get_all()


@router.get("/{ma_mon}", response_model=MonHocResponse)
def get_by_id(ma_mon: str, service: MonHocService = Depends(get_mon_hoc_service)):
    return service.get_by_id(ma_mon)


@router.post("/", response_model=MonHocResponse, status_code=201)
def create(data: MonHocCreate, service: MonHocService = Depends(get_mon_hoc_service)):
    return service.create(data)


@router.put("/{ma_mon}", response_model=MonHocResponse)
def update(ma_mon: str, data: MonHocUpdate, service: MonHocService = Depends(get_mon_hoc_service)):
    return service.update(ma_mon, data)


@router.delete("/{ma_mon}")
def delete(ma_mon: str, service: MonHocService = Depends(get_mon_hoc_service)):
    return service.delete(ma_mon)
