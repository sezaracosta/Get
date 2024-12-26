import requests

url = 'https://httpbin.org/post'

dados = {"Nome": "Joãozinho"}

response = requests.post(url,data=dados )

print(response.text)