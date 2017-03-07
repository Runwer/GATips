from app import app
from Oauth import main
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    artlist, totalusers = main('rt:activeUsers', 'rt:pageTitle, rt:pagePath' )
    return render_template('realtime.html', type=type, GA_req=artlist, GA_src=main('rt:activeUsers', 'rt:source' ), GA_tot = totalusers)
