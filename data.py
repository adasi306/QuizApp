import requests

parameters: dict[str, str | int] = {"amount": 10, "type": "boolean"}

response: requests.Response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data: dict[str, object] = response.json()
question_data: list[dict[str, object]] = data["results"]