
from fastapi import Request
from fastapi.responses import JSONResponse


# Custom exception classes

class PinCodeNotFoundError(Exception):
    def __init__(self, pincode: str):
        self.pincode = pincode


class InvalidPinCodeError(Exception):
    def __init__(
        self,
        pincode: str,
        reason: str = "Invalid Format"
    ):
        self.pincode = pincode
        self.reason = reason


# Custom exception handler

async def pincode_not_found_error(
    request: Request,
    exc: PinCodeNotFoundError
):
    return JSONResponse(
        status_code=404,
        content={
            "error": "pincode_not_found",
            "message": f"No location found for the pincode: {exc.pincode}",
            "pincode":f"{exc.pincode}"
        }
    )
    
async def invalid_pincode_error(request:Request, exc:InvalidPinCodeError):
    return JSONResponse(
        status_code=400,
        content={
            "error":"invalid_pincode",
            "message":f"Pincode : {exc.pincode} is invalide, Reason : {exc.reason}",
            "pincode":exc.pincode
        }
    )

