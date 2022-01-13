#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0
ini = 0

def cb(message):
    global n
    n =(message.data+4)*2

rospy.init_node('step1')
sub = rospy.Subscriber('count_up1', Int32, cb)
pub = rospy.Publisher('step1', Int32, queue_size=1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    pub.publish(n)
    rate.sleep()
