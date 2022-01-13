#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data     

rospy.init_node('interruption')
sub = rospy.Subscriber('count_up', Int32, cb)
pub1 = rospy.Publisher('interruption', Int32, queue_size=1)
pub2 = rospy.Publisher('interruption', Int32, queue_size=1)
rate = rospy.Rate(2)
while not rospy.is_shutdown():
    pub1.publish(n)
    pub2.publish(-n)
    rate.sleep()
