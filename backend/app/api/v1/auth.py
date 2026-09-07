from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.token import Token
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    service = AuthService(UserRepository(db))

    try:
        return service.register(user)

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc


@router.post(
    "/login",
    response_model=Token,
)
def login(
    credentials: UserLogin,
    db: Session = Depends(get_db),
):
    service = AuthService(UserRepository(db))

    try:
        token = service.login(
            credentials.email,
            credentials.password,
        )

        return Token(access_token=token)

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        ) from exc