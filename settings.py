from decouple import config

import string
import random


class Settings:
    SERVER_HOST = "localhost"

    DEBUG = config("DEBUG", cast=bool, default=False)

    DB_URL = "sqlite:///data/database.db"

    SECRET_KEY = config(
        "SECRET_KEY",
        default="".join([random.choice(string.ascii_letters) for _ in range(32)]),
    )
    JWT_ALGORITHM = "HS25"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 day

    LOGIN_URL = SERVER_HOST + "/login"


settings = Settings()
