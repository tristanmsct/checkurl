import requests
from dotenv import dotenv_values

headers = {
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Authorization': 'Bearer KEY',
}

json_data = {
    'STR_URL': "airfrạncẹ.com",
}

response = requests.post('http://127.0.0.1:8000/api', headers=headers, json=json_data)

print(response.json())
