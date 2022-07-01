import fastapi
import api.api
from config import cfg

SVC_BASE_URL = "/fasthound"
redoc_url = open_api_url = docs_url = None
if cfg.EXPOSE_API_DOCUMENTATION:
    redoc_url = f"{SVC_BASE_URL}/public/redoc"
    open_api_url = f"{SVC_BASE_URL}/public/openapi"
    docs_url = f"{SVC_BASE_URL}/public/docs"

app = fastapi.FastAPI(
    title="Fast Hound",
    version="0.2",
    responses={404: {"description": "Not found"}},
    description="Fast Hound API",
)

app.include_router(api.api.router)
