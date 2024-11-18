# FleetGlue Take-Home Assessment
A small ROS application and a server. Node 1 queries the server for JSON, and creates an action client. Node 2 creates an action server which simply prints the received JSON. 

## Prerequisites
It is assumed you have ROS2 installed and set up on your machine: [See here for details.](https://docs.ros.org/en/jazzy/index.html)

Flask is needed to run the server: 
```bash
pip3 install flask
```

Then, to run, simply run the two start scripts: 
```bash
./start_nodes.sh
./start_server.sh
```

It is recommended to run them in separate terminals to view the output of each. 

Nothing exciting will happen if the server receives no POST requests! ```send_post_requests.py``` is provided to easily send POST requests to the server:
```bash
python3 send_post_requests.py
```

Simply press enter to send a POST request, and watch as the ROS nodes receive and print them. 