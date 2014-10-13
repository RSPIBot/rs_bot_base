#!/usr/bin/python

from MotorClass import MotorClass
import time
import roslib;

roslib.load_manifest('rs_bot_base')
import rospy

from geometry_msgs.msg import Twist

motor = MotorClass()

def callback(data):
    rospy.loginfo(rospy.get_name() + " linear.x %d and angular.z %d", data.linear.x, data.angular.z)

    if (data.linear.x > 254):
        data.linear.x = 254
    if (data.linear.x < -254):
        data.linear.x = (-254)

    if (data.angular.z > 254):
        data.angular.z = 254
    if (data.angular.z < -254):
        data.angular.z = (-254)
		
    right = data.linear.x
    left = data.linear.x
    if (data.angular.z < 0):
        right = (data.angular.z*(-1))
        left = (data.angular.z)
        rospy.loginfo( "turn right left: %d and right: %d", left, right)
    if (data.angular.z > 0):
        left = data.angular.z
        right = (data.angular.z*(-1))
        rospy.loginfo( "turn left left: %d and right: %d", left, right)
	
    motor.set_motor_speed(0, int(left))
    motor.set_motor_speed(1, int(right))
    motor.set_motor_speed(2, int(left))
    motor.set_motor_speed(3, int(right))
    motor.change_motor_speed()

def listener():
    rospy.Subscriber("cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == "__main__":
    rospy.init_node('rs_bot_base')
    listener()
