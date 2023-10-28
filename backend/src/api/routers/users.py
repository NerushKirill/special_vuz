from fastapi import APIRouter

from backend.src.core.shemas.users import User


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[User])
async def read_users(skip: int = 0, limit: int = 10):
    pass


@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int):
    pass


@router.post("/", response_model=User)
async def create_user(user: User):
    pass


@router.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    pass
