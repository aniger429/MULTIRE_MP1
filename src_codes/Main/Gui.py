import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QLabel, QAction, QFileDialog, QApplication, QHBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Add database', self)
        openFile.setShortcut('Ctrl+D')
        openFile.setStatusTip('Add database')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        hbox = QHBoxLayout(self)


        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('MULTIRE MP1')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')
            print (fname[0])

            # with f:
            #     data = f.read()
            #     self.textEdit.setText(data)

            pixmap = QPixmap("C:/Users/Regina/PycharmProjects/MULTIRE_MP1/src_codes/Images/1.jpg")

            lbl = QLabel(self)
            lbl.setPixmap(pixmap)

            hbox.addWidget(lbl)
            self.setLayout(hbox)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
#                              QLabel, QApplication)
# from PyQt5.QtGui import QPixmap
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         hbox = QHBoxLayout(self)
#         pixmap = QPixmap("C:/Users/Regina/PycharmProjects/MULTIRE_MP1/src_codes/Images/1.jpg")
#
#         lbl = QLabel(self)
#         lbl.setPixmap(pixmap)
#
#         hbox.addWidget(lbl)
#         self.setLayout(hbox)
#
#         self.move(300, 200)
#         self.setWindowTitle('Red Rock')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())