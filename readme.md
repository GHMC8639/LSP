
# LSP Backend API (Loan Service Platform)

##  Project Overview

LSP Backend is a FastAPI-based backend application developed for a Loan Service Platform.
The system supports **User**, **Lender**, and **Super Admin** roles with secure authentication,
OTP verification, and role-based access control.

This project provides APIs for:

- User Registration & Login
- OTP Verification
- Super Admin Access Control
- Lender Management
- User Management
- Authentication & Security

---

##  Features
- OTP Length: 6 digits
- OTP Expiry: 5 minutes
- Max Attempts: 3
- Auto Registration: Yes
- Session Expiry: 1 day
- Refresh Token: 30 days

### Authentication & Security
- User Registration with OTP verification
- Login authentication
- Password hashing
- OTP generation and verification
- Session handling

###  Role-Based Access
- **User**
  - Register and login
  - Access own data
- **Lender**
  - Lender-related operations
- **Super Admin**
  - View all users
  - Manage users and lenders
  - Platform-level access

### OTP System
- OTP generation
- OTP verification
- OTP cleanup service

###  Database Integration
- SQLAlchemy ORM
- PostgreSQL / MySQL supported
- Centralized database configuration

---

##  Project Structure

```
LSP/
│
├── app/
│   ├── core/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone <repository_url>
cd LSP
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

Activate environment:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / Mac**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create `.env` file:

```
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 5️⃣ Run Application
```bash
uvicorn app.main:app --reload
```

API runs at:
```
http://127.0.0.1:8000
```

Swagger Docs:
```
http://127.0.0.1:8000/docs
```

---

## 🔐 User Roles

| Role | Access |
|------|--------|
| User | Register, Login, Access own data |
| Lender | Manage lender-related data |
| Super Admin | Full system access |

---

## 🛠️ Tech Stack

- FastAPI
- Python 3.10+
- SQLAlchemy
- Pydantic
- JWT Authentication
- PostgreSQL / MySQL

---

## ✅ Future Improvements

- Refresh token implementation
- Email/SMS notification integration
- Admin dashboard APIs
- Logging & monitoring
Flow Chart:
 
 
┌───────────────┐
│ App Launch    │
└───────┬───────┘
        ↓
┌────────────────────────┐
│ Auth Landing Screen    │
│ Login | Sign Up |      │
│ Forgot Password        │
└───────┬─────────┬──────┘
        │         │
        │         └───────────────┐
        │                         ↓
        │        ┌────────────────────────┐
        │        │ Forgot Password Flow   │
        │        └──────────┬─────────────┘
        │                   ↓
        │        ┌────────────────────────┐
        │        │ Enter Mobile / Email   │
        │        └──────────┬─────────────┘
        │                   ↓
        │        ┌────────────────────────┐
        │        │ OTP Verification       │
        │        └──────────┬─────────────┘
        │                   ↓
        │        ┌────────────────────────────┐
        │        │ OTP Attempts Check         │
        │        └───────┬───────────┬────────┘
        │                │ Valid     │ Exceeded
        │                │           ↓
        │                │  ┌────────────────────────┐
        │                │  │ Account Blocked        │
        │                │  │ (24 Hours Lock)        │
        │                │  └──────────┬─────────────┘
        │                │             ↓
        │                │   Auto Activate After 24h
        │                │
        │                ↓
        │        ┌────────────────────────┐
        │        │ Set New Password       │
        │        └──────────┬─────────────┘
        │                   ↓
        │        ┌────────────────────────┐
        │        │ Back to Login          │
        │        └────────────────────────┘
        │
        ↓
┌────────────────────────┐
│ Login Screen           │
│ Mobile + Password/OTP  │
└───────┬────────────────┘
        ↓
┌────────────────────────┐
│ Input Validation       │
└───────┬────────────────┘
        ↓
┌────────────────────────┐
│ Account Blocked?       │
└───────┬─────────┬──────┘
        │ No            │ Yes
        │               ↓
        │      ┌────────────────────────┐
        │      │ Show Block Message     │
        │      │ Try After 24 Hours     │
        │      └────────────────────────┘
        ↓
┌────────────────────────┐
│ User Exists?           │
└───────┬─────────┬──────┘
        │ Yes           │ No
        │               ↓
        │  ┌────────────────────────┐
        │  │ Sign-Up Flow           │
        │  │ • Enter details        │
        │  │ • OTP verification     │
        │  └──────────┬─────────────┘
        │             ↓
        │     ┌────────────────────────┐
        │     │ OTP Attempts Check     │
        │     └───────┬─────────┬──────┘
        │             │ Valid  │ Exceeded
        │             │        ↓
        │             │  ┌────────────────────────┐
        │             │  │ Account Blocked        │
        │             │  │ (24 Hours Lock)        │
        │             │  └────────────────────────┘
        │             ↓
        │        Back to Login
        │
        ↓
