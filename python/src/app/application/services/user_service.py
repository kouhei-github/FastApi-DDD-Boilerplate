from typing import List
from app.domain.models.user import User
from app.domain.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: int) -> User:
        return self.user_repository.get_user_by_id(user_id)

    def get_users(self) -> List[User]:
        return self.user_repository.get_all_users()

    def create_user(self, user: User) -> User:
        return self.user_repository.create_user(user)
