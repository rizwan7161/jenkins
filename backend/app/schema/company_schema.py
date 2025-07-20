from pydantic import BaseModel

class CompanyBase(BaseModel):
    name: str

class CompanyGet(BaseModel):
    id: int

class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int

    class Config:
        orm_mode: True