from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


def getCurrentDate():
    now = QDateTime.currentDateTime()
    return now.toUTC().toString()

def getBeforeCurrentDate():
    now = QDateTime.currentDateTime()
    # now.set
    return now.toUTC().toString()


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        main_layout = QGridLayout()
        self.setLayout(main_layout)

        title_label = QLabel('Welcome to Visualization of Epic Earthquakes')
        title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        title_label.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(title_label, 0, 1)

        magnitude_label = QLabel('Magnitude:')
        main_layout.addWidget(magnitude_label, 1, 0)

        sp = QSpinBox()
        sp.setRange(-1, 10)
        sp.setValue(-1)
        main_layout.addWidget(sp, 3, 0)

        date_time_label = QLabel('Date & Time:')
        main_layout.addWidget(date_time_label, 1, 1)

        date_time_label = QLabel('From:')
        main_layout.addWidget(date_time_label, 2, 1)

        yesterday = QDateTimeEdit()
        now = QDateTime.currentDateTime()
        now.addDays(-1)
        yesterday.setDateTime(now.toUTC())
        # some_date = QtCore.QDate(2011, 4, 22)  # Year, Month, Day

        main_layout.addWidget(yesterday, 3, 1)

        date_time_label = QLabel('To:')
        main_layout.addWidget(date_time_label, 4, 1)

        myDTE = QDateTimeEdit()
        myDTE.setDateTime(QDateTime.currentDateTime().toUTC())

        main_layout.addWidget(myDTE, 5, 1)

        geographic_region_label = QLabel('Geographic Region:')
        main_layout.addWidget(geographic_region_label, 1, 2)

        worldRadio = QRadioButton("World")
        main_layout.addWidget(worldRadio, 2, 2)

        worldRadio = QRadioButton("USA")
        main_layout.addWidget(worldRadio, 3, 2)

        button = QPushButton("Visualize")

        main_layout.addWidget(button, 6, 1)

        self.setMinimumSize(400, 400)

        self.setWindowTitle('Visualization of Epic Earthquakes')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
