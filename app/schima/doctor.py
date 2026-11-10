from pydantic import BaseModel,Field
class Doctros(BaseModel):

    name:str=Field(min_length=1,max_length=150)
    tozihat:str=Field(max_length=150)
    phone_number:str=Field(min_length=11,max_length=11)
    addres:str=Field(max_length=150)
class Doctor_update(BaseModel):
    name:str=Field(min_length=1,max_length=150)
    tozihat:str=Field(max_length=150)
    phone_number:str=Field(min_length=11,max_length=11)
    addres:str=Field(max_length=150)