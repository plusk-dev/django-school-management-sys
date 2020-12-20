import random
import requests
import json

def quote():
    info = {
        'method':'getQuote',
        'lang':'en',
        'format':'json'
    }
    response = requests.get('http://api.forismatic.com/api/1.0/',info)
    content =json.loads(response.text)
    return content["quoteText"],content["quoteAuthor"]

