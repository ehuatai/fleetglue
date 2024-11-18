import flask
import server
import requests

GET_URL = "http://localhost:8000/api/get"
POST_URL = "http://localhost:8000/api/post"

ACTION_QUEUE = []


@server.app.route("/api/post", methods=["POST"])
def post_endpoint():
    """
    Gets JSON field of request and adds it to the action queue
    """
    data = flask.request.get_json()
    ACTION_QUEUE.append(data)
    return "OK", 201


@server.app.route("/api/get", methods=["GET"])
def get_endpoint():
    """
    If actions remain, pop (FIFO) and send them with code 200
    Else, send nothing with code 204
    """
    if ACTION_QUEUE:
        return ACTION_QUEUE.pop(0), 200
    else:
        return "No action", 204
