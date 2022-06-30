import uvicorn 
import os 
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

# from .db.connect import connect
#
load_dotenv()

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# connect()


@app.get("/", tags=["Index"])
async def index():
    return {"message": "Atlan AI"}

@app.get("/api/intro", tags=["Intro"])
async def intro():
    return {"message": "Welcome to Atlan"}

@app.get("/api/lana", tags=["Lana"])
async def lana():
    return {"message": "Hello, I'm Lana ..."}

@app.get("/api/wadau", tags=["Wadau", "Chama"])
async def wadau():
    return {"message": "Welcome to Wadau: Your pathway to Posperity"}
# if __name__ == "__main__":
#     print("Hello ")
#     print("Starting app...")
#     uvicorn.run("app:app", host="0.0.0.0", port=3000, reload=True)