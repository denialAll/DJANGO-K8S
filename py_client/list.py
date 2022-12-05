import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/customers/login/"
username = 'ladeagfdle'
email = 'aaamir@gmail.com'
password = 'Qwertylsfjasd123'

auth_response = requests.post(auth_endpoint, json={'username':username, 'password':password})

print(auth_response.json())



if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"TOKEN {token}"
    }
    get_response = requests.get(auth_endpoint, headers=headers)
    print(get_response.json())