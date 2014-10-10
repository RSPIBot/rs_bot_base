#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================
class MotorClass:
    # Initialise the PWM device using the default address
    # bmp = PWM(0x40, debug=True)
    def __init__(self):
        pass

    m_pwm = PWM(0x40, debug=False)
    m_motors = 4

    m_motorAddress = [0, 1], [2, 3], [4, 5], [6, 7]

    # range from -255 to 255
    m_motorSpeed = [0, 0, 0, 0]
    m_motorMaxSpeed = 4095  # Min pulse length out of 4096
    m_motorOff = 0  # off

    def set_servo_pulse(self, channel, pulse):
        pulse_length = 1000000  # 1,000,000 us per second
        pulse_length /= 60  # 60 Hz
        print "%d us per period" % pulse_length
        pulse_length /= 4096  # 12 bits of resolution
        print "%d us per bit" % pulse_length
        pulse *= 1000
        pulse /= pulse_length
        self.m_pwm.setPWM(channel, 0, pulse)

    def set_motor_speed(self, motor, speed):
        # print "set speed %d" % speed
        # print "set speed motor %d" % motor
        if self.m_motors > motor >= 0 and -256 < speed < 256:
        #print "passed test speed is  %d" % self.m_motorSpeed[motor]
            self.m_motorSpeed[motor] = speed

    def change_motor_speed(self):
        self.m_pwm.setPWMFreq(60)
        i = 0
        while i < self.m_motors:
            # move forward
            if self.m_motorSpeed[i] >= 0:
                print "drive forward with speed %d" % self.m_motorSpeed[i]
                self.m_pwm.setPWM(((i * 2) - 2), 0, (self.m_motorMaxSpeed / 255) * self.m_motorSpeed[i])
                self.m_pwm.setPWM(((i * 2) - 1), 0, self.m_motorOff)
            else:
                # move back
                print "drive back with speed %d" % self.m_motorSpeed[i]
                self.m_pwm.setPWM(((i * 2) - 1), 0, (self.m_motorMaxSpeed / 255) * (self.m_motorSpeed[i] * (-1)))
                self.m_pwm.setPWM(((i * 2) - 2), 0, self.m_motorOff)
            i += 1

    def stop_motor(self):
        self.m_pwm.setPWMFreq(60)
        i = 0
        while i < self.m_motors:
            self.m_pwm.setPWM(((i * 2) - 2), 0, self.m_motorOff)
            self.m_pwm.setPWM(((i * 2) - 1), 0, self.m_motorOff)

            # m_pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
            # while(True):
            # Change speed of continuous servo on channel O
            # m_pwm.setPWM(0, 0, 0)
            # m_pwm.setPWM(1, 0, 0)
            # m_pwm.setPWM(2, 0, 0)
            #m_pwm.setPWM(3, 0, 0)
            #m_pwm.setPWM(4, 0, 0)
            #m_pwm.setPWM(5, 0, 0)
            #m_pwm.setPWM(6, 0, 0)
            #m_pwm.setPWM(7, 0, 0)
            #time.sleep(1)
            #pwm.setPWM(0, 0, servoMax)

# time.sleep(1)
