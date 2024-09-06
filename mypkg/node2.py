#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import random

class rndm(Node):
    def __init__(self):
        super().__init__('data_collector')
        self.create_timer(1.0, self.collect_data) 

    def collect_data(self):
        temperature = random.uniform(-10.0, 40.0)  
        pressure = random.uniform(950.0, 1050.0)  
        humidity = random.uniform(0.0, 100.0)     

        self.get_logger().info(f'Temperature: {temperature:.2f} °C, Pressure: {pressure:.2f} hPa, Humidity: {humidity:.2f}%')

def main(args=None):
    rclpy.init(args=args)
    node2 = rndm()
    rclpy.spin(node2) 
    rclpy.shutdown()

if __name__ == "__main__":
    main()
