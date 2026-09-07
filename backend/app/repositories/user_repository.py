from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)

        return self.db.execute(statement).scalar_one_or_none()

    def create(
        self,
        full_name: str,
        email: str,
        hashed_password: str,
    ) -> User:
        user = User(
            full_name=full_name,
            email=email,
            hashed_password=hashed_password,
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user