import requests
import json

URL = "http://localhost:8000/api/post"


def send_request(input):
    try:
        context = json.dumps(input)  # Convert dict to json
    except:
        print("Invalid json!")

    r = requests.post(
        URL, json=context, headers={"Content-Type": "application/json"}
    )  # Send POST request to server
    print(f"Request status: {r.text} {r.status_code}")


def loop():
    poem = (
        "I'm a little robot, Shiny and tall, "
        + "Here is my laser, Here is my claw, "
        + "When I get all cranky, Sputter and cough, "
        + "Just flip the switch, And turn me off."
    )

    request_num = 0
    print("Press enter to begin sending requests. ", end="")
    inp = input()
    print("=============\n")
    while inp != "exit":  # Loop and sends requests, iterating request_num each time
        print(f"Request number: {request_num}")
        send_request({"request_num": request_num, "poem": poem})
        request_num += 1
        print("Next request? Press enter to send. ", end="")
        inp = input()
        print("=============\n")


if __name__ == "__main__":
    loop()
