from flask import Flask
main = Blueprint('main',__name__)
from . import views,errors