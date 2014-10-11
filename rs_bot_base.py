#!/usr/bin/python

from MotorClass import MotorClass
import time
import roslib;

roslib.load_manifest('rs_bot_base')
import rospy

from geometry_msgs.msg import Twist

motor = MotorClass()

def callback(data):
    rospy.loginfo(rospy.get_name() + " linear.x %d linear.y %d linear.z %d", data.linear.x, data.linear.y,
                  data.linear.z)
    rospy.loginfo(rospy.get_name() + " angular.x %d angular.y %d angular.z %d", data.angular.x, data.angular.y,
                  data.angular.z)

    if (data.linear.x > 254):
		data.linear.x = 254
    if (data.linear.x < -254):
		data.linear.x = (-254)

	if (data.angular.z > 254):
		data.angular.z = 254
    if (data.angular.z < -254):
		data.angular.z = (-254)
		
	right = data.linear.x
	if (data.angular.z < 0)
		right - data.angular.z
	left = data.linear.x
	if (data.angular.z > 0)
		left - data.angular.z
	
    motor.set_motor_speed(0, int(right))
    motor.set_motor_speed(1, int(right))
    motor.set_motor_speed(2, int(left))
    motor.set_motor_speed(3, int(left))
    motor.change_motor_speed()

def listener():
    rospy.Subscriber("cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == "__main__":
    rospy.init_node('rs_bot_base')
    listener()
