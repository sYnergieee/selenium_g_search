# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selenium_google.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from selenium_search import result
# from selenium_search_async import result


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(770, 570, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.number_imgs_input = QtWidgets.QTextEdit(self.centralwidget)
        self.number_imgs_input.setGeometry(QtCore.QRect(550, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.number_imgs_input.setFont(font)
        self.number_imgs_input.setObjectName("number_imgs_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 0, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignJustify |
                                QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(630, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.search_input = QtWidgets.QTextEdit(self.centralwidget)
        self.search_input.setGeometry(QtCore.QRect(60, 70, 821, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_input.setFont(font)
        self.search_input.setObjectName("search_input")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 150, 821, 411))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(320, 580, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.result_label.setFont(font)
        self.result_label.setObjectName("result_label")
        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(60, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.refresh_button.setFont(font)
        self.refresh_button.setObjectName("refresh_button")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(760, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "google_selenium_search"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.number_imgs_input.setPlaceholderText(
            _translate("MainWindow", "0"))
        self.label.setText(_translate(
            "MainWindow", "Maximum number of images for one category (some images may not be parsed)"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.search_input.setPlaceholderText(
            _translate("MainWindow", "Nature"))
        self.result_label.setText(_translate(
            "MainWindow", "Completed! Check response.json file"))
        self.refresh_button.setText(_translate("MainWindow", "Clear"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))


class Logic_FirstWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.refresh_button.clicked.connect(self.refresh)
        self.add_button.clicked.connect(self.add)
        self.delete_button.clicked.connect(self.delete)
        self.start_button.clicked.connect(self.start)
        self.number_imgs_input.setText('1')
        self.result_label.hide()

    def refresh(self):
        self.listWidget.clear()

    def add(self):
        self.listWidget.addItem(self.search_input.toPlainText())
        self.search_input.clear()

    def delete(self):
        self.listWidget.takeItem(self.listWidget.currentRow())

    def start(self):
        items = []
        for i in range(self.listWidget.count()):
            items.append(self.listWidget.item(i).text())
        if len(items) == 0:
            self.result_label.setText('                   Empty list')
            self.result_label.show()
        else:
            result(items, int(self.number_imgs_input.toPlainText()))
            self.result_label.show()
            self.listWidget.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Logic_FirstWindow()
    MainWindow.show()
    sys.exit(app.exec_())
