#!/bin/bash

rm -rf ./fleetglue_package/build ./fleetglue_package/install ./fleetglue_package/log
rm -rf ./action_interface/build ./action_interface/install ./action_interface/log

colcon build --packages-select fleetglue_package action_interface

source ./install/setup.bash

ros2 launch fleetglue_package package_launch.py

