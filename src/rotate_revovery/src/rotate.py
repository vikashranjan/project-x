#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import OccupancyGrid
PI = 3.1415926535897
MAX_ROT=5
rospy.init_node('robot_startup_recovery')

def rotate():
    #Starts a new node
    
    velocity_publisher = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)
    vel_msg = Twist()

    speed = 10
    angle = 360
    clockwise = True

    #Converting from angles to radians
    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360

    #We wont use linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    # Checking if our movement is CW or CCW
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)


    #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    velocity_publisher.unregister()
 

if __name__ == '__main__':
    ROT = 0
    while ROT < MAX_ROT and not rospy.is_shutdown():
        try:
            rospy.wait_for_message("/map", OccupancyGrid, 20)
            print("Exiting startup recovery")
            break
        except:
            ROT=ROT+1
            print("Rotate recovery as no map message received")
            rotate()

