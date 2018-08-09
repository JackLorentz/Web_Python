import requests

url = "http://localhost:12345/"

params = {
    'message': '[Python Client]: Client sends the message .'
}

res = requests.post(url, data = params)

print(res.text)