import requests

endpoint = "http://localhost:8000/products/create/"

headers = {'Authorization':'Token 60d4bc57379a4c2877a6f51da44761423822153990e4b504eaa9cd025ab4b4b1'}
data = {
    'category': 'Italian',
    'title': 'Margheretta Pizzano',
    'description': 'Thin crust pizza with tomato and mozarella cheese',
    'price': 1669,
    'is_available': True,
    'serving': 5,
}

get_response = requests.post(endpoint, json=data, headers = headers)
# get_response = requests.get(endpoint, headers = headers)

print(get_response.json())


cart_data = {
    "cart": {
        "note":"This is dry test run.",
    },
    "cart_items": {
        "item": [
            "product": 1,
            "quantity":2,
        ],
        "item": [
            "product": 2,
            "quantity":4,
        ],
        "item": [
            "product": 3,
            "quantity":1,
        ],
    },
}

data2 = 
{
    "cart": {
        "note":"This is dry test run."
    },
    "cartItems": [
        {
            "product": 1,
            "quantity": 2
        },
        {
            "product": 2,
            "quantity": 4
        },
        {
            "product": 3,
            "quantity": 1
        }
    ]
}

{
   "cart": {
    "phone_number": "03415158965",
    "note": "This is a great debacle",
    "is_accepted": false,
    "address": 2
   },
   "cartItems": [
      {
         "product": 1,
         "quantity": 2
      },
      {
         "product": 2,
         "quantity": 4
      },
      {
         "product": 3,
         "quantity": 1
      }
   ]
}

{
"merchant": 3,
"address": 2,
"phone_number": "06848526781",
"note": "I have been stuck on this problem for way long"
}