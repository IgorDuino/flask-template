from decouple import config

import string
import random


class Settings:
    SERVER_HOST = "localhost"

    DEBUG = config("DEBUG", cast=bool, default=False)

    DB_USER = config("DB_USER")
    DB_NAME = config("DB_NAME")
    DB_PASS = config("DB_PASS")
    DB_HOST = config("DB_HOST")
    DB_PORT = config("DB_PORT")

    DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    SECRET_KEY = config(
        "SECRET_KEY",
        default="".join([random.choice(string.ascii_letters) for _ in range(32)]),
    )
    JWT_ALGORITHM = "HS25"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 day

    LOGIN_URL = SERVER_HOST + "/login"


settings = Settings()
