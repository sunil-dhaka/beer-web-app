from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def beerSuggester():
    url='https://api.punkapi.com/v2/beers/random'
    r=requests.get(url)
    beerJson=r.json()[0]
    beer={
        'name':beerJson['name'],
        'tagline':beerJson['tagline'],
        'desc':beerJson['description'],
        'image':beerJson['image_url'],
        'abv':beerJson['abv']
    }
    #print(beerJson)
    return render_template('index.html',beer=beer)