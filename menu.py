import sys
import qrc_resources
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication, QLabel, QMenuBar, QToolBar,  qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Hakem Yardım Sistemi")
        self.resize(800, 600)
        self.centralWidget = QLabel("Hakem Yardım Sistemine Hoşgeldiniz")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self.createMenuBar()

    def createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        editMenu = menuBar.addMenu("&Edit")
        helpMenu = menuBar.addMenu(QIcon(":help-img.png"), "&Help")


    
    
    def informationText(self):
        print("Version 1.0")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())