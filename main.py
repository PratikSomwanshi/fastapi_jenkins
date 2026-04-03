from fastapi import FastAPI



app = FastAPI()


@app.get("/")
async def greet():
    return "This is comming from jenkins"