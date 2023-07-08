from flask import Flask
from flask_cors import CORS

# flask, flask_cors - biblioteka,
# Flask, CORS - klasa

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.debug = True
