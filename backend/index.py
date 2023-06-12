from fastapi import FastAPI
import uvicorn
import main
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main.router, tags=["users"])


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("index:app", host="127.0.0.1", port=8000, reload = True)