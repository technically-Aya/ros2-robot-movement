#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MovementSubscriber(Node):
    def __init__(self):
        super().__init__('movement_subscriber')
        
        
        self.subscription = self.create_subscription(
            String,
            'movement_commands',
            self.listener_callback,
            10)
        
        
        
        self.state_subscription = self.create_subscription(
            String,
            'movement_state',
            self.state_callback,
            10)
            
        self.state = 'Idle'
        self.get_logger().info('Movement Subscriber Node Initialized')

    def listener_callback(self, msg):
        command = msg.data
        self.get_logger().info(f'Received Command: "{command}"')
        
        
        if self.state == 'Active':
            if command == 'Move Forward':
                self.move_forward()
            elif command == 'Move Backward':
                self.move_backward()
            elif command == 'Turn Left':
                self.turn_left()
            elif command == 'Turn Right':
                self.turn_right()
            elif command == 'Stop':
                self.stop()
            else:
                self.get_logger().info(f'Unknown Command: "{command}"')
        else:
            self.get_logger().info('Movement Subscriber is Idle. No action taken')

    def state_callback(self, msg):
        self.state = msg.data

        self.get_logger().info(f'State Updated to: "{self.state}"')

    def move_forward(self):
        self.get_logger().info('Robot is moving forward.')

    def move_backward(self):
        self.get_logger().info('Robot is moving backward.')

    def turn_left(self):
        self.get_logger().info('Robot is turning left.')


    def turn_right(self):
        self.get_logger().info('Robot is turning right.')

    def stop(self):
        self.get_logger().info('Robot has stopped.')


def main(args=None):
    rclpy.init(args=args)
    node = MovementSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
