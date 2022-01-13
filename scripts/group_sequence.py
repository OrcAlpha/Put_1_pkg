#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0
def cb(message):
    global n
    n = message.data
                
rospy.init_node('sequence')
sub = rospy.Subscriber('count_up', Int32, cb)
pub = rospy.Publisher('sequence', Int32, queue_size=1)
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    for i in range(n):
        pub.publish(n)
        rate.sleep()
