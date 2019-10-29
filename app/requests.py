import requests,json

def get_quotes():
    '''
    Method to get random quotes
    '''
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status_code == 200:
        quote = response.json()
       
        return quote
        