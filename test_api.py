import requests

APP_ID = "c7ab1e60"
APP_KEY = "c983beace33befb29ed2dfa9c742cf8e"

url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

params = {
    "app_id": "c7ab1e60",
    "app_key": "c983beace33befb29ed2dfa9c742cf8e",
    "results_per_page": 5,
    "what": "python developer"
}

response = requests.get(url, params=params)

data = response.json()

for job in data["results"]:
    print(job["title"], "-", job["company"]["display_name"])
