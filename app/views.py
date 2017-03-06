from app import app
from Oauth import main

@app.route('/')
@app.route('/index')
def index():
    temp = '''
    <!DOCTYPE html>
        <!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
        <!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
        <!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
        <!--[if gt IE 8]><!-->
        <html lang="en" class="no-js" ng-app="MovieApp">
        <!--<![endif]-->

        <head>

        </head>

        <body>

    '''
    for s in main():
        temp = temp + "<p>" + s + "</p>"
    temp = temp + '<body>'

    return temp