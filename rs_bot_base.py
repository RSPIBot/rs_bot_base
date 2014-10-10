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

    if (data.linear.x > 255):
	data.linear.x = 255
    motor.set_motor_speed(0, int(data.linear.x))
    #motor.set_motor_speed(1, int(data.linear.x))
    #motor.set_motor_speed(2, int(data.linear.x))
    #motor.set_motor_speed(3, int(data.linear.x))
    motor.change_motor_speed()

def listener():
    rospy.Subscriber("cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == "__main__":
    rospy.init_node('rs_bot_base')
    listener()
