#!/usr/bin/python

from MotorClass import MotorClass
import time
import roslib;

roslib.load_manifest('rs_bot_base')
import rospy

from geometry_msgs.msg import Twist

motor = MotorClass()

def callback(data):
    #limit the values between -1 and 1 to have simular results as the turtlebot
    if (data.linear.x > 1.0):
        data.linear.x = 1.0
    if (data.linear.x < -1.0):
        data.linear.x = (-1.0)

    if (data.angular.z > 1.0):
        data.angular.z = 1.0
    if (data.angular.z < -1.0):
        data.angular.z = (-1.0)

	#scale the values back
    speed = data.linear.x * 255.0
    turnAngle = data.angular.z * 255.0

    rospy.loginfo(rospy.get_name() + " linear.x %f and angular.z %f", speed, turnAngle)


    wheelDistence = 11.0
    correction = 1.0
    #right = data.linear.x
    #left = data.linear.x
    #if (data.angular.z < 0):
    #    right = (data.angular.z*(-1))
    #    left = (data.angular.z)
    #    rospy.loginfo( "turn right left: %d and right: %d", left, right)
    #if (data.angular.z > 0):
    #    left = data.angular.z
    #    right = (data.angular.z*(-1))
    #    rospy.loginfo( "turn left left: %d and right: %d", left, right)

    right = speed + (2.0/wheelDistence)*(turnAngle) * correction
    left = speed - (2.0/wheelDistence)*(turnAngle) * correction

    motor.set_motor_speed(0, int(left))
    motor.set_motor_speed(1, int(right))
    motor.set_motor_speed(2, int(left))
    motor.set_motor_speed(3, int(right))
    motor.change_motor_speed()
    rospy.loginfo(rospy.get_name() + " right speed %f left speed %f", right, left)

def listener():
    rospy.Subscriber("cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == "__main__":
    rospy.init_node('rs_bot_base')
    listener()
