from fastapi import FastAPI
from exceptions import (pincode_not_found_error,invalid_pincode_error, PinCodeNotFoundError, InvalidPinCodeError)
from models import locationResponse, bulkRequest, pincodeRequest, bulkResponse
from data import pincode_db

app = FastAPI(
    title="Pincode Lookup API",
    description="Pincode lookup API for D2C brands to automatically fill city and state"
)

#custom exception handler
app.add_exception_handler(InvalidPinCodeError, invalid_pincode_error)
app.add_exception_handler(PinCodeNotFoundError, pincode_not_found_error)

@app.get("/")
def root():
    return {"message": "Pincode Lookup API"}

@app.get("/location/{code}", response_model=locationResponse)
def pincode_lookup(code:str):
    if len(code) != 6 or not code.isdigit():
        raise InvalidPinCodeError(code, "Must be exactly 6 digits")
    if code not in pincode_db:
        raise PinCodeNotFoundError(code)
    return pincode_db[code]

@app.post("/pincode/bulk", response_model=bulkResponse)
def bulk_lookup(request:bulkRequest):
    result = []
    missing = []
    
    for code in request.pincodes:
        if code in pincode_db:
            result.append(pincode_db[code])
        else:
            missing.append(code)
    
    return bulkResponse(found=len(result), not_found=len(missing), locations=result, missing=missing)


    

