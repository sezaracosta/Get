import requests

url = 'https://httpbin.org/status/404'
request = requests.get(url)
status = request.status_code

if status >= 200:
    if status == 200:
        print('Sucesso')   
    if status != 200:
        print("sem conexão")
else:
    print("Erro!")


