from flask import Flask

app = Flask(__name__)

from nytdashboardapp import routes
