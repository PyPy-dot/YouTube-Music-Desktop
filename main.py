import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main import Ui_MainWindow


class YouTubeMusic(QMainWindow):
    def __init__(self):
        super(YouTubeMusic, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YouTubeMusic()
    window.show()

    sys.exit(app.exec_())