from PyQt5 import QtCore, QtGui, QtWidgets


import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 619)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Frame = QtWidgets.QFrame(self.centralwidget)
        self.Frame.setGeometry(QtCore.QRect(0, 0, 711, 621))
        self.Frame.setStyleSheet(
            "QFrame {\n" "    background-color:rgb(0, 0, 47);\n" "}"
        )
        self.Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame.setLineWidth(1)
        self.Frame.setObjectName("Frame")
        self.pushButton = QtWidgets.QPushButton(self.Frame)
        self.pushButton.setGeometry(QtCore.QRect(630, 10, 10, 10))
        self.pushButton.setStyleSheet(
            "background-color: rgb(0, 255, 0);\n" "border-radius: 5;"
        )
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(MainWindow.showMinimized)
        self.pushButton_2 = QtWidgets.QPushButton(self.Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 10, 10, 10))
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(255, 255, 0);\n" "border-radius: 5;"
        )
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.showMax)
        self.pushButton_3 = QtWidgets.QPushButton(self.Frame)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 10, 10, 10))
        self.pushButton_3.setStyleSheet(
            "background-color: rgb(255, 0, 0);\n" "border-radius: 5;"
        )
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(sys.exit)
        self.frame = QtWidgets.QFrame(self.Frame)
        self.frame.setGeometry(QtCore.QRect(0, 0, 710, 32))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(20, 20, 47);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.push_button_25 = QtWidgets.QLabel(self.frame)
        self.push_button_25.setGeometry(QtCore.QRect(290, 0, 72, 32))
        font = QtGui.QFont()
        font.setFamily("Oxygen")
        font.setPointSize(16)
        self.push_button_25.setFont(font)
        self.push_button_25.setStyleSheet("color: white;")
        self.push_button_25.setAlignment(QtCore.Qt.AlignCenter)
        self.push_button_25.setIndent(0)
        self.push_button_25.setObjectName("label_25")
        self.push_button_26 = QtWidgets.QLabel(self.frame)
        self.push_button_26.setGeometry(QtCore.QRect(370, 0, 32, 32))
        font = QtGui.QFont()
        font.setFamily("Oxygen")
        font.setPointSize(16)
        self.push_button_26.setFont(font)
        self.push_button_26.setStyleSheet("color: white;")
        self.push_button_26.setAlignment(QtCore.Qt.AlignCenter)
        self.push_button_26.setIndent(0)
        self.push_button_26.setObjectName("label_26")
        self.push_button_27 = QtWidgets.QLabel(self.frame)
        self.push_button_27.setGeometry(QtCore.QRect(370, 0, 32, 32))
        font = QtGui.QFont()
        font.setFamily("Oxygen")
        font.setPointSize(16)
        self.push_button_27.setFont(font)
        self.push_button_27.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_27.setStyleSheet("color: white;")
        self.push_button_27.setAlignment(QtCore.Qt.AlignCenter)
        self.push_button_27.setIndent(0)
        self.push_button_27.setObjectName("label_27")
        self.line = QtWidgets.QFrame(self.Frame)
        self.line.setGeometry(QtCore.QRect(70, 240, 570, 4))
        self.line.setStyleSheet(
            "background-color: white;\n" "color: white;\n" "border-color: white;"
        )
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.Frame)
        self.line_3.setGeometry(QtCore.QRect(70, 380, 570, 4))
        self.line_3.setStyleSheet(
            "background-color: white;\n" "color: white;\n" "border-color: white;"
        )
        self.line_3.setLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.Frame)
        self.line_4.setGeometry(QtCore.QRect(251, 100, 4, 430))
        self.line_4.setStyleSheet(
            "background-color: white;\n" "color: white;\n" "border-color: white;"
        )
        self.line_4.setLineWidth(0)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.Frame)
        self.line_5.setGeometry(QtCore.QRect(460, 100, 4, 430))
        self.line_5.setStyleSheet(
            "background-color: white;\n" "color: white;\n" "border-color: white;"
        )
        self.line_5.setLineWidth(0)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.push_button = QtWidgets.QPushButton(self.Frame)
        self.push_button.setGeometry(QtCore.QRect(110, 120, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button.setFont(font)
        self.push_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button.setObjectName("label")
        self.push_button_2 = QtWidgets.QPushButton(self.Frame)
        self.push_button_2.setGeometry(QtCore.QRect(320, 120, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_2.setFont(font)
        self.push_button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_2.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_2.setObjectName("label_2")
        self.push_button_3 = QtWidgets.QPushButton(self.Frame)
        self.push_button_3.setGeometry(QtCore.QRect(510, 120, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_3.setFont(font)
        self.push_button_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_3.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_3.setObjectName("label_3")
        self.push_button_4 = QtWidgets.QPushButton(self.Frame)
        self.push_button_4.setGeometry(QtCore.QRect(110, 260, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_4.setFont(font)
        self.push_button_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_4.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_4.setObjectName("label_4")
        self.push_button_5 = QtWidgets.QPushButton(self.Frame)
        self.push_button_5.setGeometry(QtCore.QRect(320, 260, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_5.setFont(font)
        self.push_button_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_5.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_5.setObjectName("label_5")
        self.push_button_6 = QtWidgets.QPushButton(self.Frame)
        self.push_button_6.setGeometry(QtCore.QRect(510, 260, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_6.setFont(font)
        self.push_button_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_6.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_6.setObjectName("label_6")
        self.push_button_7 = QtWidgets.QPushButton(self.Frame)
        self.push_button_7.setGeometry(QtCore.QRect(110, 400, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_7.setFont(font)
        self.push_button_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_7.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_7.setObjectName("label_7")
        self.push_button_8 = QtWidgets.QPushButton(self.Frame)
        self.push_button_8.setGeometry(QtCore.QRect(320, 400, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_8.setFont(font)
        self.push_button_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_8.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_8.setObjectName("label_8")
        self.push_button_9 = QtWidgets.QPushButton(self.Frame)
        self.push_button_9.setGeometry(QtCore.QRect(510, 400, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_9.setFont(font)
        self.push_button_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_9.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_9.setObjectName("label_9")
        self.push_button_10 = QtWidgets.QPushButton(self.Frame)
        self.push_button_10.setGeometry(QtCore.QRect(110, 120, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_10.setFont(font)
        self.push_button_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_10.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_10.setObjectName("label_10")
        self.push_button_11 = QtWidgets.QPushButton(self.Frame)
        self.push_button_11.setGeometry(QtCore.QRect(320, 120, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_11.setFont(font)
        self.push_button_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_11.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_11.setObjectName("label_11")
        self.push_button_12 = QtWidgets.QPushButton(self.Frame)
        self.push_button_12.setGeometry(QtCore.QRect(510, 120, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_12.setFont(font)
        self.push_button_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_12.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_12.setObjectName("label_12")
        self.push_button_13 = QtWidgets.QPushButton(self.Frame)
        self.push_button_13.setGeometry(QtCore.QRect(110, 260, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_13.setFont(font)
        self.push_button_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_13.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_13.setObjectName("label_13")
        self.push_button_14 = QtWidgets.QPushButton(self.Frame)
        self.push_button_14.setGeometry(QtCore.QRect(320, 260, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_14.setFont(font)
        self.push_button_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_14.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_14.setObjectName("label_14")
        self.push_button_15 = QtWidgets.QPushButton(self.Frame)
        self.push_button_15.setGeometry(QtCore.QRect(510, 260, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_15.setFont(font)
        self.push_button_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_15.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_15.setObjectName("label_15")
        self.push_button_16 = QtWidgets.QPushButton(self.Frame)
        self.push_button_16.setGeometry(QtCore.QRect(110, 400, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_16.setFont(font)
        self.push_button_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_16.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_16.setObjectName("label_16")
        self.push_button_17 = QtWidgets.QPushButton(self.Frame)
        self.push_button_17.setGeometry(QtCore.QRect(320, 400, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_17.setFont(font)
        self.push_button_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_17.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_17.setObjectName("label_17")
        self.push_button_18 = QtWidgets.QPushButton(self.Frame)
        self.push_button_18.setGeometry(QtCore.QRect(510, 400, 80, 90))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_18.setFont(font)
        self.push_button_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_18.setStyleSheet(
            "color: white;\n" "text-align: center;\n" "background-color: rgb(0, 0, 47);"
        )
        self.push_button_18.setObjectName("label_18")
        self.frame.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.line.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.push_button.raise_()
        self.push_button_2.raise_()
        self.push_button_3.raise_()
        self.push_button_4.raise_()
        self.push_button_5.raise_()
        self.push_button_6.raise_()
        self.push_button_7.raise_()
        self.push_button_8.raise_()
        self.push_button_9.raise_()
        self.push_button_10.raise_()
        self.push_button_11.raise_()
        self.push_button_12.raise_()
        self.push_button_13.raise_()
        self.push_button_14.raise_()
        self.push_button_15.raise_()
        self.push_button_16.raise_()
        self.push_button_17.raise_()
        self.push_button_18.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.push_button_25.setText(_translate("MainWindow", "Player:"))
        self.push_button_26.setText(_translate("MainWindow", "X"))
        self.push_button_27.setText(_translate("MainWindow", "O"))
        self.push_button.setText(_translate("MainWindow", ""))

        def label_clicked():
            self.push_button.setText(_translate("MainWindow", "X"))

        self.push_button_2.setText(_translate("MainWindow", ""))

        def label_2_clicked():
            self.push_button_2.setText(_translate("MainWindow", "X"))

        self.push_button_3.setText(_translate("MainWindow", ""))

        def label_3_clicked():
            self.push_button_3.setText(_translate("MainWindow", "X"))

        self.push_button_4.setText(_translate("MainWindow", ""))

        def label_4_clicked():
            self.push_button_4.setText(_translate("MainWindow", "X"))

        self.push_button_5.setText(_translate("MainWindow", ""))

        def label_5_clicked():
            self.push_button_5.setText(_translate("MainWindow", "X"))

        self.push_button_6.setText(_translate("MainWindow", ""))

        def label_6_clicked():
            self.push_button_6.setText(_translate("MainWindow", "X"))

        self.push_button_7.setText(_translate("MainWindow", ""))

        def label_7_clicked():
            self.push_button_7.setText(_translate("MainWindow", "X"))

        self.push_button_8.setText(_translate("MainWindow", ""))

        def label_8_clicked():
            self.push_button_8.setText(_translate("MainWindow", "X"))

        self.push_button_9.setText(_translate("MainWindow", ""))

        def label_9_clicked():
            self.push_button_9.setText(_translate("MainWindow", "X"))

        self.push_button_10.setText(_translate("MainWindow", ""))

        def label_10_clicked():
            self.push_button_10.setText(_translate("MainWindow", "O"))

        self.push_button_11.setText(_translate("MainWindow", ""))

        def label_11_clicked():
            self.push_button_11.setText(_translate("MainWindow", "O"))

        self.push_button_12.setText(_translate("MainWindow", ""))

        def label_12_clicked():
            self.push_button_12.setText(_translate("MainWindow", "O"))

        self.push_button_13.setText(_translate("MainWindow", ""))

        def label_13_clicked():
            self.push_button_13.setText(_translate("MainWindow", "O"))

        self.push_button_14.setText(_translate("MainWindow", ""))

        def label_14_clicked():
            self.push_button_14.setText(_translate("MainWindow", "O"))

        self.push_button_15.setText(_translate("MainWindow", ""))

        def label_15_clicked():
            self.push_button_15.setText(_translate("MainWindow", "O"))

        self.push_button_16.setText(_translate("MainWindow", ""))

        def label_16_clicked():
            self.push_button_16.setText(_translate("MainWindow", "O"))

        self.push_button_17.setText(_translate("MainWindow", ""))

        def label_17_clicked():
            self.push_button_17.setText(_translate("MainWindow", "O"))

        self.push_button_18.setText(_translate("MainWindow", ""))

        def label_18_clicked():
            self.push_button_18.setText(_translate("MainWindow", "O"))

        self.push_button.clicked.connect(label_clicked)
        self.push_button_2.clicked.connect(label_2_clicked)
        self.push_button_3.clicked.connect(label_3_clicked)
        self.push_button_4.clicked.connect(label_4_clicked)
        self.push_button_5.clicked.connect(label_5_clicked)
        self.push_button_6.clicked.connect(label_6_clicked)
        self.push_button_7.clicked.connect(label_7_clicked)
        self.push_button_8.clicked.connect(label_8_clicked)
        self.push_button_9.clicked.connect(label_9_clicked)
        self.push_button_10.clicked.connect(label_10_clicked)
        self.push_button_11.clicked.connect(label_11_clicked)
        self.push_button_12.clicked.connect(label_12_clicked)
        self.push_button_13.clicked.connect(label_13_clicked)
        self.push_button_14.clicked.connect(label_14_clicked)
        self.push_button_15.clicked.connect(label_15_clicked)
        self.push_button_16.clicked.connect(label_16_clicked)
        self.push_button_17.clicked.connect(label_17_clicked)
        self.push_button_18.clicked.connect(label_18_clicked)

    def showMax(self):
        if MainWindow.isMaximized():
            MainWindow.showNormal()
        else:
            MainWindow.showMaximized()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
