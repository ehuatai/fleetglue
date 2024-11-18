#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
import requests

from action_interface.action import Print


class ROSNode(Node):
    def __init__(self):
        super().__init__("action_client")
        self.get_logger().info("Starting action_client node")

        self.timer = self.create_timer(1.0, self.fetch_actions)

        self.action_client = ActionClient(self, Print, "print_action")

    def fetch_actions(self):
        """
        Queries the GET endpoint of the api, checks for a valid response,
        and dispatches it to the action server.
        """

        self.get_logger().info("Querying server...")
        url = "http://localhost:8000/api/get"

        try:
            response = requests.get(url, headers={"Content-Type": "application/json"})
            if response.status_code == 200:  # Status OK, response received
                json_request = response.json()
                self.get_logger().info(f"New action received: {json_request}")
                self.send_goal(str(json_request))

            elif response.status_code == 204:  # Status OK, but no new response
                self.get_logger().info("No new action.")

            else:
                self.get_logger().info(
                    "Error fetching from endpoint."
                )  # Any other status code is invalid

        except:
            self.get_logger().info("No server connection.")

        

    def send_goal(self, json_request):
        """
        Creates an action and dispatches it to the action server
        """

        goal = Print.Goal()  # Custom action type
        goal.to_print = json_request

        self.action_client.wait_for_server()

        goal_future = self.action_client.send_goal_async(goal)
        goal_future.add_done_callback(
            self.goal_response_callback
        )  # Calls goal_response_callback on action acceptance

    def goal_response_callback(self, future):
        """
        Handles action acceptance and rejection.
        If accepted, handles result through result_callback
        """

        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected.")
            return

        self.get_logger().info("Goal accepted!")

        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.result_callback)

    def result_callback(self, future):
        """
        Prints result of action (True for success, False for failure)
        """

        result = future.result().result
        self.get_logger().info(f"Result: {result.complete}")


def main():
    rclpy.init()
    node = ROSNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
