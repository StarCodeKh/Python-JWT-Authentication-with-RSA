# Python JWT Authentication with RSA

Secure REST API authentication using Python, FastAPI, JWT, and RSA (RS256).

---

## Run Project

```bash
git clone https://github.com/StarCodeKh/Python-JWT-Authentication-with-RSA.git
cd Python-JWT-Authentication-with-RSA
python -m venv venv
source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
mkdir -p storage/rsa
openssl genpkey -algorithm RSA -out storage/rsa/private.pem -pkeyopt rsa_keygen_bits:2048
openssl rsa -pubout -in storage/rsa/private.pem -out storage/rsa/public.pem
cp .env.example .env
uvicorn app.main:app --reload
