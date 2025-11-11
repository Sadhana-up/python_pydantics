from pydantic import BaseModel,ValidationError, Field,EmailStr,HttpUrl,SecretStr
from datetime import datetime,UTC
from typing import Literal,Annotated
from uuid import UUID,uuid4


##we define a class which inherits from base model

class User(BaseModel):
    # uid :Annotated[int,Field(gt=0)] ##want an integer which is greater than 0 
    uid : UUID = Field(default_factory=uuid4) #generate unique uid for users 
    username : Annotated[str,Field(min_length=3,max_length=20)] ##max username is 20 length 

    email :EmailStr

    website : HttpUrl | None = None 

    password : SecretStr 

    age : Annotated[int,Field(ge= 13,le=130)]

    verified_at : datetime |None = None

    bio : str = "" ##Optional Fields

    website: HttpUrl | None = None

    is_active :bool = True # optioanl field cause we have passed the value 

    full_name :str |None = None  #full name is either string or none 
    #using union 

    slug : Annotated[str,Field(pattern=r"^[a-z0-9]+$")]



class BlogPost(BaseModel):
    title :str 
    content: str 
    view_count:int = 0 
    is_published : bool = False


    tags : list[str] = Field(default_factory =list ) 
#default factory is a function which gets callwd everytime we create an instance 
#for each user fresh new list is created 
    # created_at : datetime = datetime.now(UTC) # is called once when a class is created and not an instance
    created_at : datetime = Field(default_factory=lambda:datetime.now(tz = UTC))

    author_id : int | str

    status : Literal["Draft","Published","archived "] = "Draft"
    


user1 = User(
    username="bunty ",
    email="what@gmail.com",
    age= 21, 
    password="wowowo111",
    slug="hello221"
)
print(user1.password.get_secret_value())
print(user1)





