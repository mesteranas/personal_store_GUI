import settings,gui
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Account(qt.QWidget):
    def __init__(self,p):
        super().__init__()
        layout=qt.QVBoxLayout(self)
        if settings.settings_handler.get("g","api")=="":
            self.login=qt.QPushButton(_("login"))
            self.login.clicked.connect(lambda:gui.login.Login(self).exec())
            layout.addWidget(self.login)
            self.createNewAccount=qt.QPushButton(_("create new account"))
            self.createNewAccount.clicked.connect(lambda:gui.createNewAccount.Login(self).exec())
            layout.addWidget(self.createNewAccount)
        else:
            self.logout=qt.QPushButton(_("logout"))
            self.logout.clicked.connect(lambda:settings.settings_handler.set("g","api",""))
            layout.addWidget(self.logout)
            self.editProfile=qt.QPushButton(_("edit profile"))
            self.editProfile.clicked.connect(lambda:gui.editProfile.Login(self).exec())
            layout.addWidget(self.editProfile)
            self.changePassword=qt.QPushButton(_("change password"))
            self.changePassword.clicked.connect(lambda:gui.changePassword.Login(self).exec())
            layout.addWidget(self.changePassword)
            self.delete=qt.QPushButton(_("delete account"))
            self.delete.clicked.connect(lambda:gui.deleteAccount.Login(self).exec())
            layout.addWidget(self.delete)