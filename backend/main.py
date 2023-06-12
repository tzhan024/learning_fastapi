from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello Worldddd"}

@router.get("/users/{username}")
async def read_user(username: str):
    return {"username": username}