from settings import app,settings_handler
import requests
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Login(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("login"))
        self.p=p
        layout=qt.QFormLayout(self)
        self.username=qt.QLineEdit()
        layout.addRow(_("username"),self.username)
        self.password=qt.QLineEdit()
        self.password.setEchoMode(qt.QLineEdit.EchoMode.Password)
        layout.addRow(_("password"),self.password)
        self.loginBTN=qt.QPushButton(_("login"))
        self.loginBTN.clicked.connect(self.on_login)
        layout.addWidget(self.loginBTN)
    def on_login(self):
        r=requests.post(app.link + "/en/api/accounts/login",data={"username":self.username.text(),"password":self.password.text()})
        data=r.json()
        if data["code"]==0:
            settings_handler.set("g","api",data["token"])
            qt.QMessageBox.information(self,_("done"),_("loged in"))
        else:
            qt.QMessageBox.warning(self,_("error"),_("error"))
        self.close()
        