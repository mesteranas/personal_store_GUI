import guiTools
from settings import app,settings_handler
import requests
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Login(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("edit profile"))
        r=requests.post(app.link + "/en/api/accounts/viewProfile",data={"api":settings_handler.get("g","api")})
        data=r.json()
        layout=qt.QFormLayout(self)
        self.firstName=qt.QLineEdit()
        self.firstName.setText(data["firstName"])
        layout.addRow(_("first name"),self.firstName)
        self.lastName=qt.QLineEdit()
        self.lastName.setText(data["lastName"])
        layout.addRow(_("last name"),self.lastName)
        self.email=qt.QLineEdit()
        self.email.setText(data["email"])
        layout.addRow(_("email"),self.email)
        self.country=qt.QComboBox()
        self.country.addItems(guiTools.dictionarys.countries)
        self.country.setCurrentText(data["country"])
        layout.addRow(_("country"),self.country)
        self.currency=qt.QComboBox()
        self.currency.addItems(guiTools.dictionarys.currencies)
        self.currency.setCurrentText(data["currency"])
        layout.addRow(_("currency"),self.currency)
        self.address=qt.QLineEdit()
        self.address.setText(data["address"])
        layout.addRow(_("address"),self.address)
        self.createBTN=qt.QPushButton(_("edit"))
        self.createBTN.clicked.connect(self.on_create)
        layout.addWidget(self.createBTN)
    def on_create(self):
        RData={"firstName":self.firstName.text(),"lastName":self.lastName.text(),"email":self.email.text(),"country":self.country.currentText(),"currency":self.currency.currentText(),"address":self.address.text(),"api":settings_handler.get("g","api")}
        r=requests.post(app.link + "/en/api/accounts/editProfile",data=RData)
        data=r.json()
        if data["code"]==0:
            qt.QMessageBox.information(self,_("done"),_("edited"))
        else:
            qt.QMessageBox.warning(self,_("error"),_("error"))
        self.close()
        