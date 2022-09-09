from flask import Flask

app = Flask(__name__)


@app.route('/')     # methods=['GET'])
def home():
    return 'This is home page'


@app.route('/first')        # methods=['GET'])
def first_page():
    return 'This is first page'


if __name__ == '__main__':
    app.run()
