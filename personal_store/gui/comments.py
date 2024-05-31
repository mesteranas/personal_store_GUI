from settings import app
import requests
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Comments(qt.QDialog):
    def __init__(self,p,itemID):
        super().__init__(p)
        self.itemID=itemID
        self.setWindowTitle(_("comments"))
        self.commentsList={}
        layout=qt.QVBoxLayout(self)
        r=requests.post(app.link + "/en/api/comments",data={"pk":itemID})
        self.commentsList=r.json()
        self.commentsBox=qt.QListWidget()
        for comment in self.commentsList:
            self.commentsBox.addItem(comment["content"] + " by " + comment["user"])
        layout.addWidget(self.commentsBox)