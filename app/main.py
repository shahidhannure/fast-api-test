from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Azure!"}

@app.get("/ping")
def ping():
    return {"status": "ok"}
