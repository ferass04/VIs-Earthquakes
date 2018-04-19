from optionsUI import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.status_bar = self.statusBar()
        self.option_widget = Options(self)
        self.init_ui()

    def init_ui(self):
        self.setCentralWidget(self.option_widget)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
