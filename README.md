# Ultrasonic-Task
•In this storage, there is a python code that commands the robot to stop or continue 
based on the average of the data given by a robot's Ultrasonic sensor every 100 ms.

## collect_sensor_data

•this function collect the data from by using "input" functions and if user press "q" the collecting of data expire.
For each parameter entered after the user input 20 parameters, the parameters entered at the beginning are deleted one by one.

## calculate_average_distance
•This function Calculate average of the last 20 data points.

## navigate_robot
•This function could use the average distance to determine whether the robot should "Continue" or "Stop".
if average of distance bigger than 10 robot will continue otherwise robot will stop.

## run_robot_navigation
•this function display the result to user.

## Output

![result](https://github.com/OsmanErunali/Ultrasonic-Task/assets/109237631/8e9adb9e-ea5f-4ed8-a0e9-7726b04f1ee2)
