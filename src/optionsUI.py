import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qtpy import QtCore

from usgs import *
from earthquake_visualization import *
import dateutil.parser
from color_bar import *


class Options(QFrame):
    msg2_status_bar = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)

        self.max_sp = QSpinBox()
        self.min_sp = QSpinBox()
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

        min_label = QLabel('Minimum')
        mg_layout.addWidget(min_label)

        self.min_sp.setRange(0, 10)
        self.min_sp.setValue(3)
        mg_layout.addWidget(self.min_sp)
        options_layout.addLayout(mg_layout)

        max_label = QLabel('Maximum')
        mg_layout.addWidget(max_label)

        self.max_sp.setRange(-1, 10)
        self.max_sp.setValue(10)
        mg_layout.addWidget(self.max_sp)
        # options_layout.addLayout(mg_layout)

        # create a layout for date and time options
        dt_layout = QVBoxLayout()

        date_time_label = QLabel('Date & Time:')
        dt_layout.addWidget(date_time_label)

        date_time_label = QLabel('From:')
        dt_layout.addWidget(date_time_label)

        self.start_edit = QDateTimeEdit()
        self.start_edit.setDisplayFormat("MM/dd/yyyy hh:mm AP")

        # now = QDateTime.currentDateTime()
        start_time = QDateTime(QDate(2011, 2, 15), QTime(0, 0, 0))
        self.start_edit.setDateTime(start_time)

        dt_layout.addWidget(self.start_edit)

        date_time_label = QLabel('To:')
        dt_layout.addWidget(date_time_label)

        self.end_edit = QDateTimeEdit()
        self.end_edit.setDisplayFormat("MM/dd/yyyy hh:mm AP")

        end_time = QDateTime(QDate(2011, 6, 1), QTime(0, 0, 0))
        self.end_edit.setDateTime(end_time)

        dt_layout.addWidget(self.end_edit)
        options_layout.addLayout(dt_layout)

        # rg_layout = QVBoxLayout()

        # geographic_region_label = QLabel('Geographic Region:')
        # rg_layout.addWidget(geographic_region_label)
        #
        # worldRadio = QRadioButton("World")
        # rg_layout.addWidget(worldRadio)
        #
        # worldRadio = QRadioButton("USA")
        # rg_layout.addWidget(worldRadio)
        # options_layout.addLayout(rg_layout)

        vis_button = QPushButton('Visualize with Animation')
        vis_button.clicked.connect(self.button_clicked_animate)
        main_layout.addLayout(options_layout)
        main_layout.addWidget(vis_button)

        vis_button2 = QPushButton('Visualize All')
        vis_button2.clicked.connect(self.button_clicked_show_all)
        main_layout.addWidget(vis_button2)

        vis_button2 = QPushButton('See the Color Map')
        vis_button2.clicked.connect(self.show_colormap)
        main_layout.addWidget(vis_button2)

    def button_clicked_animate(self):
        start = dateutil.parser.parse(self.start_edit.dateTime().toString())
        end = dateutil.parser.parse(self.end_edit.dateTime().toString())

        usags = USAGS(self.min_sp.value(), self.max_sp.value(), str(start), str(end))
        if usags.request():
            graph(usags.content, True)
        else:
            self.showdialog()

    def button_clicked_show_all(self):
        start = dateutil.parser.parse(self.start_edit.dateTime().toString())
        end = dateutil.parser.parse(self.end_edit.dateTime().toString())

        usags = USAGS(self.min_sp.value(), self.max_sp.value(), str(start), str(end))
        if usags.request():
            graph(usags.content, False)
        else:
            self.showdialog()

    @staticmethod
    def show_colormap():
        get_colorscale()

    @staticmethod
    def showdialog():
        d = QDialog()
        b1 = QPushButton("ok", d)
        b1.move(120, 50)

        b1.clicked.connect(d.hide)
        d.setWindowTitle("Dialog")
        label = QLabel('The data is too big. Please try again with shorter length of time or magnitude', d)
        label.setGeometry(50, 0, 200, 50)
        label.setAlignment(QtCore.Qt.AlignCenter)

        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()

