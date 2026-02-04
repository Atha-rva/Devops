import requests

API_URL = "https://official-joke-api.appspot.com/random_joke"
DAD_JOKES_URL = "https://icanhazdadjoke.com/"
def jokes_data_fn(url_type, mood):
    headers = {
        "Accept":"application/json"
    }
    response = requests.get(url=url_type, headers=headers)

    if mood == "dad":
        finalJoke = response.json()
    if mood == "pj":
        finalJoke = response.json()["setup"] + response.json()["punchline"]  # Filter out a Whole Joke 

    return finalJoke

mood = input("Enter your Mood Type :- ")

if mood == "dad":
    url_type = DAD_JOKES_URL
elif mood == 'pj':
    url_type = API_URL
finalJoke = jokes_data_fn(url_type,mood)

print(finalJoke)

    