from flask import Flask


app = Flask(__name__)
app.config['DEBUG'] = True

from api import routes