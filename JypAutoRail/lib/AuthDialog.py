import sys
from PyQt5.QtWidgets import *

class AuthDialog(QDialog,object):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.userKey = None

    def setupUI(self):
        self.setGeometry(700,400,300,100)
        self.setWindowTitle("Sign In")
        self.setFixedSize(300,100)

        label1 = QLabel("Key:")

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setEchoMode(QLineEdit().Password)

        self.pushButton = QPushButton("SerialKey 입력")
        self.pushButton.clicked.connect(self.submitLogin)

        layout = QGridLayout()
        layout.addWidget(label1,0,0)
        layout.addWidget(self.lineEdit1,0,1)
        layout.addWidget(self.pushButton,0,2)

        self.setLayout(layout)



    def submitLogin(self):
        self.userKey = self.lineEdit1.text()

        if self.userKey is None or self.userKey == '' or not self.userKey:
            QMessageBox.about(self,"인증오류","SerialKey를 입력하세요.")
            self.lineEdit1.setFocus(True)
            return None
        # 이 부분에서 필요한 경우 실제 로컬 DB 또는 서버 연동 후
        # 유저 정보 및 사용 유효기간을 체크하는 코드를 넣어주세요.
        # code
        # code
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UserAdmitDialog = AuthDialog()
    UserAdmitDialog.show()
    app.exec_()
