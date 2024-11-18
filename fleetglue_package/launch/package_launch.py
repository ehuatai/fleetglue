#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="fleetglue_package",
                namespace="fleetglue",
                executable="rn1",
                name="node1",
            ),
            Node(
                package="fleetglue_package",
                namespace="fleetglue",
                executable="rn2",
                name="node2",
            ),
        ]
    )
