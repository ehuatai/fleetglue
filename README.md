# FleetGlue Take-Home Assessment
A small ROS application and a server. Node 1 queries the server for JSON, and creates an action client. Node 2 creates an action server which simply prints the received JSON. 

## Prerequisites
It is assumed you have ROS2 and Python3 installed and set up on your machine.

[See here for ROS2 details.](https://docs.ros.org/en/jazzy/index.html)

[See here for Python3 download.](https://www.python.org/downloads/)

Flask is needed to run the server: 
```bash
pip3 install flask
```
Note: ROS2 does not play well with Python virtual environments. Either ensure your virtual environment contains only Flask, and none of the ROS2 Python dependencies, or install Flask to the global environment (```sudo apt install python3-flask```).

## Usage
First, clone the repository:
```bash
git clone git@github.com:ehuatai/fleetglue.git
```

To run, simply execute the two start scripts from your terminal: 
```bash
cd fleetglue
./start_nodes.sh
./start_server.sh
```
```./start_nodes.sh``` cleans the directory, then builds and launches the ROS packages. ```./start_server.sh``` starts the Flask server on ```http://localhost:8000```. There is no GUI, only the API. 

It is recommended to run the scripts in separate terminals to be able to view the output of each. 

Nothing exciting will happen if the server receives no POST requests! ```send_post_requests.py``` is provided to easily send POST requests to the server:
```bash
python3 send_post_requests.py
```
Each request contains a short poem about a robot and a request ID. 

Simply press enter to send a POST request, and watch as the ROS nodes receive and print them. 