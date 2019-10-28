import requests,json

def get_quotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status_code == 200:
        random_quote = response.json()
        return random_quote
        