ON ROS Master

roslaunch turtlebot_bringup minimal.launch
roslaunch turtlebot_teleop keyboard_teleop.launch

roslaunch realsense2_camera rs_d400_and_t265.launch

for mapping
roslaunch realsense2_camera rs_d400_and_t265.launch

for navigation

rosrun depthimage_to_laserscan depthimage_to_laserscan image:=/d400/depth/image_rect_raw camera_info:/d400/depth/camera_info
roslaunch turtlebot_navigation amcl_d400_t265.launch map_file:=/home/nvidia/map_study.yaml

On Client
roslaunch turtlebot_rviz_launchers view_navigation.launch --screen
http://wiki.ros.org/turtlebot_navigation/Tutorials/Autonomously%20navigate%20in%20a%20known%20map

save map 
rosrun map_server map_saver map:=/occupancy -f map_home

Gmapping

roslaunch turtlebot_bringup minimal.launch
roslaunch turtlebot_teleop keyboard_teleop.launch
roslaunch realsense2_camera rs_rgbd.launch

rosrun depthimage_to_laserscan depthimage_to_laserscan image:=/camera/depth/image_rect_raw camera_info:/camera/depth/camera_info
roslaunch turtlebot_navigation gmapping_demo_d400.launch

rosrun map_server map_saver -f map
roslaunch turtlebot_navigation amcl_d400_t265.launch map_file:=/home/nvidia/map.yaml
On Client
roslaunch turtlebot_rviz_launchers view_navigation.launch --screen

RTABMAp
roslaunch rtab_nav rtab_nav.launch args:="--delete_db_on_start"
rosrun map_server map_saver map:=/rtabmap/proj_map –f my_map_1

Install
cd to src
run catkin_init_worspace
run sudo apt-get install ros-kinetic-tf2-bullet
run sudo apt-get install ros-kinetic-rtabmap-ros
sudo apt-get install ros-kinetic-kobuki
sudo apt-get install ros-kinetic-navigation
run catkin_make
run catkin_make install


rosrun map_server map_saver map:=/rtabmap/proj_map  --occ 1 --free 0.196 -f rtab
