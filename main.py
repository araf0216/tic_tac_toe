from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sys


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, bo, rounter, app, MainWindow, c_pl, pl_n):
        super(Ui_MainWindow, self).__init__()
        self.navhov = False
        self.setMouseTracking(True)
        self.gS_l = ["Started", "Won", "Draw"]
        self.c_gS = self.gS_l[0]
        self.omp = None

        self.setupUi(bo, rounter, app, MainWindow, c_pl, pl_n)
        self.label.mousePressEvent = self.mousePressEvent
        self.label.mouseMoveEvent = self.mouseMoveEvent
        self.label.mouseReleaseEvent = self.mouseReleaseEvent

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.buttons() == QtCore.Qt.LeftButton:
            self.omp = e.pos()

    def mouseMoveEvent(self, e: QtGui.QMouseEvent):
        if e.buttons() == QtCore.Qt.LeftButton:
            MainWindow.move(e.globalPos() - self.omp)

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.buttons() == QtCore.Qt.LeftButton:
            self.omp = None

    def setupUi(self, bo, rounter, app, MainWindow, c_pl, pl_n):
        self.cc_p = c_pl
        self.cpl_n = pl_n
        self._tr = app.translate
        _translate = self._tr
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 619)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Frame = QtWidgets.QFrame(self.centralwidget)
        self.Frame.setGeometry(QtCore.QRect(0, 0, 710, 621))
        self.Frame.setStyleSheet("QFrame {\n" "background-color:rgb(0, 0, 47);\n" "}")
        self.Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame.setLineWidth(1)
        self.Frame.setObjectName("Frame")
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
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 710, 32))
        font = QtGui.QFont()
        font.setFamily("Oxygen")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "color: white;\n" "background-color: rgb(20, 20, 47);\n"
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.Frame)
        self.pushButton.setGeometry(QtCore.QRect(630, 10, 10, 10))
        self.pushButton.setStyleSheet(
            "background-color: rgb(0, 255, 0);\n" "border-radius: 5px;\n"
        )
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        if "" == "".join(bo.values()):
            self.pushButton.clicked.connect(self.reset)
            self.label.setText(_translate("MainWindow", "Player: " + c_pl))
        else:
            self.pushButton.clicked.connect(self.reconf_pop)
        self.pushButton.installEventFilter(self)
        self.pushButton_2 = QtWidgets.QPushButton(self.Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 10, 10, 10))
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(255, 255, 0);\n" "border-radius: 5px\n;"
        )
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(MainWindow.showMinimized)
        self.pushButton_2.installEventFilter(self)
        self.pushButton_3 = QtWidgets.QPushButton(self.Frame)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 10, 10, 10))
        self.pushButton_3.setStyleSheet(
            "background-color: rgb(255, 0, 0);\n" "border-radius: 5px\n;"
        )
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(sys.exit)
        self.pushButton_3.installEventFilter(self)
        font = QtGui.QFont()
        font.setFamily("Oxygen")
        font.setPointSize(16)
        self.line = QtWidgets.QFrame(self.Frame)
        self.line.setGeometry(QtCore.QRect(70, 240, 574, 4))
        self.line.setStyleSheet(
            "background-color: white;\n" "color: white;\n" "border-color: white;"
        )
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.Frame)
        self.line_2.setGeometry(QtCore.QRect(70, 384, 574, 4))
        self.line_2.setStyleSheet(
            "background-color: white;\n" "color: white;\n" "border-color: white;"
        )
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.Frame)
        self.line_3.setGeometry(QtCore.QRect(258, 100, 4, 428))
        self.line_3.setStyleSheet(
            "background-color: white;\n" "color: white;\n" "border-color: white;"
        )
        self.line_3.setLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.Frame)
        self.line_4.setGeometry(QtCore.QRect(454, 100, 4, 428))
        self.line_4.setStyleSheet(
            "background-color: white;\n" "color: white;\n" "border-color: white;"
        )
        self.line_4.setLineWidth(0)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.push_button = QtWidgets.QPushButton(self.Frame)
        self.push_button.setGeometry(QtCore.QRect(70, 100, 188, 140))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button.setFont(font)
        self.push_button.setStyleSheet(
            "color: white;\n"
            "text-align: center;\n"
            "background-color: rgb(0, 0, 47);\n"
            "border: none;"
        )
        self.push_button.setObjectName("push_button")
        self.push_button_2 = QtWidgets.QPushButton(self.Frame)
        self.push_button_2.setGeometry(QtCore.QRect(262, 100, 192, 140))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_2.setFont(font)
        self.push_button_2.setStyleSheet(
            "color: white;\n"
            "text-align: center;\n"
            "background-color: rgb(0, 0, 47);\n"
            "border: none;"
        )
        self.push_button_2.setObjectName("push_button_2")
        self.push_button_3 = QtWidgets.QPushButton(self.Frame)
        self.push_button_3.setGeometry(QtCore.QRect(458, 100, 186, 140))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_3.setFont(font)
        self.push_button_3.setStyleSheet(
            "color: white;\n"
            "text-align: center;\n"
            "background-color: rgb(0, 0, 47);\n"
            "border: none;"
        )
        self.push_button_3.setObjectName("push_button_3")
        self.push_button_4 = QtWidgets.QPushButton(self.Frame)
        self.push_button_4.setGeometry(QtCore.QRect(70, 244, 188, 140))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_4.setFont(font)
        self.push_button_4.setStyleSheet(
            "color: white;\n"
            "text-align: center;\n"
            "background-color: rgb(0, 0, 47);\n"
            "border: none;"
        )
        self.push_button_4.setObjectName("push_button_4")
        self.push_button_5 = QtWidgets.QPushButton(self.Frame)
        self.push_button_5.setGeometry(QtCore.QRect(262, 244, 192, 140))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_5.setFont(font)
        self.push_button_5.setStyleSheet(
            "color: white;\n"
            "text-align: center;\n"
            "background-color: rgb(0, 0, 47);\n"
            "border: none;"
        )
        self.push_button_5.setObjectName("push_button_5")
        self.push_button_6 = QtWidgets.QPushButton(self.Frame)
        self.push_button_6.setGeometry(QtCore.QRect(458, 244, 186, 140))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_6.setFont(font)
        self.push_button_6.setStyleSheet(
            "color: white;\n"
            "text-align: center;\n"
            "background-color: rgb(0, 0, 47);\n"
            "border: none;"
        )
        self.push_button_6.setObjectName("push_button_6")
        self.push_button_7 = QtWidgets.QPushButton(self.Frame)
        self.push_button_7.setGeometry(QtCore.QRect(70, 388, 188, 140))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_7.setFont(font)
        self.push_button_7.setStyleSheet(
            "color: white;\n"
            "text-align: center;\n"
            "background-color: rgb(0, 0, 47);\n"
            "border: none;"
        )
        self.push_button_7.setObjectName("push_button_7")
        self.push_button_8 = QtWidgets.QPushButton(self.Frame)
        self.push_button_8.setGeometry(QtCore.QRect(262, 388, 192, 140))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_8.setFont(font)
        self.push_button_8.setStyleSheet(
            "color: white;\n"
            "text-align: center;\n"
            "background-color: rgb(0, 0, 47);\n"
            "border: none;"
        )
        self.push_button_8.setObjectName("push_button_8")
        self.push_button_9 = QtWidgets.QPushButton(self.Frame)
        self.push_button_9.setGeometry(QtCore.QRect(458, 388, 186, 140))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(72)
        self.push_button_9.setFont(font)
        self.push_button_9.setStyleSheet(
            "color: white;\n"
            "text-align: center;\n"
            "background-color: rgb(0, 0, 47);\n"
            "border: none;"
        )
        self.push_button_9.setObjectName("push_button_9")
        self.frame.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        ti_l = []
        self.push_button.raise_()
        ti_l.append(self.push_button)
        self.push_button_2.raise_()
        ti_l.append(self.push_button_2)
        self.push_button_3.raise_()
        ti_l.append(self.push_button_3)
        self.push_button_4.raise_()
        ti_l.append(self.push_button_4)
        self.push_button_5.raise_()
        ti_l.append(self.push_button_5)
        self.push_button_6.raise_()
        ti_l.append(self.push_button_6)
        self.push_button_7.raise_()
        ti_l.append(self.push_button_7)
        self.push_button_8.raise_()
        ti_l.append(self.push_button_8)
        self.push_button_9.raise_()
        ti_l.append(self.push_button_9)
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.retranslateUi(app, rounter, MainWindow, c_pl, pl_n, ti_l, bo)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def eventFilter(self, obj, event):
        _translate = self._tr
        nbs = [self.pushButton, self.pushButton_2, self.pushButton_3]
        if obj in nbs and event.type() == QtCore.QEvent.Enter:
            m = int(nbs.index(obj) * 30)
            self.navhov = True
            obj.setGeometry(QtCore.QRect(627 + m, 7, 16, 16))
            if obj == nbs[0]:
                self.label.setText(_translate("MainWindow", "Restart Game"))
                obj.setStyleSheet(
                    "background-color: rgb(0, 255, 0);\n"
                    "border-radius: 8px;\n"
                    "border-width: 2px;\n"
                    "border-color: white;\n"
                    "border-style: solid;\n"
                )
            elif obj == nbs[1]:
                self.label.setText(_translate("MainWindow", "Minimize"))
                obj.setStyleSheet(
                    "background-color: rgb(255, 255, 0);\n"
                    "border-radius: 8px;\n"
                    "border-width: 2px;\n"
                    "border-color: white;\n"
                    "border-style: solid;\n"
                )
            else:
                self.label.setText(_translate("MainWindow", "Close"))
                obj.setStyleSheet(
                    "background-color: rgb(255, 0, 0);\n"
                    "border-radius: 8px;\n"
                    "border-width: 2px;\n"
                    "border-color: white;\n"
                    "border-style: solid;\n"
                )
            return True
        elif obj in nbs and event.type() == QtCore.QEvent.Leave:
            m = int(nbs.index(obj) * 30)
            self.navhov = False
            obj.setGeometry(QtCore.QRect(630 + m, 10, 10, 10))
            if self.c_gS == self.gS_l[0]:
                self.label.setText(_translate("MainWindow", "Player: " + self.cc_p))
            elif self.c_gS == self.gS_l[1]:
                self.label.setText(
                    _translate(
                        "MainWindow", "Game Over!   Player " + self.cc_p + " Wins!"
                    )
                )
            elif self.c_gS == self.gS_l[2]:
                self.label.setText(
                    _translate(
                        "MainWindow",
                        "Draw! Both Players are Equally Good (or Equally Bad)!",
                    )
                )
            if obj == nbs[0]:
                obj.setStyleSheet(
                    "background-color: rgb(0, 255, 0);\n" "border-radius: 5px;\n"
                )
            elif obj == nbs[1]:
                obj.setStyleSheet(
                    "background-color: rgb(255, 255, 0);\n" "border-radius: 5px;\n"
                )
            else:
                obj.setStyleSheet(
                    "background-color: rgb(255, 0, 0);\n" "border-radius: 5px;\n"
                )
            return False
        else:
            return False

    # displaying the board and all the moves
    def retranslateUi(self, app, rounter, MainWindow, c_pl, pl_n, ti_l, bo, w_ts=None):
        _translate = self._tr
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        if rounter == "Game Over!":
            if type(w_ts) == str:
                self.label.setText(_translate("MainWindow", w_ts))
            elif type(w_ts) == list:
                self.label.setText(
                    _translate("MainWindow", "Game Over!    Player " + c_pl + " Wins!")
                )
                for tin in range(len(ti_l)):
                    if int(tin + 1) in w_ts:
                        ti_l[tin].setStyleSheet(
                            "background-color: white;\n"
                            "color: rgb(0, 0, 47);\n"
                            "text-align: center;\n"
                            "border: none\n"
                        )
                    ti_l[tin].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                    ti_l[tin].setDisabled(True)
        elif type(rounter) == int and rounter <= 9:
            self.label.setText(_translate("MainWindow", "Player: " + c_pl))

            # checking if the current tile is clicked or not
            def is_ti_clicked(ti, bo, rounter, c_pl, pl_n, ti_l, app, MainWindow):
                # getting the current state of the current tile
                bk = int(ti_l.index(ti) + 1)
                # setting the new state of the current tile
                ti.setText(_translate("MainWindow", bo[bk]))
                if bo[bk] == "":
                    ti.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                # updating the current state of the tile if clicked
                def upd():
                    if bo[bk] == "":
                        bo.update({bk: c_pl})
                        ti.setText(_translate("MainWindow", c_pl))
                        ti.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                        self.ch_end(bo, rounter, c_pl, pl_n, ti_l, app, MainWindow)

                ti.clicked.connect(upd)

            for ti in ti_l:
                is_ti_clicked(ti, bo, rounter, c_pl, pl_n, ti_l, app, MainWindow)

    # confirm resetting the board/game
    def reconf_pop(self):
        pop = QtWidgets.QMessageBox()
        pop.setWindowTitle("Confirm Reset")
        pop.setText("Clear the Board and Restart the Game?")
        pop.setStyleSheet("background-color: rgb(0, 0, 47);\n" "color: white;")
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        pop.setFont(font)
        pop.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        for b in pop.buttons():
            b.setStyleSheet(
                "background-color: white;\n"
                "color: rgb(0, 0, 47);\n"
                "border: none;\n"
                "padding: 2px 10px 2px 10px;\n"
            )
            b.setFont(font)
            if b.text() == "&No":
                pop.setDefaultButton(b)
        pop.buttonClicked.connect(self.pop_res)
        popex = pop.exec()

    def pop_res(self, res):
        if res.text() == "&Yes":
            self.reset()

    # clear and restart the board/game and switch player
    def reset(self):
        self.c_gS = self.gS_l[0]
        pl_n = self.cpl_n
        bo = {}
        for n in range(9):
            bo[n + 1] = ""
        main(bo, rounter, int(1 - pl_n), app, MainWindow)

    # checking for endgame (winner/stalemate)
    def ch_end(self, bo, rounter, c_pl, pl_n, ti_l, app, MainWindow):
        vl = list(bo.keys())

        def cols_match():
            a_cols = [k for k in vl[::3]]
            b_cols = [k for k in vl[1::3]]
            c_cols = [k for k in vl[2::3]]
            all_cols = [a_cols, b_cols, c_cols]
            p_matches = [
                (
                    all(bo[a_cols[0]] == bo[f_col] for f_col in a_cols)
                    and bo[a_cols[0]] != ""
                ),
                (
                    all(bo[b_cols[0]] == bo[f_col] for f_col in b_cols)
                    and bo[b_cols[0]] != ""
                ),
                (
                    all(bo[c_cols[0]] == bo[f_col] for f_col in c_cols)
                    and bo[c_cols[0]] != ""
                ),
            ]
            col_res = {
                "matches": (True in p_matches),
                "m_tis": None,
            }
            for e in range(len(p_matches)):
                if p_matches[e] == True:
                    col_res["m_tis"] = [c for c in all_cols[e]]
            return col_res

        def rows_match():
            f_rows = [row_vs for row_vs in vl[:3]]
            s_rows = [row_vs for row_vs in vl[3:6]]
            t_rows = [row_vs for row_vs in vl[6:9]]
            all_rows = [f_rows, s_rows, t_rows]
            p_matches = [
                (
                    all(bo[f_rows[0]] == bo[ff_row] for ff_row in f_rows)
                    and bo[f_rows[0]] != ""
                ),
                (
                    all(bo[s_rows[0]] == bo[fs_row] for fs_row in s_rows)
                    and bo[s_rows[0]] != ""
                ),
                (
                    all(bo[t_rows[0]] == bo[ft_row] for ft_row in t_rows)
                    and bo[t_rows[0]] != ""
                ),
            ]
            row_res = {
                "matches": (True in p_matches),
                "m_tis": None,
            }
            for e in range(len(p_matches)):
                if p_matches[e] == True:
                    row_res["m_tis"] = [r for r in all_rows[e]]
            return row_res

        def diags_match():
            ps_diags = [k for k in vl[2:7:2]]
            ns_diags = [k for k in vl[::4]]
            all_diags = [ps_diags, ns_diags]
            p_matches = [
                (
                    all(bo[ps_diags[0]] == bo[pdv] for pdv in ps_diags)
                    and bo[ps_diags[0]] != ""
                ),
                (
                    all(bo[ns_diags[0]] == bo[ndv] for ndv in ns_diags)
                    and bo[ns_diags[0]] != ""
                ),
            ]
            diag_res = {
                "matches": (True in p_matches),
                "m_tis": None,
            }
            for e in range(len(p_matches)):
                if p_matches[e] == True:
                    diag_res["m_tis"] = [r for r in all_diags[e]]
            return diag_res

        c = dict(cols_match())
        r = dict(rows_match())
        d = dict(diags_match())

        if c["matches"] or r["matches"] or d["matches"] or rounter >= 9:
            if c["matches"] or r["matches"] or d["matches"]:
                self.c_gS = self.gS_l[1]
                if c["matches"]:
                    w_ts = c["m_tis"]
                elif r["matches"]:
                    w_ts = r["m_tis"]
                elif d["matches"]:
                    w_ts = d["m_tis"]
            elif rounter == 9:
                self.c_gS = self.gS_l[2]
                w_ts = "Draw! Both Players are Equally Good (or Equally Bad)!"
            self.retranslateUi(
                app, "Game Over!", MainWindow, c_pl, pl_n, ti_l, bo, w_ts=w_ts
            )
        else:
            main(bo, rounter, int(1 - pl_n), app, MainWindow)


def main(bo, rounter, pl_n, app, MainWindow):
    pls = ["X", "O"]
    c_pl = pls[pl_n]

    rounter += 1

    ui = Ui_MainWindow(bo, rounter, app, MainWindow, c_pl, pl_n)
    MainWindow.show()


if __name__ == "__main__":
    # initializing the board
    board = {}
    for n in range(9):
        board[n + 1] = ""
    # initializing the round number
    rounter = 0

    # initializing random player (X/O)
    rng = random.randint(0, 1)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main(board, rounter, rng, app, MainWindow)
    sys.exit(app.exec_())