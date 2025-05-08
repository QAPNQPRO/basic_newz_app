# from app import bcrypt
import bcrypt # type: ignore


def encrypt_password(password: str) -> str:
    salt = bcrypt.gensalt()  # Generate a salt
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password


def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password, hashed)
