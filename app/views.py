from app import app
from Oauth import main
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    artlist, totalusers, artpart = main('rt:activeUsers', 'rt:pageTitle, rt:pagePath' )
    sources, fb, eb = main('rt:activeUsers', 'rt:source' )
    fb = round((float(fb)/totalusers) * 100, 2)
    eb = round((float(eb) / totalusers) * 100, 2)
    return render_template('realtime.html', type=type, GA_req=artlist, GA_artpart=artpart, GA_src=sources, GA_tot = totalusers, GA_fb=fb, GA_eb=eb)
