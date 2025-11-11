from pydantic import BaseModel,ValidationError
from datetime import datetime

##we define a class which inherits from base model

class User(BaseModel):
    uid :int 
    username : str 
    email :str

    verified_at : datetime |None = None

    bio : str = "" ##Optional Fields
    is_active :bool = True#optioanl field cause we have passed the value 

    full_name :str |None = None  #full name is either string or none 
    #using union 



##when creating user instances , it has to be passed on 
try :

    user = User(username=None,email="hello@gmail.com",uid=123)
    print(user)

except ValidationError as e : 
    print(e)

user.bio = "developer"

##Acess and modify data 
print(user.username)
print(user.bio) #doesnot trigger re-validation 


print(user.model_dump_json(indent=3)) #serialize our model for storage and sendng into network 
#Serialize : python obj into simple format that can be easily saved into a file 


