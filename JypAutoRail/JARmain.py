import sys, os, io, re, datetime, time, telegram, threading
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl, QThread
from PyQt5 import uic
from lib.JypAutoRailLayOut import Ui_MainWindow
from lib.AuthDialog import AuthDialog
from lib.RailAuto import RailAutoTest
from tinydb import TinyDB
import datetime
from PyQt5.QtMultimedia import QSound
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)
lock = threading.Lock()
db = TinyDB(os.path.join(os.path.abspath(os.path.dirname(__file__)),'db','database.db'),default_table='log')
log = db.table('log')
#form_class = uic.loadUiType("C:/Mydocument/ComputerStudy/practice/JypAutoRail/ui")[0]

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #초기화
        self.setupUi(self)
        #초기 잠금
        self.initAuthLock()
        #시그널 초기화
        self.initSignal()
        self.createobj()
        #로그인 관련 변수 선언
        self.userKey = None
        self.RailKey = None
        self.bot = telegram.Bot(token='111111')    #Jyp Bot 토큰 / bot을 선언합니다.
        self.chat_id = 111111
        self.al_total = 1
        self.counter = 1

    def closeEvent(self,event):
        self.RAobj.driver.quit()
        db.close()
        event.accept()

    def initAuthLock(self):
        self.radioButton.setEnabled(False)
        self.radioButton_2.setEnabled(False)
        self.RailIDLineEdit.setEnabled(False)
        self.RailPWLineEdit.setEnabled(False)
        self.RailLoginButton.setEnabled(False)
        self.dateEdit.setEnabled(False)
        self.StartPlacelineEdit.setEnabled(False)
        self.ArrivePlacelineEdit.setEnabled(False)
        self.InfoPushButton.setEnabled(False)
        self.AutoStartButton.setEnabled(False)
        self.AutoFinishButton.setEnabled(False)
        self.showStatusMsg('인증안됨')

    #기본 UI 활성화
    def initAuthActive(self):
        self.radioButton.setEnabled(True)
        self.radioButton_2.setEnabled(True)
        self.RailIDLineEdit.setEnabled(True)
        self.RailPWLineEdit.setEnabled(True)
        self.UserAdmitButton.setText("인증완료")
        self.UserAdmitButton.setEnabled(False)
        self.RailIDLineEdit.setFocus(True)

    #시그널 초기화
    def initSignal(self):
        self.UserAdmitButton.clicked.connect(self.authCheck)
        self.radioButton.clicked.connect(self.railchoice)
        self.radioButton_2.clicked.connect(self.railchoice)
        self.RailLoginButton.clicked.connect(self.RailLogin)
        self.InfoPushButton.clicked.connect(self.RailParsing)
        self.AutoStartButton.clicked.connect(self.RailAuto)
        self.AutoFinishButton.clicked.connect(self.replay)

    def createobj(self):
        self.RAobj = RailAutoTest()
        self.RAobj.add_al.connect(self.add_progressbar)
        self.RAobj.add_al_2.connect(self.add_progressbar)
        self.RAobj.add_al_3.connect(self.add_progressbar)
        self.RAobj.sleepsig.connect(self.add_status_progress)

    def showStatusMsg(self,msg):
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')
        nowTime = now.strftime('%H:%M:%S')
        app_msg = msg + '    -    (' +nowDate+' '+nowTime+ ')'
        self.statusbar.showMessage(app_msg)
        log.insert({'Date': nowDate, 'log': msg+' ['+nowTime+']'})

    def add_progressbar(self,addal_val):
        for i in range(addal_val):
            setval = self.al_total + i
            self.progressBar.setValue(setval)
        self.al_total += addal_val

    def add_status_progress(self,count):
        delaymsg = "딜레이시간 대기중...   ["+str(self.counter)+"회 시도]"
        self.counter += count
        self.showStatusMsg(delaymsg)

    def soundplay(self,soundfile):
        self.intro = QSound(os.path.join(os.path.abspath(os.path.dirname(__file__)),'src',soundfile))
        self.intro.play()

    @pyqtSlot()
    def authCheck(self):
        self.soundplay('click.wav')
        dlg = AuthDialog()
        dlg.exec_()
        self.userKey = dlg.userKey
        # 이 부분에서 필요한 경우 실제 로컬 DB 또는 서버 연동 후
        # 유저 정보 및 사용 유효기간을 체크하는 코드를 넣어주세요.
        if True: #self.userKey == "gmlsenddl":
            self.initAuthActive()
            self.showStatusMsg('사용자 인증 완료')
            self.soundplay('start.wav')
        else:
            QMessageBox.about(self, "인증오류", "SerialKey 인증 오류")
            self.showStatusMsg('사용자 인증 실패')

    @pyqtSlot()
    def railchoice(self):
        self.RailLoginButton.setEnabled(True)
        self.soundplay('click.wav')
        if self.radioButton.isChecked():
            self.RailKey = 1
            self.showStatusMsg('Srt 선택')
        else:
            self.RailKey = 2
            self.showStatusMsg('Korail 선택')

    @pyqtSlot()
    def RailLogin(self):
        lock.acquire()
        try:
            self.progressBar.setValue(0)
            self.al_total = 1
            start_time = time.time()
            self.RailID = self.RailIDLineEdit.text().strip()
            self.RailPW = self.RailPWLineEdit.text().strip()
            if self.RailKey == 1:
                self.RASRTobj = self.RAobj.SrtRailAuto(self.RailID,self.RailPW)
                if next(self.RASRTobj):
                    spendtime = round(time.time() - start_time,2)
                    spendtimemsg = 'Srt 로그인 확인 소요시간 : '+str(spendtime)+'초'
                    self.showStatusMsg(spendtimemsg)
                    self.dateEdit.setEnabled(True)
                    self.StartPlacelineEdit.setEnabled(True)
                    self.ArrivePlacelineEdit.setEnabled(True)
                    self.InfoPushButton.setEnabled(True)
                    self.radioButton.setEnabled(False)
                    self.radioButton_2.setEnabled(False)
                    self.RailIDLineEdit.setEnabled(False)
                    self.RailPWLineEdit.setEnabled(False)
                    self.RailLoginButton.setText("인증됨")
                    self.RailLoginButton.setEnabled(False)
                else:
                    self.showStatusMsg('Srt 로그인 실패')
                    QMessageBox.about(self, "Srt 로그인 실패", "아이디 또는 비밀번호 인증 오류")
                    self.createobj()
            else:
                self.RAKOobj = self.RAobj.KorailAuto(self.RailID,self.RailPW)
                if next(self.RAKOobj):
                    spendtime = round(time.time() - start_time,2)
                    spendtimemsg = 'Korail 로그인 확인 소요시간 : '+str(spendtime)+'초'
                    self.showStatusMsg(spendtimemsg)
                    self.dateEdit.setEnabled(True)
                    self.StartPlacelineEdit.setEnabled(True)
                    self.ArrivePlacelineEdit.setEnabled(True)
                    self.InfoPushButton.setEnabled(True)
                    self.radioButton.setEnabled(False)
                    self.radioButton_2.setEnabled(False)
                    self.RailIDLineEdit.setEnabled(False)
                    self.RailPWLineEdit.setEnabled(False)
                    self.RailLoginButton.setText("인증됨")
                    self.RailLoginButton.setEnabled(False)
                else:
                    self.showStatusMsg('Korail 로그인 실패')
                    QMessageBox.about(self, "Korail 로그인 실패", "아이디 또는 비밀번호 인증 오류")
                    self.createobj()
        except Exception as ex:
            QMessageBox.about(self,"Error Message",ex)
        finally:
            lock.release()

    @pyqtSlot()
    def RailParsing(self):
        lock.acquire()
        try:
            self.progressBar.setValue(0)
            self.al_total = 1
            start_time = time.time()
            self.RailStartplace = self.StartPlacelineEdit.text().strip()
            self.RailArriveplace = self.ArrivePlacelineEdit.text().strip()
            self.TripDate = self.dateEdit.text().strip()
            hangul = re.compile('[가-힣]+')
            parsevar = (self.RailStartplace,self.RailArriveplace,self.TripDate)
            if hangul.match(self.RailStartplace) is not None:
                pass
            else:
                QMessageBox.about(self,"출발지형식오류","올바른 한글 형식이 아닙니다.")
                self.StartPlacelineEdit.clear()
                self.StartPlacelineEdit.setFocus(True)
            if hangul.match(self.RailArriveplace) is not None:
                if self.RailKey == 1:
                    RailParsed = self.RASRTobj.send(parsevar)
                    if RailParsed is not False:
                        for q in RailParsed:
                            self.ParsedcomboBox.addItem(q)
                        spendtime = round(time.time() - start_time,2)
                        spendtimemsg = 'Srt 파싱 소요시간 : '+str(spendtime)+'초'
                        self.showStatusMsg(spendtimemsg)
                        self.dateEdit.setEnabled(False)
                        self.StartPlacelineEdit.setEnabled(False)
                        self.ArrivePlacelineEdit.setEnabled(False)
                        self.InfoPushButton.setEnabled(False)
                        self.AutoStartButton.setEnabled(True)
                        self.AutoFinishButton.setEnabled(True)
                    else:
                        QMessageBox.about(self,"예외발생","Error Message")
                else:
                    RailParsed = self.RAKOobj.send(parsevar)
                    if RailParsed is not False:
                        for q in RailParsed:
                            self.ParsedcomboBox.addItem(q)
                        spendtime = round(time.time() - start_time,2)
                        spendtimemsg = 'Korail 파싱 소요시간 : '+str(spendtime)+'초'
                        self.showStatusMsg(spendtimemsg)
                        self.dateEdit.setEnabled(False)
                        self.StartPlacelineEdit.setEnabled(False)
                        self.ArrivePlacelineEdit.setEnabled(False)
                        self.InfoPushButton.setEnabled(False)
                        self.AutoStartButton.setEnabled(True)
                        self.AutoFinishButton.setEnabled(True)
                    else:
                        QMessageBox.about(self,"예외발생","Error Message")
            else:
                QMessageBox.about(self,"도착지형식오류","올바른 한글 형식이 아닙니다.")
                self.ArrivePlacelineEdit.clear()
                self.ArrivePlacelineEdit.setFocus(True)
        except Exception as ex:
            QMessageBox.about(self,"Error Message",ex)
        finally:
            lock.release()

    @pyqtSlot()
    def RailAuto(self):
        lock.acquire()
        try:
            self.progressBar.setValue(0)
            self.al_total = 1
            start_time = time.time()
            self.ParsedcomboBox.setEnabled(False)
            self.DelayComboBox.setEnabled(False)
            message = self.ParsedcomboBox.currentText()
            delay = self.DelayComboBox.currentText().replace('초','')
            if self.RailKey == 1:
                if self.RASRTobj.send(self.ParsedcomboBox.currentIndex()):
                    spendtime = round(time.time() - start_time,2)
                    spendtimemsg = 'Srt 자동예매 및 텔레그램 메세지 전송완료.  소요시간 : '+str(spendtime)+'초, 시도횟수 : '+str(self.counter)
                    self.bot.sendMessage(chat_id=self.chat_id, text= message+' Srt 자동예약완료 - 바로결제하세요')
                    self.showStatusMsg(spendtimemsg)
                    self.AutoStartButton.setEnabled(False)
                    self.soundplay('start.wav')
                else:
                    threading.Timer(int(delay),self.RailAuto).start()
            else:
                if self.RAKOobj.send(self.ParsedcomboBox.currentIndex()):
                    spendtime = round(time.time() - start_time,2)
                    spendtimemsg = 'Korail 자동예매 및 텔레그램 메세지 전송완료.  소요시간 : '+str(spendtime)+'초, 시도횟수 : '+str(self.counter)
                    self.bot.sendMessage(chat_id=self.chat_id, text= message+' Korail 자동예약완료 - 바로결제하세요')
                    self.showStatusMsg(spendtimemsg)
                    self.AutoStartButton.setEnabled(False)
                    self.soundplay('start.wav')
                else:
                    threading.Timer(int(delay),self.RailAuto).start()

        except Exception as ex:
            QMessageBox.about(self,"Error Message",ex)
        finally:
            lock.release()

    @pyqtSlot()
    def replay(self):
        self.ParsedcomboBox.clear()
        self.ArrivePlacelineEdit.clear()
        self.StartPlacelineEdit.clear()
        self.RailIDLineEdit.clear()
        self.RailPWLineEdit.clear()
        self.radioButton.setEnabled(True)
        self.radioButton_2.setEnabled(True)
        self.RailIDLineEdit.setEnabled(True)
        self.RailPWLineEdit.setEnabled(True)
        self.RailLoginButton.setText("로그인")
        self.RailLoginButton.setEnabled(True)
        self.ParsedcomboBox.setEnabled(True)
        self.DelayComboBox.setEnabled(True)
        self.AutoStartButton.setEnabled(False)
        self.AutoFinishButton.setEnabled(False)
        self.createobj()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    JypAutoRail_main = Main()
    JypAutoRail_main.show()
    sys.exit(app.exec_())
