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

    # age : Annotated[int,Field(ge= 13,le=130)]
    age: int

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

    @field_validator("age")
    @classmethod
    def validate_age(cls,value):
        if value <0 :
            raise ValueError("Age must be positive ...Unless u want to age backwards ")
        

        return value
    

class UserRegistration(BaseModel):
    email : EmailStr
    password : str 
    confirm_password : str 

    @model_validator(mode = "after") ## no use of class method cause we have used validator after 
    def password_match(self)->"UserRegistration":
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        
        return self 
    

try : 
    res = UserRegistration( 
        email="sadhana@gmail.com",
        password="secret123",
        confirm_password = "notasecret"
    )

except ValidationError as e : 
    print(e)


 








