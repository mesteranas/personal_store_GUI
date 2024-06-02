from settings import app
import requests
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Login(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("login"))
        layout=qt.QFormLayout(self)
        self.username=qt.QLineEdit()
        layout.addRow(_("username"),self.username)
        self.password=qt.QLineEdit()
        self.password.setEchoMode(qt.QLineEdit.EchoMode.Password)
        layout.addRow(_("password"),self.password)
        self.loginBTN=q.QPushButton(_("login"))
        layout.addWidget(self.loginBTN)