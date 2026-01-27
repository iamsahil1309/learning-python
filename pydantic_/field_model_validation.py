from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username : str


    @field_validator('username')
    def username_length(cls,v) :
        if v < 4 :
            raise ValueError("username must be greater than or equal to 4 characters")
        return v
    
class SignupData(BaseModel):
    password : str
    confirm_password : str

    @model_validator(mode='after')
    def password_check(cls,value):
        if value.passwaord != value.confirm_password :
            raise ValueError("Password do not match")
        return value