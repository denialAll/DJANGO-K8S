import requests
import sys

endpoint = "http://localhost:8000/api/login/"

token = "346378182118dabc9b4fa0fd66de0ca0bc3449656cc9044bde506d655147a30f"

username = "shaig"
password = "Shaig1234"
login_data = {'username':username, 'password':password}

headers = {
        "Authorization": f"TOKEN {token}"
    }

get_response = requests.post(endpoint, data=login_data)

print(get_response.json())