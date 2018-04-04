# import geoplotlib as gl
import urllib
import csv
import io
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        basicOptions = tk.Label(self, text="Basic Options").grid(row=0, column=1)

        magnitudeFrame = tk.Frame(self)
        magnitudeFrame.grid(row=1, column=0)

        magnitude = tk.Label(magnitudeFrame, text="Magnitude:").grid(row=0)
        magnitudeSize = tk.Label(magnitudeFrame, text="Note: -1 to 10", font=2).grid(row=1)
        mgList = tk.Spinbox(magnitudeFrame, from_=-1, to=10, state=tk.NORMAL)  # .grid(row=2, column=0)
        mgList.grid(row=2)

        dateTimeFrame = tk.Frame(self)
        dateTimeFrame.grid(row=1, column=1)

        dateTime = tk.Label(dateTimeFrame, text="Date & Time:").grid(row=0)

        startLabel = tk.Label(dateTimeFrame, text="Start (UTC)").grid(row=1)
        start_v = tk.StringVar(dateTimeFrame, value='2018-03-27 00:00:00')
        startEntery = tk.Entry(dateTimeFrame, textvariable=start_v).grid(row=2)

        end_v = tk.StringVar(dateTimeFrame, value='2018-04-03 23:59:59')
        endLabel = tk.Label(dateTimeFrame, text="End (UTC):").grid(row=3)
        endEntery = tk.Entry(dateTimeFrame, textvariable=end_v).grid(row=4)

        geographicRegionFrame = tk.Frame(self)
        geographicRegionFrame.grid(row=1, column=2)

        geographicRegion = tk.Label(geographicRegionFrame, text="Geographic Region:").grid(row=0)
        gREntery = tk.Entry(geographicRegionFrame, text="enter ..").grid(row=1)

        visButton = tk.Button(self, text="Visualize")
        visButton.grid(row=3, column=1)
        visButton.bind("<Button-1>", self.test)

        self.pack()

    def test(self, event):
        data = self.csv_import(
            'https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2018-03-01&endtime=2018-04-01')
        print(next(data))

        # geoplotlib.dot(data)
        # geoplotlib.show()

    def csv_import(self, url):
        url_open = urllib.request.urlopen(url)
        csvfile = csv.reader(io.StringIO(url_open.read().decode('utf-8')), delimiter=',')
        return csvfile


# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("Visualization of Epic Earthquakes")
myapp.master.minsize(300, 300)
myapp.master.maxsize(1000, 1000)

# start the program
myapp.mainloop()
