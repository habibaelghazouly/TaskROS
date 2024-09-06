#!/usr/bin/env python3
import  rclpy
from rclpy.node import Node

class check(Node):
    def __init__(self):
        super().__init__("node1")
        self.number = 0
        self.create_timer(1.0, self.check_even_odd)  

    def check_even_odd(self):
        if self.number % 2 == 0:
            self.get_logger().info(f'Number {self.number} is even')
        else:
            self.get_logger().info(f'Number {self.number} is odd')
        self.number += 1  

def main(args=None):
    rclpy.init(args=args)
    node1 = check()
    rclpy.spin(node1) 
    rclpy.shutdown()

if __name__ == "__main__":
    main()
