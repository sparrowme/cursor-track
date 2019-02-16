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
            print('got click')
            #self.drag_position = event.globalPos() - self.pos();
            self.app.quit()
        event.accept();

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        text = "Window => x: {0},  y: {1}".format(x, y)
        print(text)
        self.movie.setGeometry(e.x()-50,e.y()-50,100,100)
 #       self.movie.start()

class CustomMovie(QLabel):
    def __init__(self,window,file):
        super().__init__(window)
        window.movie=self
        movie=QMovie(file)
        self.setMovie(movie)
        pos=QCursor.pos()
        self.setGeometry(pos.x()-50,pos.y()-50,100,100)
        movie.start()
        self.setMouseTracking(True)
    def mouseMoveEvent(self, event):
        #x = e.x()
        #y = e.y()
        #text = "Movie => x: {0},  y: {1}".format(x, y)
        #print(text)
        #self.setGeometry(e.x()-50,e.y()-50,100,100)
        super(QLabel, self).mouseMoveEvent(event)
  #      self.start()
#gif
#moviee = QLabel(window)
#window.movie=moviee
#movie = QMovie("circle.gif")

#moviee.setMovie(movie)
#moviee.setGeometry(5,3,100,100)
#movie.start()

app = QApplication(sys.argv)

# Create the main window
window = CustomWindow(app)

window.setWindowFlags(Qt.FramelessWindowHint)
window.setAttribute(Qt.WA_NoSystemBackground, True)
window.setAttribute(Qt.WA_TranslucentBackground, True)
#window.clicked.connect(app.quit)

m=CustomMovie(window,"circle.gif")

# Create the button
#pushButton = QPushButton(window)
#pushButton.setGeometry(QRect(240, 190, 90, 31))
#pushButton.setText("Finished")
#pushButton.clicked.connect(app.quit)


# Center the button
#qr = pushButton.frameGeometry()
#cp = QDesktopWidget().availableGeometry().center()
#qr.moveCenter(cp)
#pushButton.move(qr.topLeft())

# Run the application
window.showFullScreen()
sys.exit(app.exec_())
