from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from lib.share import ShareInfo
import sys


class LoginWindow:
    def __init__(self):
        self.ui = QUiLoader().load("login.ui")

        self.ui.pushButton.clicked.connect(self.CheckFace)

    def CheckFace(self):
        ShareInfo.Main_Window = MainWindow()
        ShareInfo.Main_Window.ui.show()
        ShareInfo.loginwindow.ui.close()


class MainWindow(QMainWindow):
    def __init__(self):
        self.ui = QUiLoader().load("main.ui")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ShareInfo.loginwindow = LoginWindow()
    ShareInfo.loginwindow.ui.show()
    sys.exit(app.exec_())
