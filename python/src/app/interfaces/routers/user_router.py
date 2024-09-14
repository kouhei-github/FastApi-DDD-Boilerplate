from fastapi import APIRouter, Depends
from typing import List
from src.app.application.services.user_service import UserService
from src.app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from src.app.interfaces.schemas.user_schema import UserCreate, UserResponse
from src.app.domain.models.user import User

router = APIRouter()

def get_user_service():
    user_repository = UserRepositoryImpl()
    return UserService(user_repository)

@router.get("/users", response_model=List[UserResponse])
def read_users(user_service: UserService = Depends(get_user_service)):
    users = user_service.get_users()
    return [UserResponse(user_id=user.user_id, name=user.name, email=user.email) for user in users]

@router.post("/users", response_model=UserResponse)
def create_user(user_create: UserCreate, user_service: UserService = Depends(get_user_service)):
    user = User(name=user_create.name, email=user_create.email)
    created_user = user_service.create_user(user)
    return UserResponse(user_id=created_user.user_id, name=created_user.name, email=created_user.email)
