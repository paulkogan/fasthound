from fastapi import FastAPI
from config import cfg

app = FastAPI()


@app.get("/")
async def root():
    # return {"message": f"Hello Fasthound 4"}
    return {"message": f"Hello Fasthound 4 {cfg.DB_HOST}"}
