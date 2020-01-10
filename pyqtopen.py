import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip,
                             QPushButton, QMessageBox)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

#align center
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        self.resize(800, 700)
        
        #置中function
        self.center()

        self.setWindowTitle('Center')    
        self.show()

    #置中functio
    def center(self):
        
        #獲得window框架
        qr = self.frameGeometry()
        #獲得中間點
        cp = QDesktopWidget().availableGeometry().center()
        #置中
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

#關閉時的談窗
'''class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('Message box')    
        self.show()

    #如果關閉視窗會出現的event
    def closeEvent(self, event):
        #彈出視窗
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        
        #respone
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())'''

#關閉視窗
'''class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        qbtn = QPushButton('Quit', self)
        
        #click to close
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        
        #qbtn.sizeHint()默認button大小
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())'''

#帶圖標示窗
'''class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        #combine .move, .resize
        self.setGeometry(300, 300, 500, 220)
        self.setWindowTitle('Icon')
        #window 左上角的圖示
        self.setWindowIcon(QIcon('/ta-ju/peg/1.png'))        

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())'''
    
    
# 純開視窗    
'''if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    #windows size
    #w.resize(1920, 1080)
    
    #視窗出現在螢幕中的位置，沒打置中
    #w.move(500, 500)
    #title
    w.setWindowTitle('Simple')
    #open window
    w.show()

    sys.exit(app.exec_())'''