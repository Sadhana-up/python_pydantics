##easy if we know type hints . # why use pydantics when u can do it manuallyn
##even if we have a small function , the validation is a lot 
# def create_user(username,email,password,age):
#     if not isinstance(username,str):
#         raise TypeError("Username must be a string ")
    
#     if not isinstance(email,str):
#         raise TypeError("email also should be a string")
    
#     if not isinstance(password,str):
#         raise TypeError("pw must be a string")
    
#     if not isinstance(age,int):
#         raise TypeError("age must be an integer")
    
#     return{"username ": username,"pw":password,"age":age,"email":email}


# a = create_user("sadhana","hiii123@","rumrummmm",21)
# print(a)

# a1 = create_user("ss","bb","cc","dd")
# print(a1)

##using PYDANTIC INSTEAD

from  pydantic import BaseModel
class User(BaseModel):
    username : str
    email :str 
    age : int

user1 = User(username="ram",email="ram@gmail.com",age=21)
print(user1)

u2 = User(username="hell",email="khoi",age="twentytwo")
print(u2)