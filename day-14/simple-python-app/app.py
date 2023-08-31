from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Say,Hello to world!'

if __name__ == '__main__':
    app.run()

