#!/usr/bin/env python3
import message_filters
import rospy
from std_msgs.msg import Int32

n = 0
initial = 0

def cb1(message1):
    global n
    n = message1.data

def cb2(message2):
    global initial
    initial = message2.data

rospy.init_node('last')
sub1 = rospy.Subscriber('step2', Int32, cb1)
sub2 = rospy.Subscriber('count_up2', Int32, cb2)
pub = rospy.Publisher('last', Int32, queue_size=1)
rospy.ApproximateTimeSynchronizer([sub1, sub2], queue_size, delay)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    pub.publish(n-initial)
    rate.sleep()
