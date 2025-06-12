import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "input": [5, 116, 74, 0, 0, 25.6, 0.201, 30, 0, 0, 1]  # Pastikan jumlah fitur = 11
}

response = requests.post(url, json=data)

# Cek status code dan tampilkan hasil
print("Status Code:", response.status_code)

try:
    print("Response JSON:", response.json())
except Exception as e:
    print("Gagal parse response JSON:", str(e))
    print("Isi Response Mentah:", response.text)
