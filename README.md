 In the main.py file we have seen how , with the increase in the number of functions , validation becomes harder. 
A solution to this can be the use of pydantics in python. 

pydantic_1.py : I have used the modules : Pydantic , Typing, UUID, Datetime 
with objects 1. pydantic package : BaseModel, ValidationError,Field,EmailStr,HttpUrl,SecretStr 
2. TYPING PACKAGE : Literal , Annotated 
3. UUID : uuid, uuid4 

I have made a base class and used typehinting (in this case pydantic modelling). 

2_using_decorators : 
Here i have enlarged my scope by using decorators like : Validators : @fieldvalidator & @model_validator inside the @classmethod 



