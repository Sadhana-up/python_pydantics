from pydantic import BaseModel,ValidationError, Field,EmailStr,HttpUrl,SecretStr,field_validator, model_validator,ValidationInfo
from datetime import datetime,UTC
from typing import Literal,Annotated
from uuid import UUID,uuid4


#NOW WE R USING DECORATORS AND PYDANTIC :



class User(BaseModel):

    uid : UUID = Field(default_factory=uuid4) 

    username : Annotated[str,Field(min_length=3,max_length=20)] 

    email :EmailStr

   

    password : SecretStr 

    age : Annotated[int,Field(ge= 13,le=130)]

    verified_at : datetime |None = None

    bio : str = "" #

    website: HttpUrl | None = None

    is_active :bool = True 

    full_name :str |None = None   

    slug : Annotated[str,Field(pattern=r"^[a-z0-9]+$")]

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str)->str : ##used type hinting whwere value takes a str and its output is also a str
        if not value.replace("_","").isalnum(): 
            raise ValueError("Username must be alphanumeric(underscores allowed)")
        return value.lower()



class BlogPost(BaseModel):
    title :str 
    content: str 
    view_count:int = 0 
    is_published : bool = False
    tags : list[str] = Field(default_factory =list ) 
    created_at : datetime = Field(default_factory=lambda:datetime.now(tz = UTC))
    author_id : int | str
    status : Literal["Draft","Published","archived "] = "Draft"

    
##USAGE     

user1 = User(
    username="bunty",
    email="what@gmail.com",
    age= 21, 
    password="wowowo111",
    slug="hello221"
)
print(user1.password.get_secret_value())
print(user1)






