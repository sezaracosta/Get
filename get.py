import requests

url = 'https://httpbin.org/status/404'
request = requests.get(url)
status = request.status_code

if status == 200:
    print("Sucesso")
else:
    print("erro Conexão")