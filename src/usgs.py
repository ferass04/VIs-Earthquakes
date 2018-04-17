import requests
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import json
import csv
import pandas as pd
import io
import src.plotlt_bubble_map as t


class USAGS(object):
    URL = 'https://earthquake.usgs.gov/fdsnws/event/1/'

    def getTodayEQ(self, minmagnitude, maxmagnitude, start_t, end_t):

        r = requests.get(
            self.URL + "query?format=geojson&starttime=" + start_t.toString() + "&endtime=" + end_t.toString()
            + "&minmagnitude=" + minmagnitude + "&maxmagnitude=" + maxmagnitude)
        if (r.status_code == 200):
            with requests.Session() as s:
                download = s.get(
                    self.URL + "query?format=csv&starttime=" + start_t.toString() + "&endtime=" + end_t.toString())

                decoded_content = download.content.decode('utf-8')

                cr = csv.reader(decoded_content.splitlines(), delimiter=',')
                self.data = list(cr)
                self.events = []

                del self.data[0]

                for row in self.data:
                    self.events.append(Event(row))
                # for row in data:
                #     print(row)

        else:
            print("false")

    def request(self):
        r = requests.get(self.URL)
        self.content = r.content

        if r.status_code == 200:
            return True
        else:
            return False

    # initialize URL with range of time and magnitude
    def __init__(self, minmagnitude, maxmagnitude, start_t, end_t):
        self.URL += "query?format=csv&starttime=" + start_t + "&endtime=" + end_t + "&minmagnitude=" + str(minmagnitude) + "&maxmagnitude=" + str(maxmagnitude)
        self.URL = self.URL.replace(" ", "T")
        print(self.URL)

        self.content = None


class Event(object):

    def __init__(self, columns):
        self.data = columns[0]
        self.latitude = columns[1]
        self.longitude = columns[2]
        self.depth = columns[3]
        self.mag = columns[4]
        self.magType = columns[5]
        self.nst = columns[6]
        self.gap = columns[7]
        self.dmin = columns[8]
        self.rms = columns[9]
        self.net = columns[10]
        self.id = columns[11]
        self.updated = columns[12]
        self.place = columns[13]
        self.type = columns[14]
        self.horizontalError = columns[15]
        self.depthError = columns[16]
        self.magError = columns[17]
        self.magNst = columns[18]
        self.status = columns[19]
        self.locationSource = columns[20]
        self.magSource = columns[21]
