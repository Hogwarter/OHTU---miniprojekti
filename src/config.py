
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv

load_dotenv()

test_env = getenv("TEST_ENV") == "true"
print(f"Test environment: {test_env}")

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY", "default_secret_key")
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://my_superuser:mypassword@localhost/mydatabase"
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://lossis:yourpassword@localhost/refrences"
db = SQLAlchemy(app)