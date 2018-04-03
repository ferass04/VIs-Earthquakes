import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        basicOptions = tk.Label(self, text="Basic Options").grid(row=0, column=1)

        magnitude = tk.Label(self, text="Magnitude:").grid(row=1, column=0)
        magEntery = tk.Entry(self, text="enter ..").grid(row=1, column=1)

        geographicRegion = tk.Label(self, text="Geographic Region:").grid(row=2, column=0)
        gREntery = tk.Entry(self, text="enter ..").grid(row=2, column=1)

        self.pack()


# create the application
myapp = App()


#
# here are method calls to the window manager class
#
myapp.master.title("Visualization of Epic Earthquakes")
myapp.master.minsize(400,400)
myapp.master.maxsize(1000, 1000)

# start the program
myapp.mainloop()
