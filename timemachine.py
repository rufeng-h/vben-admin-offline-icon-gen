import requests

response = requests.get("http://localhost:3000/login/cellphone",
                        params={"cellphone": "19586444040", "password": "@windcf20001123"})
print(response.text)
