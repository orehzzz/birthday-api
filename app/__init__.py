from flask import Flask
from flask_jwt_extended import JWTManager
import configparser
from flask_cors import CORS

# os.chdir(os.path.dirname(os.path.abspath(__file__))) #set file's directory as working
config = configparser.ConfigParser()
config.read("config.ini")

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = config.get("Main", "secret_key")
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]

jwt = JWTManager(app)

CORS(app)
