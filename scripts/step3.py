#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0
ini = 0

def cb1(message):
    global n
    n = message.data-6

def cb2(message):
    global ini
    ini = message.data

rospy.init_node('step3')
sub1 = rospy.Subscriber('step2', Int32, cb1)
sub2 = rospy.Subscriber('step2', Int32, cb2)
pub1 = rospy.Publisher('step3', Int32, queue_size=1)
pub2 = rospy.Publisher('step3', Int32, queue_size=1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    pub1.publish(n)
    pub2.publish(ini)
    rate.sleep()
