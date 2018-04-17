import numpy as np
import pandas as pd
import datetime


def read_earthquake_data():
    df = pd.read_csv("../data/query.csv", header=0)
    A = df.as_matrix()
    time = A[:, 0]
    latitude = A[:, 1]
    longitude = A[:, 2]
    depth = A[:, 3]
    mag = A[:, 4]
    return time, latitude, longitude, depth, mag


def convert_time(time):
    converted_time = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
    return converted_time


def main():
    time, latitude, longitude, depth, mag = read_earthquake_data()
    time_list = np.empty(10)

    for each_time in time:
        np.append(time_list, convert_time(each_time))
        print(convert_time(each_time))


if __name__ == "__main__":
    main()
