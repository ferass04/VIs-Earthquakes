import requests
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import json
import csv


class Usags(object):
    URL = 'https://earthquake.usgs.gov/fdsnws/event/1/'

    def getTodayEQ(self, start_t, end_t):
        r = requests.get(
            self.URL + "query?format=geojson&starttime=" + start_t.toString() + "&endtime=" + end_t.toString())
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

        # print(data)

    def __init__(self):
        self.data = []
        # self.event


class Event(object):

    def __init__(self, event):
        self.data = event[0]
        self.latitude = event[1]
        self.longitude = event[2]
        self.depth = event[3]
        self.mag = event[4]
        self.magType = event[5]
        self.nst = event[6]
        self.gap = event[7]
        self.dmin = event[8]
        self.rms = event[9]
        self.net = event[10]
        self.id = event[11]
        self.updated = event[12]
        self.place = event[13]
        self.type = event[14]
        self.horizontalError = event[15]
        self.depthError = event[16]
        self.magError = event[17]
        self.magNst = event[18]
        self.status = event[19]
        self.locationSource = event[20]
        self.magSource = event[21]
