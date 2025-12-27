# Python JWT Authentication with RSA

Secure REST API authentication using Python, FastAPI, JWT, and RSA (RS256).

---

## Run Project

```bash
git clone https://github.com/StarCodeKh/Python-JWT-Authentication-with-RSA.git
cd Python-JWT-Authentication-with-RSA
python -m venv venv
source venv/bin/activate   # macOS / Linux
openssl genpkey -algorithm RSA -out storage/rsa/private.pem -pkeyopt rsa_keygen_bits:2048
openssl rsa -pubout -in storage/rsa/private.pem -out storage/rsa/public.pem
cp .env.example .env
pip install fastapi uvicorn python-jose bcrypt mysql-connector-python python-dotenv cryptography
uvicorn app.main:app --reload



CREATE DATABASE python_rsa_auth;
USE python_rsa_auth;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  password VARCHAR(255),
  role VARCHAR(20) DEFAULT 'user',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE token_blacklist (
  id INT AUTO_INCREMENT PRIMARY KEY,
  token TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
