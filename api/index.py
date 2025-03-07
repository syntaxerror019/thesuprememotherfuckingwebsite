from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    with open("page.txt", "r") as f:
        res = file.readlines()
    return res
