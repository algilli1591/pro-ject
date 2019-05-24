
import sqlalchemy

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def appy():
    return render_template('webby.html')