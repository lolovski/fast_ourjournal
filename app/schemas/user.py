import re
from typing import Optional
from pydantic import BaseModel, Field, validator, root_validator


class UserCreate(BaseModel):
    username: str = Field()
    password: str = Field(min_length=8, max_length=100)
    last_name: str = Field()
    first_name: str = Field()
    middle_name: Optional[str] = Field(None)
    class_user: int = Field()

    class Config:
        title = 'Создание пользователя'
        str_min_length = 2
        str_max_length = 32


    @root_validator(skip_on_failure=True)
    def using_latin(cls, values):
        if values.get('middle_name') is None:
            lfm_list = ['last_name', 'first_name']
        else:
            lfm_list = ['last_name', 'first_name', 'middle_name']
        for i in lfm_list:
            if re.search('[а-яё ]', values.get(i), re.IGNORECASE):
                continue
            else:
                raise ValueError('ФИО не может содержать латиницу и цифры')
        return values

class UserRead(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True



