from pydantic import BaseModel,field_validator

class pincodeRequest(BaseModel):
    pincode:str
    
    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value):
        if len(value) != 6 or not value.isdigit():
            raise ValueError("Pincode must be exactly 6 digits")
        return value

class locationResponse(BaseModel):
    pincode:str
    city:str
    state:str
    district:str
    
class bulkRequest(BaseModel):
    pincodes:list[str]
    
    @field_validator("pincodes")
    @classmethod
    def validate_pincodes(cls,value):
        if len(value) == 0:
            raise ValueError("There should be one pincode input")
        elif len(value) > 20:
            raise ValueError("There should be 20 maximum pincodes")
        
        for code in value:
            if len(code) != 6 or not code.isdigit():
                raise ValueError("Each  pincode must be exactly 6 digits")
        return value
                
                
class bulkResponse(BaseModel):
    status:str = "success"
    found:int
    not_found:int
    locations:list[locationResponse]
    missing:list[str]