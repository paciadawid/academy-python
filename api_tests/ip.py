import requests


res = requests.get("https://swapi.dev/api/people/1")
status_code = res.status_code
response_text = res.text
response_json = res.json()
headers = res.headers
cookies = res.cookies
print()

assert response_json["name"] == "Luke Skywalker", response_json["name"]
