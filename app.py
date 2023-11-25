# app.py
# web-server
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    i = 0
    while i < 99999999:
        i+=1
    return 'Welcome to CommunitySphere!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
