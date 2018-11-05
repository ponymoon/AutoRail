from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os, datetime
#os.path.dirname(os.path.realpath(__file__))
UpperDir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
UpperDirsrc = os.path.join(UpperDir,'src')
now = datetime.datetime.now()
nowDateYear = now.strftime('%Y')
nowDateMonth = now.strftime('%m')
nowDateDay = now.strftime('%d')
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 483)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(763, 483))
        MainWindow.setMaximumSize(QtCore.QSize(763, 483))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(UpperDirsrc,'File_Logo.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(21, 12, 191, 261))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(19, 26, 130, 48))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(os.path.join(UpperDirsrc,'Srt_logo.png')))
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.RailIDLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.RailIDLineEdit.setGeometry(QtCore.QRect(19, 161, 91, 31))
        self.RailIDLineEdit.setObjectName("RailIDLineEdit")
        self.RailPWLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.RailPWLineEdit.setGeometry(QtCore.QRect(19, 207, 91, 31))
        self.RailPWLineEdit.setObjectName("RailPWLineEdit")
        self.RailPWLineEdit.setEchoMode(QLineEdit().Password)
        self.RailLoginButton = QtWidgets.QPushButton(self.groupBox_2)
        self.RailLoginButton.setGeometry(QtCore.QRect(120, 198, 61, 41))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(11)
        self.RailLoginButton.setFont(font)
        self.RailLoginButton.setObjectName("RailLoginButton")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(162, 43, 21, 20))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(19, 80, 141, 50))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(os.path.join(UpperDirsrc,'Korail_logo.png')))
        self.label_3.setObjectName("label_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(162, 99, 21, 20))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(123, 168, 56, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(454, 18, 291, 421))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 10, 211, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(os.path.join(UpperDirsrc,'Rail_Logo.png')))
        self.label.setObjectName("label")
        self.UserAdmitButton = QtWidgets.QPushButton(self.groupBox)
        self.UserAdmitButton.setGeometry(QtCore.QRect(40, 160, 211, 31))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(12)
        self.UserAdmitButton.setFont(font)
        self.UserAdmitButton.setObjectName("UserAdmitButton")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 210, 272, 201))
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(229, 12, 201, 261))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(19, 40, 41, 21))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(19, 78, 51, 31))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(19, 117, 51, 41))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_3)
        self.dateEdit.setGeometry(QtCore.QRect(79, 39, 100, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(int(nowDateYear), int(nowDateMonth), int(nowDateDay)), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.StartPlacelineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.StartPlacelineEdit.setGeometry(QtCore.QRect(78, 75, 100, 31))
        self.StartPlacelineEdit.setObjectName("StartPlacelineEdit")
        self.ArrivePlacelineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.ArrivePlacelineEdit.setGeometry(QtCore.QRect(78, 122, 100, 31))
        self.ArrivePlacelineEdit.setObjectName("ArrivePlacelineEdit")
        self.InfoPushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.InfoPushButton.setGeometry(QtCore.QRect(40, 184, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.InfoPushButton.setFont(font)
        self.InfoPushButton.setObjectName("InfoPushButton")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(21, 282, 411, 101))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.ParsedcomboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.ParsedcomboBox.setGeometry(QtCore.QRect(10, 20, 391, 31))
        self.ParsedcomboBox.setObjectName("ParsedcomboBox")
        self.DelayComboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.DelayComboBox.setGeometry(QtCore.QRect(71, 68, 61, 22))
        self.DelayComboBox.setObjectName("DelayComboBox")
        self.DelayComboBox.addItem("")
        self.DelayComboBox.addItem("")
        self.DelayComboBox.addItem("")
        self.DelayComboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(13, 68, 51, 21))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.AutoStartButton = QtWidgets.QPushButton(self.groupBox_4)
        self.AutoStartButton.setGeometry(QtCore.QRect(227, 62, 81, 31))
        self.AutoStartButton.setObjectName("AutoStartButton")
        self.AutoFinishButton = QtWidgets.QPushButton(self.groupBox_4)
        self.AutoFinishButton.setGeometry(QtCore.QRect(321, 62, 81, 31))
        self.AutoFinishButton.setObjectName("AutoFinishButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(19, 390, 420, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(27, 410, 421, 23))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.progressBar.setFont(font)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 18))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuversion = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.menuversion.setFont(font)
        self.menuversion.setObjectName("menuversion")
        self.menuVersion = QtWidgets.QMenu(self.menuversion)
        self.menuVersion.setObjectName("menuVersion")
        self.menu = QtWidgets.QMenu(self.menuversion)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.actionHelp.setFont(font)
        self.actionHelp.setObjectName("actionHelp")
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action4 = QtWidgets.QAction(MainWindow)
        self.action4.setObjectName("action4")
        self.action5 = QtWidgets.QAction(MainWindow)
        self.action5.setObjectName("action5")
        self.action6 = QtWidgets.QAction(MainWindow)
        self.action6.setObjectName("action6")
        self.actionJRail_v1_1 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.actionJRail_v1_1.setFont(font)
        self.actionJRail_v1_1.setObjectName("actionJRail_v1_1")
        self.menuVersion.addAction(self.actionJRail_v1_1)
        self.menu.addAction(self.action1)
        self.menu.addAction(self.action2)
        self.menu.addAction(self.action3)
        self.menu.addAction(self.action4)
        self.menu.addAction(self.action5)
        self.menu.addSeparator()
        self.menu.addAction(self.action6)
        self.menuversion.addAction(self.menu.menuAction())
        self.menuversion.addAction(self.menuVersion.menuAction())
        self.menubar.addAction(self.menuversion.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JypAutoRail"))
        self.groupBox_2.setTitle(_translate("MainWindow", "열차접속"))
        self.RailLoginButton.setText(_translate("MainWindow", "로그인"))
        self.label_8.setText(_translate("MainWindow", "ID/PW"))
        self.UserAdmitButton.setText(_translate("MainWindow", "사용자 인증"))
        self.groupBox_3.setTitle(_translate("MainWindow", "INFO"))
        self.label_4.setText(_translate("MainWindow", "날짜"))
        self.label_5.setText(_translate("MainWindow", "출발지"))
        self.label_6.setText(_translate("MainWindow", "도착지"))
        self.InfoPushButton.setText(_translate("MainWindow", "입력"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Auto실행"))
        self.DelayComboBox.setItemText(0, _translate("MainWindow", "10초"))
        self.DelayComboBox.setItemText(1, _translate("MainWindow", "15초"))
        self.DelayComboBox.setItemText(2, _translate("MainWindow", "20초"))
        self.DelayComboBox.setItemText(3, _translate("MainWindow", "30초"))
        self.label_7.setText(_translate("MainWindow", "딜레이"))
        self.AutoStartButton.setText(_translate("MainWindow", "예매시작"))
        self.AutoFinishButton.setText(_translate("MainWindow", "처음으로"))
        self.menuversion.setTitle(_translate("MainWindow", "Help"))
        self.menuVersion.setTitle(_translate("MainWindow", "Version"))
        self.menu.setTitle(_translate("MainWindow", "설명"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.action1.setText(_translate("MainWindow", "1. 열차 선택후 로그인"))
        self.action2.setText(_translate("MainWindow", "2. 로그인 후 날짜와 출발, 도착입력"))
        self.action3.setText(_translate("MainWindow", "3. 입력 후 나오는 시간 확인후 딜레이 설정"))
        self.action4.setText(_translate("MainWindow", "4. 시작"))
        self.action5.setText(_translate("MainWindow", "5. 예매완료시 Telegram 전송, 종료"))
        self.action6.setText(_translate("MainWindow", "네트워크 환경에따라 동작이 중지될 수 있습니다."))
        self.actionJRail_v1_1.setText(_translate("MainWindow", "JRail_v1.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())