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


