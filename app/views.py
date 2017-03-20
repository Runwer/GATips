from app import app
from Oauth import main
from flask import render_template
from flask import Flask,jsonify
import requests
import json

@app.route('/')
@app.route('/index')
def index():
    artlist, totalusers, artpart = main('rt:activeUsers', 'rt:pageTitle, rt:pagePath' )
    sources, fb, eb = main('rt:activeUsers', 'rt:source' )
    fb = round((float(fb)/totalusers) * 100, 2)
    eb = round((float(eb) / totalusers) * 100, 2)
    return render_template('realtime.html', type=type, GA_req=artlist, GA_artpart=artpart, GA_src=sources, GA_tot = totalusers, GA_fb=fb, GA_eb=eb)


@app.route("/testapi")
def testapi():
    uri = "https://9zsc6adzzj.execute-api.eu-west-1.amazonaws.com/prod"
    try:
        response = requests.get(uri).json()
        response = sorted(response, key=lambda x: float(x['scoreEngagement']), reverse=True)
        response = response[0:20]
    except requests.ConnectionError:
       return "Connection Error"

    return render_template('TestApi.html', type=type, data = response)


    return Jresponse

if __name__ == "__main__":
    app.run(debug = True)
