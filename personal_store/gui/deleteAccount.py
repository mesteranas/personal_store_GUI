from settings import app,settings_handler
import requests
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Login(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("delete account"))
        layout=qt.QFormLayout(self) 
        self.password=qt.QLineEdit()
        self.password.setEchoMode(qt.QLineEdit.EchoMode.Password)
        layout.addRow(_("password"),self.password)
        self.deleteBTN=qt.QPushButton(_("delete account"))
        self.deleteBTN.clicked.connect(self.on_delete)
        layout.addWidget(self.deleteBTN)
    def on_delete(self):
        RData={"password":self.password.text(),"api":settings_handler.get("g","api")}
        r=requests.post(app.link + "/en/api/accounts/delete",data=RData)
        data=r.json()
        if data["code"]==0:
            settings_handler.set("g","api","")
            qt.QMessageBox.information(self,_("done"),_("deleted"))
        else:
            qt.QMessageBox.warning(self,_("error"),_("error"))
        self.close()
        