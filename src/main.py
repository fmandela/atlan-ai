import uvicorn 

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/", tags=["Root"])
async def index():
    return {"message": "Welcome to Atlas API"}

@app.get("/api/intro", tags=["Intro"])
async def intro():
    return {"message": "I am Mandela"}

# if __name__ == "__main__":
#     print("Starting app...")
#     uvicorn.run("app:app", host="0.0.0.0", port=3000, reload=True)