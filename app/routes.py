from flask import Blueprint

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return "Hello, GitHub Lab!"

@main.route("/about")
def about():
    return "About page"

@main.route("/login")
def login():
    return "Login page - Insira os seus dados"