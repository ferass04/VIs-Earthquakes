from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.optionWidet = Options(self)
        self.setCentralWidget(self.optionWidet)

        self.statusbar = self.statusBar()
        # self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)

        self.setMinimumSize(300, 300)

        self.setWindowTitle('Visualization of Epic Earthquakes')

        self.show()

    def center(self):
        '''centers the window on the screen'''

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


class Options(QFrame):
    msg2Statusbar = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)

        self.initOptions()

    def initOptions(self):
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
        options_layout.addLayout(self.magnitude_layout())

        # create a layout for date and time options
        options_layout.addLayout(self.date_time_layout())

        options_layout.addLayout(self.region_layout())

        vis_button = QPushButton('Visualize')
        main_layout.addLayout(options_layout)
        main_layout.addWidget(vis_button)



    def magnitude_layout(self):
        mg_layout = QVBoxLayout()

        magnitude_label = QLabel('Magnitude:')
        mg_layout.addWidget(magnitude_label)

        sp = QSpinBox()
        sp.setRange(-1, 10)
        sp.setValue(-1)
        mg_layout.addWidget(sp)
        return mg_layout

    def date_time_layout(self):
        dt_layout = QVBoxLayout()

        date_time_label = QLabel('Date & Time:')
        dt_layout.addWidget(date_time_label)

        date_time_label = QLabel('From:')
        dt_layout.addWidget(date_time_label)

        yesterday = QDateTimeEdit()
        now = QDateTime.currentDateTime()
        now.addDays(-1)
        yesterday.setDateTime(now.toUTC())

        dt_layout.addWidget(yesterday)

        date_time_label = QLabel('To:')
        dt_layout.addWidget(date_time_label)

        myDTE = QDateTimeEdit()
        myDTE.setDateTime(QDateTime.currentDateTime().toUTC())

        dt_layout.addWidget(myDTE)

        return dt_layout

    def region_layout(self):
        rg_layout = QVBoxLayout()

        geographic_region_label = QLabel('Geographic Region:')
        rg_layout.addWidget(geographic_region_label)

        worldRadio = QRadioButton("World")
        rg_layout.addWidget(worldRadio)

        worldRadio = QRadioButton("USA")
        rg_layout.addWidget(worldRadio)

        return rg_layout


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
