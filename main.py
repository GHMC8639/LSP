import asyncio

from fastapi import FastAPI
from services.otp_cleanup import cleanup_otps
from core.database import Base
from core.database import engine, SessionLocal
from core.seed import create_default_super_admin
from core.config import  SUPER_ADMIN_MOBILE, SUPER_ADMIN_PASSWORD,SUPER_ADMIN_NAME,SUPER_ADMIN_DEVICE_ID
from routers import user_register
from routers import lender
from routers import superadmin_access
from routers import login_SL





Base.metadata.create_all(bind=engine)

app = FastAPI(title="Loan Service Platform - OTP and Session Auth API")

@app.on_event("startup")
def startup():
    db = SessionLocal()
    try:
        if SUPER_ADMIN_MOBILE and SUPER_ADMIN_PASSWORD:
            create_default_super_admin(
                db,
                SUPER_ADMIN_NAME,
                SUPER_ADMIN_MOBILE,
                SUPER_ADMIN_PASSWORD,
                SUPER_ADMIN_DEVICE_ID,
              
            )
    finally:
        db.close()

@app.get("/",tags=["start"])
def read_root():
    return {"message": "Welcome to the OTP + Session Auth API"}
app.include_router(user_register.router)
app.include_router(lender.router)
app.include_router(login_SL.router)
app.include_router(superadmin_access.router)

async def otp_cleanup_loop():
    while True:
        db = SessionLocal()
        try:
            cleanup_otps(db)
        finally:
            db.close()
        await asyncio.sleep(300)  # every 5 minutes
 
 
@app.on_event("startup")
async def start_cleanup():
    asyncio.create_task(otp_cleanup_loop())



