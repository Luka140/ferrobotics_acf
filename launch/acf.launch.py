from launch import LaunchDescription
from launch_ros.actions import Node

from itertools import product
import numpy as np 

import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    pkg = "ferrobotics_acf"
    ld = LaunchDescription()


    acf_node = Node(
        package='ferrobotics_acf',
        executable='acf.py',
        parameters=[
            {'ip': '169.254.200.17',
             'ramp_duration': 0.,
             'frequency': 120,
             'payload': 1.6,
             'control_p': 0.9,
             'control_i': 9 / 1000,
             'control_d': 30  / 1000,
             'f_max': 20
            }
        ]
    )

    ld.add_action(acf_node)
    return ld 


""" Seems to work decently well
            {'ip': '169.254.200.17',
             'ramp_duration': 0.,
             'frequency':120,
             'payload': 1.6,
             'control_p': 0.9,
             'control_i': 9 / 1000,
             'control_d': 30  / 1000,
             'f_max': 20}
"""