#!/usr/bin/python

import rospy
from geometry_msgs.msg import Twist
from math import radians

def draw_star():
    rospy.init_node('draw_star_node', anonymous=True)
    rate = rospy.Rate(5)  # Tần số gửi message 5 Hz
    vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    #Nhập vào độ dài cạnh:
    edge = float(input("Nhập độ dài cạnh: "))
    # Biến đi thẳng
    vel_msg = Twist()
    vel_msg.linear.x = edge/10 # Tốc độ tuyến tính
    vel_msg.angular.z = 0
    # Biến quay đầu
    turn_msg = Twist()
    turn_msg.linear.x = 0
    turn_msg.angular.z = radians(-144/2) #144 độ/s
    while not rospy.is_shutdown():
        rospy.loginfo("Đi thẳng")
        for x in range(0,50):
            vel_pub.publish(vel_msg)
            rate.sleep()
        rospy.loginfo("Quay -144 độ")
        for x in range(0,10):
            vel_pub.publish(turn_msg)
            rate.sleep()

if __name__ == '__main__':
    try:
        draw_star()
    except rospy.ROSInterruptException:
        pass

