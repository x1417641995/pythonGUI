import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMenu
from PyQt5.QtGui import QIcon


#main
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('/ta-ju/peg/2.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# 工具欄
'''class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        exitAct = QAction(QIcon('/ta-ju/peg/1.png'), 'Exit2', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        
        #show 工具欄
        self.toolbar = self.addToolBar('Exit2')
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())'''
    
#右鍵menu
'''class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):         

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context menu')    
        self.show()

    #create 右鍵 menu
    def contextMenuEvent(self, event):

           cmenu = QMenu(self)

           newAct = cmenu.addAction("New")
           opnAct = cmenu.addAction("Open")
           quitAct = cmenu.addAction("Quit")
           
           #顯示選單
           action = cmenu.exec_(self.mapToGlobal(event.pos()))
           
           if action == newAct:
               print("newAct")
           if action == opnAct:
               print("Open")
           if action == quitAct:
               qApp.quit()
        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())'''

#勾選menu
'''class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):         

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        #create
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        
        #點擊event
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')    
        self.show()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())'''

#submenu

'''class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):         

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        
        #create new menu
        impMenu = QMenu('Import', self)
        
        #create new sub menu
        impAct = QAction('ccc', self) 
        impMenu.addAction(impAct)

        newAct = QAction('New', self)
        newAct2 = QAction('ㄏㄏㄏ', self)  

        fileMenu.addAction(newAct)
        fileMenu.addAction(newAct2)
        fileMenu.addMenu(impMenu)
        #fileMenu.addMenu(impMenu2)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())'''

#
'''class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               
        
        #創建MENU行列
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct2 = QAction(QIcon('exit.png'), '787', self)
        
        #set 快捷鍵
        exitAct.setShortcut('Ctrl+Q')
        exitAct2.setShortcut('Ctrl+K')
        
        #在最下方顯示文字
        exitAct.setStatusTip('Exit application')
        exitAct2.setStatusTip('c c c')
        exitAct2.addAction(fileMenu2)
        #關閉視窗
        exitAct.triggered.connect(qApp.quit)
        #exitAct2.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu2 = menubar.addMenu('GO')
        
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())'''
#    
    
'''class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 600, 150)
        self.setWindowTitle('Statusbar')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())'''