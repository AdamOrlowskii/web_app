from jose import JWTError, jwt
from datetime import datetime, timedelta


SECRET_KEY = "nhfiaw8475nv8uqu45vyiuwllw75598pnvy5324ws3409d25e094faa6ca2556c818166b7a6429b93f7099f6f0f4ctf6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt