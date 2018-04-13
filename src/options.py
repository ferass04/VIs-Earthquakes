import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from src.usgs import *
from src.ploty import *



class Options(QFrame):
    msg2_status_bar = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)

        self.start_edit = QDateTimeEdit()
        self.end_edit = QDateTimeEdit()
        self.init_options()

    def init_options(self):
        # the main layout, using Grid
        main_layout = QVBoxLayout()
        # add the layout to main window
        self.setLayout(main_layout)

        # Main label
        title_label = QLabel('Welcome to Visualization of Epic Earthquakes')
        # made the main label centered and expanding
        title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        title_label.setAlignment(Qt.AlignCenter)

        # add the label to main layout
        main_layout.addWidget(title_label)

        # this layout will hold the three options
        options_layout = QHBoxLayout()

        # creating a layout for magnitude options
        mg_layout = QVBoxLayout()

        magnitude_label = QLabel('Magnitude:')
        mg_layout.addWidget(magnitude_label)

        sp = QSpinBox()
        sp.setRange(-1, 10)
        sp.setValue(-1)
        mg_layout.addWidget(sp)
        options_layout.addLayout(mg_layout)

        # create a layout for date and time options
        dt_layout = QVBoxLayout()

        date_time_label = QLabel('Date & Time:')
        dt_layout.addWidget(date_time_label)

        date_time_label = QLabel('From:')
        dt_layout.addWidget(date_time_label)

        self.start_edit = QDateTimeEdit()

        now = QDateTime.currentDateTime()
        start_time = now.addDays(-1).toUTC()
        self.start_edit.setDateTime(start_time)

        # self.start_edit.dateTimeChanged.connect(lambda: self.start_data_event())

        dt_layout.addWidget(self.start_edit)

        date_time_label = QLabel('To:')
        dt_layout.addWidget(date_time_label)

        self.end_edit = QDateTimeEdit()
        self.end_edit.setDateTime(now.toUTC())
        # self.end_edit.dateTimeChanged.connect(lambda: self.end_data_event())

        dt_layout.addWidget(self.end_edit)
        options_layout.addLayout(dt_layout)

        rg_layout = QVBoxLayout()

        geographic_region_label = QLabel('Geographic Region:')
        rg_layout.addWidget(geographic_region_label)

        worldRadio = QRadioButton("World")
        rg_layout.addWidget(worldRadio)

        worldRadio = QRadioButton("USA")
        rg_layout.addWidget(worldRadio)
        options_layout.addLayout(rg_layout);

        vis_button = QPushButton('Visualize')
        vis_button.clicked.connect(self.button_clicked)
        main_layout.addLayout(options_layout)
        main_layout.addWidget(vis_button)

    # def magnitude_layout(self):
    #     return mg_layout

    # def date_time_layout(self):
    #     return dt_layout

    def region_layout(self):
        rg_layout = QVBoxLayout()

        geographic_region_label = QLabel('Geographic Region:')
        rg_layout.addWidget(geographic_region_label)

        worldRadio = QRadioButton("World")
        rg_layout.addWidget(worldRadio)

        worldRadio = QRadioButton("USA")
        rg_layout.addWidget(worldRadio)

        return rg_layout

    def button_clicked(self):
        usags = Usags()
        usags.getTodayEQ(self.start_edit.dateTime(), self.end_edit.dateTime());

        for event in usags.events:
            print(event.id)

        test(usags.events)
        # data = read_csv('data/bus.csv')
        # geoplotlib.dot(data)
        # geoplotlib.show()


# if __name__ == '__main__':
