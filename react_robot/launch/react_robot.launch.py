import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    package_dir = get_package_share_directory('react_robot')
    urdf = os.path.join(package_dir, 'turtlebot3_burger.urdf.xacro')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='my_robot_state_publisher',
            output='screen',
            arguments=[urdf]),
    ])