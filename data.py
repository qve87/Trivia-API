import requests

parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean"

}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question = response.json()
question_data = question['results']
