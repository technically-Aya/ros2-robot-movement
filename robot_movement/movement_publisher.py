#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MovementPublisher(Node):
    def __init__(self):
        super().__init__('movement_publisher')
        self.publisher_ = self.create_publisher(String, 'movement_commands', 10)
        timer_period = 2 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Movement Publisher Node Initialized')

    def timer_callback(self):
        msg = String()
        msg.data = 'Move Forward'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = MovementPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

