#! /usr/bin/python3
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CustomWindow(QMainWindow):
    movie=None
    def __init__(self,app=None):
        self.app=app
        super().__init__()
        self.setMouseTracking(True)

    def paintEvent(self, event=None):
        painter = QPainter(self)

        painter.setOpacity(0.0)
        painter.setBrush(Qt.white)
        painter.setPen(QPen(Qt.white))
        painter.drawRect(self.rect())
    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            #print('got click')
            self.app.quit()
        event.accept();

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        #text = "Window => x: {0},  y: {1}".format(x, y)
        #print(text)
        self.movie.setGeometry(e.x()-(self.movie.width/2),e.y()-(self.movie.height/2),self.movie.width,self.movie.height)

class CustomMovie(QLabel):
    def __init__(self,window,file,width,height):
        super().__init__(window)
        self.width=width
        self.height=height
        window.movie=self
        movie=QMovie(file)
        self.setMovie(movie)
        pos=QCursor.pos()
        self.setGeometry(pos.x()-(width/2),pos.y()-(height/2),width,height)
        movie.start()
        self.setMouseTracking(True)
    def mouseMoveEvent(self, event):
        #call super() if mouse is over the movie to get global coordinates
        super(QLabel, self).mouseMoveEvent(event)

app = QApplication(sys.argv)

# Create the main window
window = CustomWindow(app)

window.setWindowFlags(Qt.FramelessWindowHint)
window.setAttribute(Qt.WA_NoSystemBackground, True)
window.setAttribute(Qt.WA_TranslucentBackground, True)

m=CustomMovie(window,"circle.gif",100,100)

# Run the application
window.showFullScreen()
sys.exit(app.exec_())
