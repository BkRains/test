# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ID_Number.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 421)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CreateId = QtWidgets.QPushButton(self.centralwidget)
        self.CreateId.setGeometry(QtCore.QRect(70, 219, 91, 23))
        self.CreateId.setObjectName("CreateId")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(81, 70, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(81, 99, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(81, 129, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(81, 159, 60, 16))
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(160, 99, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.Num = QtWidgets.QLineEdit(self.centralwidget)
        self.Num.setGeometry(QtCore.QRect(160, 159, 113, 20))
        self.Num.setObjectName("Num")
        self.man = QtWidgets.QRadioButton(self.centralwidget)
        self.man.setGeometry(QtCore.QRect(160, 129, 41, 16))
        self.man.setObjectName("man")
        self.woman = QtWidgets.QRadioButton(self.centralwidget)
        self.woman.setGeometry(QtCore.QRect(210, 129, 41, 16))
        self.woman.setObjectName("woman")
        self.province = QtWidgets.QComboBox(self.centralwidget)
        self.province.setGeometry(QtCore.QRect(160, 69, 121, 22))
        self.province.setObjectName("province")
        self.city = QtWidgets.QComboBox(self.centralwidget)
        self.city.setGeometry(QtCore.QRect(290, 69, 121, 22))
        self.city.setObjectName("city")
        self.county = QtWidgets.QComboBox(self.centralwidget)
        self.county.setGeometry(QtCore.QRect(420, 69, 121, 22))
        self.county.setObjectName("county")
        self.ShowId = QtWidgets.QTextBrowser(self.centralwidget)
        self.ShowId.setGeometry(QtCore.QRect(75, 250, 341, 91))
        self.ShowId.setObjectName("ShowId")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CreateId.setText(_translate("MainWindow", "生成身份证号"))
        self.label.setText(_translate("MainWindow", "城市选择："))
        self.label_2.setText(_translate("MainWindow", "出生时间："))
        self.label_3.setText(_translate("MainWindow", "    性别："))
        self.label_4.setText(_translate("MainWindow", "生成个数："))
        self.man.setText(_translate("MainWindow", "男"))
        self.woman.setText(_translate("MainWindow", "女"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

