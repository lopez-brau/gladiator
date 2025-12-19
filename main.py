from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from config import get_settings


# Initialize the FastAPI app and the app settings.
app = FastAPI()
settings = get_settings()

# Set up CORS to allow whitelisted origins, cookies, all HTTP requests, and
# all HTTP request headers.
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up an exception handler for converting HTTP exceptions to JSON.
@app.exception_handler(StarletteHTTPException)
async def exception_handler(
    request: Request,
    exception: StarletteHTTPException,
):
    return JSONResponse(
        status_code=exception.status_code,
        content=jsonable_encoder(
            {
                "url": request.url.path,
                "detail": exception.detail,
            }
        )
    )

