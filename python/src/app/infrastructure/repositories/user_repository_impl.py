from typing import List
from src.app.domain.models.user import User
from src.app.domain.repositories.user_repository import UserRepository

class UserRepositoryImpl(UserRepository):
    def __init__(self):
        # メモリ上にユーザーを保存
        self.users = {}
        self.next_id = 1

    def get_user_by_id(self, user_id: int) -> User:
        return self.users.get(user_id)

    def get_all_users(self) -> List[User]:
        return list(self.users.values())

    def create_user(self, user: User) -> User:
        user.user_id = self.next_id
        self.users[self.next_id] = user
        self.next_id += 1
        return user
