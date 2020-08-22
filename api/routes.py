from flask import render_template
from api import app

@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')