import requests

product_id = input('What product id do you want to destroy? \n')

try: 
    product_id = int(product_id)
except:
    product_id = None
    print('The product id you entered is wrong. Please enter a valid product id!')

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete"

    get_response = requests.delete(endpoint)

    print(get_response.status_code, get_response.status_code == 204)