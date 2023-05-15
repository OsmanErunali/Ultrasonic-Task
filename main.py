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
