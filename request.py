import requests

# Definição da URL base da aplicação Flask
BASE_URL = "http://127.0.0.1:5000"

# ==============================
# Testar rota /calculator/1
# ==============================
print("\n=== Testar rota /calculator/1 ===")

payload_1 = {
    "number": 30
}

try:
    response = requests.post(f"{BASE_URL}/calculator/1", json=payload_1)
    print("Status Code:", response.status_code)
    print("Resposta:", response.json())
except Exception as e:
    print("Erro ao realizar requisição /calculator/1:", str(e))


# ==============================
# Testar rota /calculator/2
# ==============================
print("\n=== Testar rota /calculator/2 ===")

payload_2 = {
    "numbers": [2.12, 4.62, 1.32]  # lista de floats conforme Calculator2 espera
}

try:
    response = requests.post(f"{BASE_URL}/calculator/2", json=payload_2)
    print("Status Code:", response.status_code)
    print("Resposta:", response.json())
except Exception as e:
    print("Erro ao realizar requisição /calculator/2:", str(e))
