from pydantic import BaseModel,ValidationError, Field,EmailStr,HttpUrl,SecretStr,field_validator, model_validator,ValidationInfo,computed_field
from datetime import datetime,UTC
from typing import Literal,Annotated
from uuid import UUID,uuid4



class User(BaseModel):

    uid : UUID = Field(default_factory=uuid4) 

    username : Annotated[str,Field(min_length=3,max_length=20)] 

    email :EmailStr


    password : SecretStr 

    age: int

    verified_at : datetime |None = None

    bio : str = "" #

    website: HttpUrl | None = None

    is_active :bool = True 

    full_name :str |None = None   

    first_name : str =""
    last_name : str =""
    follower_count : int = 0

    

    # slug : Annotated[str,Field(pattern=r"^[a-z0-9]+$")]

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
    
    @field_validator("website",mode="before")
    @classmethod
    def add_https(cls,v :str)->str | None:
        if v and not v.startswith(("http://","https://")):
            return f"https://{v}"
        return v 
    
    @computed_field
    @property
    def is_inf(self)->bool:
        return self.follower_count>0
    

    @computed_field
    @property
    def name(self)->str:
        return f"{self.username}"
    
    




#Nested models 
class Comment(BaseModel):
    content : str 
    author_email : EmailStr
    likes : int = 0 

class BlogPost(BaseModel): ##contains user as the author and the lsit od comments 
    title :str 
    content: str 
    author :User
    view_count:int = 0 
    is_published : bool = False
    tags : list[str] = Field(default_factory =list ) 
    created_at : datetime = Field(default_factory=lambda:datetime.now(tz = UTC))
    # author_id : int | str
    status : Literal["Draft","Published","archived "] = "Draft"
    comments : list[Comment] = Field(default_factory=list)

#AUTOMATICALLY VALIDATES : 
post_data = {
    "title": "Understanding Pydantic Models",
    "content": "Pydantic makes data validation easy and intuitive...",
    "slug": "understanding-pydantic",
    "author": {
        "username": "coreyms",
        "email": "CoreyMSchafer@gmail.com",
        "age": 39,
        "password": "secret123",
    },
    "comments": [
        {
            "content": "I think I understand nested models now!",
            "author_email": "student@example.com",
            "likes": 25,
        },
        {
            "content": "Can you cover FastAPI next?",
            "author_email": "viewer@example.com",
            "likes": 15,
        },
    ],
}

post = BlogPost(**post_data) # or use BlogPost.model_vaidate(post_data)

print(post.model_dump_json(indent=2))


#user = User( username="sadhana_uprety",email="humpty@gmail.com",age=33,website="sadhana.com",password="secrettt",first_name="sadhana",last_name="uprety")
# # print(user)
# # print(user.model_dump_json(indent=3))


# class UserRegistration(BaseModel):
#     email : EmailStr
#     password : str 
#     confirm_password : str 

#     @model_validator(mode = "after") ## no use of class method cause we have used validator after 
#     def password_match(self)->"UserRegistration":
#         if self.password != self.confirm_password:
#             raise ValueError("Passwords do not match")
        
#         return self 
    

# try : 
#     res = UserRegistration( 
#         email="sadhana@gmail.com",
#         password="secret123",
#         confirm_password = "notasecret"
#     )

# except ValidationError as e : 
#     print(e)


 








