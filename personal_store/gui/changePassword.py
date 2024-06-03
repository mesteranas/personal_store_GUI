from settings import app,settings_handler
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
        self.changeBTN.clicked.connect(self.on_change)
        layout.addWidget(self.changeBTN)
    def on_change(self):
        if self.newPassword.text()==self.confNewPassword.text():
            r=requests.post(app.link + "/en/api/accounts/changePassword",data={"currentPassword":self.currentPassword.text(),"newPassword":self.newPassword.text(),"api":settings_handler.get("g","api")})
            data=r.json()
            if data["code"]==0:
                qt.QMessageBox.information(self,_("done"),_("password changed"))
            else:
                qt.QMessageBox.warning(self,_("error"),_("error"))
            self.close()
        