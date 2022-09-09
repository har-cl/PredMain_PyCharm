import os
from flask_cors import CORS, cross_origin
import flask_monitoringdashboard as dashboard
from flask import Flask, request, render_template
from wsgiref import simple_server

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
dashboard.bind(app)
CORS(app)


@app.route('/', methods=['GET'])    # setting home url
@cross_origin()    #to permit browser to load resource from any other resource other then current file's own
def home():
    print(__name__)
    return render_template('index.html')


@app.route('/train', methods=['POST'])  # setting train url
@cross_origin()
def trainRouteClient():
    try:
        pass
    except:
        pass


@app.route('/predict', methods=['POST'])    # setting test url
@cross_origin()
def predictRouteClient():
    try:
        pass
    except:
        pass


port = int(os.getenv('PORT', 5000))
if __name__ == '__main__':
    host = '0.0.0.0'
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()
