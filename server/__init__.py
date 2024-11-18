import flask

app = flask.Flask(__name__)

from server.api import get_endpoint, post_endpoint

