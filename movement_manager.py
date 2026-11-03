#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MovementManager(Node):
    def __init__(self):
        super().__init__('movement_manager')
        self.subscription = self.create_subscription(
            String,
            'movement_commands',
            self.command_callback,
            10
        )
        self.publisher_ = self.create_publisher(String, 'movement_state', 10)
        self.state = 'Idle'
        self.get_logger().info('Movement Manager Node Initialized')

    def command_callback(self, msg):
        command = msg.data
        self.get_logger().info(f'Received Command: "{command}"')
        if command == 'Start':
            self.state = 'Active'
            state_msg = String()
            state_msg.data = 'Active'
            self.publisher_.publish(state_msg)
            self.get_logger().info('Movement Manager: Activated')
        elif command == 'Stop':
            self.state = 'Idle'
            state_msg = String()
            state_msg.data = 'Idle'
            self.publisher_.publish(state_msg)
            self.get_logger().info('Movement Manager: Deactivated')
        else:
            self.get_logger().info(f'Unknown Command: "{command}"')


def main(args=None):
    rclpy.init(args=args)
    node = MovementManager()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
