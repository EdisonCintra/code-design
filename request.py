import requests

# Definição da URL base da aplicação Flask
BASE_URL = "http://127.0.0.1:5000"

print("\n=== Testar rota /calculator/1 ===")

# Corpo da requisição que será enviado em formato JSON
payload = {
    "number": 30
}

try:
    # Envia requisição POST para o endpoint
    response = requests.post(f"{BASE_URL}/calculator/1", json=payload)

    # Exibe código de status e corpo da resposta
    print("Status Code:", response.status_code)
    print("Resposta:", response.json())

except Exception as e:
    print("Erro ao realizar requisição:", str(e))
