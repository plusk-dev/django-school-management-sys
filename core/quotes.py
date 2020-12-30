import random
import requests

def quote():
    info = {
        'method':'getQuote',
        'lang':'en',
        'format':'json'
    }
    response = requests.get('http://api.forismatic.com/api/1.0/',info)
    content =response.json()
    return content["quoteText"],content["quoteAuthor"]

