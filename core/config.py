from dotenv import load_dotenv
import os

from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

SUPERADMIN_TOKEN = os.getenv("SUPERADMIN_TOKEN")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
SUPER_ADMIN_NAME= os.getenv("SUPER_ADMIN_NAME")
SUPER_ADMIN_MOBILE = os.getenv("SUPER_ADMIN_MOBILE")
SUPER_ADMIN_DEVICE_ID = os.getenv("SUPER_ADMIN_DEVICE_ID")
SUPER_ADMIN_PASSWORD = os.getenv("SUPER_ADMIN_PASSWORD")



ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 10))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 30))

DATABASE_URL = "postgresql://postgres:8639@localhost:5432/Lsp_project"

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY not found in environment")










