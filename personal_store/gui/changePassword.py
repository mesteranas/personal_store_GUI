from settings import app
import requests
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Login(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("change password"))
        layout=qt.QFormLayout(self)
        self.currentPassword=qt.QLineEdit()
        self.currentPassword.setEchoMode(qt.QLineEdit.EchoMode.Password)
        layout.addRow(_("current password"),self.currentPassword)
        self.newPassword=qt.QLineEdit()
        self.newPassword.setEchoMode(qt.QLineEdit.EchoMode.Password)
        layout.addRow(_("new password"),self.newPassword)
        self.confNewPassword=qt.QLineEdit()
        self.confNewPassword.setEchoMode(qt.QLineEdit.EchoMode.Password)
        layout.addRow(_("confirm new password"),self.confNewPassword)
        self.changeBTN=qt.QPushButton(_("change password"))
        layout.addWidget(self.changeBTN)