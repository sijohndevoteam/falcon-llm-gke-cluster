import requests

data = {"prompt": "Who is Lionel Messi?"}
res = requests.post("http://127.0.0.1:8080/v1/models/model:predict", json=data)
print(res.json())