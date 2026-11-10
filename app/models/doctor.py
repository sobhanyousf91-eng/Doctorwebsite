from sqlmodel import SQLModel,Field
class Doctors(SQLModel,tabals=True):
    id:int|None=Field(primary_key=True,index=True)
    name:str=Field(min_length=1,max_length=150)
    tozihat:str=Field(max_length=150)
    phone_number:str=Field(min_length=11,max_length=11)
    addres:str=Field(max_length=150)