┌────────────────────────┐
│ Verify Credentials     │
└───────┬─────────┬──────┘
        │ Success       │ Fail
        │               ↓
        │  ┌────────────────────────┐
        │  │ Show Error Message     │
        │  │ Retry Login            │
        │  └────────────────────────┘
        │
        ↓
┌────────────────────────┐
│ Create Session         │
│ • Session record       │
│ • Refresh token        │
└───────┬────────────────┘
        ↓
┌────────────────────────┐
│ Issue JWT Access Token │
└───────┬────────────────┘
        ↓
┌────────────────────────┐
│ Login Success          │
│ Dashboard              │
└────────────────────────┘

## ER Diagrams

                 ┌──────────────┐
                 │    USERS     │
                 │--------------│
                 │ id (PK)      │
                 │ username     │
                 │ mobile_number│
                 │ password_hash│
                 │ role         │
                 │ created_at   │
                 └──────┬───────┘
                        │
            ┌───────────┴────────────┐
            │                        │
            ▼                        ▼
   ┌────────────────┐        ┌────────────────┐
   │ USER_SESSIONS  │        │    LENDERS     │
   │----------------│        │----------------│
   │ id (PK)        │        │ id (PK)        │
   │ user_id (FK)   │        │ user_id (FK)   │
   │ session_token  │        │ company_name   │
   │ refresh_token  │        │ gst_number     │
   │ is_active      │        │ is_active      │
   │ expires_at     │        │ is_verified    │
   └────────────────┘        └────────────────┘

## Flow of ER Diagram
 
 Relationship                           Type
---------------                      ------------
User -> Sessions                      One to Many
User -> Lender                        One to One
Lender -> User                        Many to One


 # API Endpoints
 
Send OTP
POST /auth/send-otp
Request:
{
  "mobile_number": "9032148034",
  "usename": "kalyani"
}
 
Verify OTP
POST /auth/verify-otp
Request:
{
  "mobile_number": "9032148034",
  "otp": "123456"
}
 
# OTP Rules
- OTP valid for 5 minutes
- Maximum 3 attempts
- OTP invalid after success
 
# Auto Registration
If mobile number does not exist, system creates a new user automatically.
 
# Session Management
Access Token expiry: 1 day
Refresh Token expiry: 30 days
 
# Security Best Practices
- Hash OTP before storing
- Limit OTP attempts
- Expire OTP automatically

## users
- Basic registered account.
- Can apply for loans.
- Can view personal loan status.
- Cannot access admin or lender modules.
- Role name stored as: USER.

## database model
| Action           | Table Name                      |
| ---------------- | ------------------------------- |
| Register User    | users                           |
| Store Password   | users                           |
| Activate Account | users (is_active=true)          |
| Update Profile   | users                           |
| Delete User      | users (is_deleted=true)         |
| Login            | user_sessions                   |
| Logout           | user_sessions (is_active=false) |



 
 ## superadmin 
- Default system-level account.
- Has full access to all APIs and modules.
- Can create, update, and delete Lender accounts.
- Can view all registered users.
- Can manage roles and permissions.
- Can monitor system activities.
- Role name stored as: SUPER_ADMIN.
- Password is stored in hashed format in database.
- Should change default password after first login.

## Database model

| Action             | Table Name    |
| ------------------ | ------------- |
| Create Super Admin | users         |
| Login Super Admin  | user_sessions |
| Create Lender      | users         |
| View All Users     | users         |
| Disable User       | users         |
| Delete Lender      | users         |
| Logout             | user_sessions |


## lender
- Created by Super Admin.
- Can manage loan-related operations.
- Can view and manage users under their scope.
- Cannot create or manage Super Admin accounts.
- Role name stored as: LENDER.
- Authentication required via OTP and password.
- Access restricted based on role-based authorization.

## database models

| Action                | Table Name    |
| --------------------- | ------------- |
| Create Lender Account | users         |
| Store Lender Details  | lenders       |
| Update Lender Details | lenders       |
| Login Lender          | user_sessions |
| View Assigned Users   | users         |
| Manage Loans          | loans         |
| Logout                | user_sessions |

 
# summary:
 
Existing users are authenticated → session created,
new users are redirected to signup before authentication
 