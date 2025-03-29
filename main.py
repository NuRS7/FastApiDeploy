from fastapi import FastAPI
from users.generic import router as generic_router


app = FastAPI(title="DeployApp")
app.include_router(generic_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
