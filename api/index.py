from flask import Flask

app = Flask(__name__)

res = """
THE SUPREME MOTHERFUCKING WEBSITE\n
---------------------------------\n
With all your fancy template based websites you probably think markdown is where its at.\n
Have you forgotten?

"""

@app.route('/')
def home():
    return res
