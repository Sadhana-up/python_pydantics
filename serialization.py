##how to use json and serialize  : 
# imort configdict from pydantics 

# Sometimes your Python variable names and your input data keys don’t match.

# You might get JSON data from an API with camelCase keys.

# But your Python code follows snake_case.

# Pydantic aliases bridge that gap — you can keep your clean Python names while still accepting (or outputting) different field names.



from pydantic import (BaseModel,ValidationError,
                       Field,EmailStr,HttpUrl,SecretStr,
                       field_validator, model_validator,ValidationInfo,
                       computed_field,ConfigDict)
from datetime import datetime,UTC
from typing import Literal,Annotated
from uuid import UUID,uuid4
import json



class User(BaseModel):
    model_config = ConfigDict(populate_by_name=True,extra="allow",validate_assignment=True,frozen=True) # accept a field name and also an alias
#model config le k garcha vanda : extra instance add garna dinxa while creating objs, validate assi le chei instance ma paxi change garna dinxa, froze garesi chei kei change garna mildena 
    uid : UUID = Field(alias = "id",default_factory=uuid4) 

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
    
    


### User Dictionary
user_data = {
    "id": "3bc4bf25-1b73-44da-9078-f2bb310c7374", ##model ma hale uid use garya cha but yeta chei id so pydantic ko alias agi nei define garisakeko cha 
    "username": "Corey_Schafer",
    "email": "CoreyMSchafer@gmail.com",
    "age": "39",
    "password": "secret123",
}
user = User.model_validate_json(json.dumps(user_data)) #useful when we r reading json file from an api or so on 

print(user.model_dump_json(indent=2,by_alias=True,exclude={"password"},include={"username","email"})) #pw is now excluded 






