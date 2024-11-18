#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
import requests

from action_interface.action import Print


class ROSNode(Node):
    def __init__(self):
        super().__init__("action_server")
        self.get_logger().info("Starting action_server node")

        self.action_server = ActionServer(
            self, Print, "print_action", self.execute_callback
        )

    def execute_callback(self, goal_handle):
        """
        Receives action and deals with it.
        First, sends feedback (simply a bool indicating acceptance)
        Second, prints action to log (thus completing the goal)
        """

        self.get_logger().info("Executing action...")
        to_print = goal_handle.request.to_print  # String to print

        feedback = Print.Feedback()
        feedback.currently_printing = to_print  # Not used
        feedback.accepted_print = True
        goal_handle.publish_feedback(
            feedback
        )  # Feedback loop, just prints the action request

        self.get_logger().info(to_print)  # Goal of the action
        goal_handle.succeed()
        result = Print.Result()
        result.complete = True  # Indicate goal complete
        return result


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
