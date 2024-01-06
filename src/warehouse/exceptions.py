from fastapi import HTTPException
from starlette.responses import JSONResponse


class CustomException(HTTPException):
    def __int__(self, detail: str, status_code: int = 500):
        super().__init__(status_code=status_code, detail=detail)


async def handler_input_params(request, exc):
    return JSONResponse(
        status_code=422,
        content={"Message": "Isnt correct input data", "errors": exc.errors()},
    )
