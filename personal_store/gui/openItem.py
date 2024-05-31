from .comments import Comments
from settings import app
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class ViewItem(qt.QDialog):
    def __init__(self,p,item):
        super().__init__(p)
        self.item=item
        self.setWindowTitle(item["name"])
        layout=qt.QVBoxLayout(self)
        self.summery=qt.QLabel(item["summery"])
        layout.addWidget(self.summery)
        self.image=qt.QLabel()
        self.image.setPixmap(qt1.QPixmap(app.link + item["image"]))
        layout.addWidget(self.image)
        self.mainPrice=qt.QLabel(str(item["price"]) + "$")
        layout.addWidget(self.mainPrice)
        self.availableItems=qt.QLabel(_("available items :") + str(item["itemsCount"]))
        layout.addWidget(self.availableItems)
        self.date=qt.QLabel(_("date :") + str(item["date"]))
        layout.addWidget(self.date)
        self.category=qt.QLabel(_("category :") + item["category"])
        layout.addWidget(self.category)
        self.description=qt.QPlainTextEdit()
        self.description.setReadOnly(True)
        self.description.setPlainText(item["description"])
        layout.addWidget(self.description)
        self.info=qt.QPlainTextEdit()
        self.info.setReadOnly(True)
        self.info.setPlainText(item["information"])
        layout.addWidget(self.info)
        self.comments=qt.QPushButton(_("comments"))
        self.comments.clicked.connect(lambda:Comments(self,item["id"]).exec())
        layout.addWidget(self.comments)