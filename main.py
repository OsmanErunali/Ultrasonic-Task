data_list = []


def collect_sensor_data():
    # This function handles the task of receiving a single data point from the sensor and storing it.
    while True:
        data = input("Data from sensor (or 'q' to quit): ")
        if data.lower() == 'q':
            break
        data = int(data)
        data_list.append(data)
        if len(data_list) > 20:
            data_list.pop(0)
    return data_list


def calculate_average_distance():
    # This function is responsible for calculating the average of the last 20 data points.
    total = sum(data_list)
    count = len(data_list)
    # prevent ZeroDivisionError
    if count == 0:
        return 0
    else:
        average = total / count
        return average


def navigate_robot(threshold=10):
    # This function could use the average distance to determine whether the robot should "Continue" or "Stop".
    collect_sensor_data()
    average_distance = calculate_average_distance()
    if average_distance > threshold:
        return "continue"
    else:
        return "stop"


def run_robot_navigation():
    #this function is show the result to user
    result = navigate_robot()
    print("Robot should:", result)



run_robot_navigation()
print(calculate_average_distance())
