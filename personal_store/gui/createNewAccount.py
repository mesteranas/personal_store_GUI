import guiTools
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
        self.firstName=qt.QLineEdit()
        layout.addRow(_("first name"),self.firstName)
        self.lastName=qt.QLineEdit()
        layout.addRow(_("last name"),self.lastName)
        self.email=qt.QLineEdit()
        layout.addRow(_("email"),self.email)
        self.gender=qt.QComboBox()
        self.gender.addItems([_("male"),_("female")])
        layout.addRow(_("gender"),self.gender)
        self.country=qt.QComboBox()
        self.country.addItems(guiTools.dictionarys.countries)
        layout.addRow(_("country"),self.country)
        self.currency=qt.QComboBox()
        self.currency.addItems(guiTools.dictionarys.currencies)
        layout.addRow(_("currency"),self.currency)
        self.address=qt.QLineEdit()
        layout.addRow(_("address"),self.address)
        self.password=qt.QLineEdit()
        self.password.setEchoMode(qt.QLineEdit.EchoMode.Password)
        layout.addRow(_("password"),self.password)
        self.createBTN=qt.QPushButton(_("create"))
        layout.addWidget(self.create)