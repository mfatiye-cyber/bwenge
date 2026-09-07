from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository


class UserService:

    @staticmethod
    def get_current_user(db: Session, email: str):
        repository = UserRepository(db)
        return repository.get_by_email(email)