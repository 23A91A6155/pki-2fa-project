⭐ PKI + 2FA Authentication System (FastAPI + Docker)

This project demonstrates a secure authentication system using:

✔ RSA-based PKI encryption
✔ TOTP-based Two-Factor Authentication
✔ FastAPI backend API
✔ Docker container deployment

🚀 Features

Feature	Description
PKI Encryption	RSA Public/Private key encryption for secure messages
TOTP Authentication	Time-based OTP codes for secure login
Password Validation	Simple password check stored in dummy DB
API Testing	Works with Postman or Curl
📂 Project Structure

PKI-2FA-PROJECT/
│
├── app/
│   ├── __pycache__/        # auto-generated
│   ├── cron/
│   │   └── 2fa-cron        # cron script (if used)
│   ├── data/
│   ├── scripts/
│   │   ├── crypto_utils.py
│   │   ├── totp_utils.py
│   │   ├── log_2fa_cron.py     # optional
│   ├── __init__.py
│   └── main.py              # FastAPI App
│
|
├── student_private.pem
└── student_public.pem
│
├── scripts/
│   └── start.sh
│
├── .gitattributes
├── .gitignore
├── docker-compose.yml     
├── Dockerfile
├── README.md
└── requirements.txt


🛠 Run Using Docker
1️⃣ Build Docker Image
docker build -t pki-2fa-app .

2️⃣ Run the Container
docker run -d -p 8000:8000 --name pki-2fa-container pki-2fa-app

🧪 Test API Endpoints

📌 Use Postman or browser

✔ Check Server Running
GET http://localhost:8000/


Response:

{"message": "PKI + 2FA System Running"}

🔐 Encrypt Message
POST http://localhost:8000/encrypt
{ "message": "Hello World" }

🔓 Decrypt Message
POST http://localhost:8000/decrypt
{ "encrypted_message": "<paste encrypted text>" }

🔢 Generate TOTP (Enter code in login)
GET http://localhost:8000/generate-totp


Response:

{ "code": "123456" }

🔑 Login With 2FA
POST http://localhost:8000/login
{
  "username": "akhila",
  "password": "mypassword",
  "totp_code": "123456"
}


Success:

{ "message": "Login successful for akhila" }


Invalid Code:

{ "detail": "Invalid TOTP code" }

📌 Technologies Used

Component	Tool
Backend Framework	FastAPI
Containerization	Docker
Cryptography	RSA Keys
2FA	PyOTP
Language	Python

🏁 Conclusion

This project combines Public Key Infrastructure (PKI) and Two-Factor Authentication (2FA) to create a strong security model protecting data and user access.