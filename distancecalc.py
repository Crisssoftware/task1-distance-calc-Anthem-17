import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float64

class TurtleDistance(Node): #create new class
	
	def __init__(self):
		super().__init__('turtle_distance') #calls const of Node and names it

		#subscribe to /turtle1/pose
		self.subscription = self.create_subscription(
			Pose,'/turtle1/pose', self.turtleposi_callback, 10) #subscriber object

		#publish to /turtle1/distance_from_origin
		self.publisher = self.create_publisher(
			Float64, '/turtle1/distance_from_origin', 10)


	def turtleposi_callback(self, msg):
		x = msg.x
		y = msg.y

		d = (x**2 + y**2)
		distance = d**(1/2)

		msg = Float64()
		msg.data = distance
		self.publisher.publish(msg)

		self.get_logger().info(f'x coord: {x:.2f}, y coord: {y:.2f}, Distance from origin: {distance:.2f}')



def main(args=None):
	rclpy.init(args=args)

	turtle_distance = TurtleDistance()

	rclpy.spin(turtle_distance)

	turtle_distance.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()







