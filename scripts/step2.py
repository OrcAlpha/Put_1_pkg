#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = (message.data-6)//2

rospy.init_node('step2')
sub1 = rospy.Subscriber('step1', Int32, cb)
pub = rospy.Publisher('step2', Int32, queue_size=1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    pub.publish(n)
    rate.sleep()
