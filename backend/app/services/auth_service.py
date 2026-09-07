from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.security.jwt import create_access_token
from app.security.password import hash_password, verify_password


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(self, user: UserCreate):
        existing_user = self.repository.get_by_email(user.email)

        if existing_user:
            raise ValueError("Email already registered")

        hashed_password = hash_password(user.password)

        return self.repository.create(
            full_name=user.full_name,
            email=user.email,
            hashed_password=hashed_password,
        )

    def login(self, email: str, password: str) -> str:
        user = self.repository.get_by_email(email)

        if user is None:
            raise ValueError("Invalid credentials")

        if not verify_password(password, user.hashed_password):
            raise ValueError("Invalid credentials")

        return create_access_token(subject=user.email)