from flask import Flask
from configuracao import configure_all

app = Flask(__name__)

configure_all(app)

app.run(debug=True, port='3000')