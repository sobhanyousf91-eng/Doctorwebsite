from fastapi import FastAPI,Body,status,Path ,HTTPException
from typing import Annotated
from app.schima.doctor import Doctros,Doctor_update
from app.models.doctor import Doctors as DoctorDB
from app.dependecis import SessionDep
from sqlmodel import select
app=FastAPI()
@app.post("/creat/",status_code=status.HTTP_201_CREATED)
async def doctors(
    doctors_info:Annotated[Doctros,Body()],
    session:SessionDep
):
    doctos_for_db=DoctorDB(
        name=doctors_info.name ,
        tozaihat=doctors_info.tozihat,
        phone_number=doctors_info.phone_number,
        addres=doctors_info.addres
    )
    session.add(doctos_for_db)
    session.commit()
    return doctos_for_db
@app.get("/doctors/")
async def hameh_doctors(

        session:SessionDep
):
    return session.exec(select(DoctorDB)).all()
@app.get("/doctor/{id:int}")
async def  get_doctor_by_id (
    id:Annotated[int,Path()],
    session:SessionDep
):
    doctor_from_db=session.exec(select(DoctorDB).where(DoctorDB.id==id)).first()    
    if not doctor_from_db:
        raise HTTPException(status.HTTP_404_FOUND,detail="کاربر پیدا نشد")
    return doctor_from_db
@app.delete("/docros/{id:int}/delet",status_code=status.HTTP_204_NO_CONTENT)
async def delet_doctor(
    id:Annotated[int,Path()],
    session:SessionDep
)->None:
    doctor_from_db=session.exec(select(DoctorDB).where(DoctorDB.id==id)).first()
    if not doctor_from_db:
        raise HTTPException(status.HTTPE_404_FOUND,detail="کاربر پیدا نشد")
@app.patch("/docros/{id:int}/update")
async def update_doctor(
    id:Annotated[int,Path()],
    session:SessionDep,
    new_info:Annotated[Doctor_update,Body()]
):
    doctor_from_db=session.exec(select(DoctorDB).where(DoctorDB.id==id)).first()
    if not doctor_from_db:
        raise HTTPException(status.HTTPE_404_FOUND,detail="کاربر اپدیت نشد")
    doctor_from_db.sqlmodel_update(new_info.model_dump(exclude_unset=True))
    session.commit()
    session.refresh(doctor_from_db)
    return doctor_from_db




