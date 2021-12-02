import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QToolTip # 하나 추가
from PyQt5.QtGui import QFont, QIcon

# class MyApp(QWidget):
class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget<b> widget')

        # 버튼
        quitBtn = QPushButton('Quit', self)
        quitBtn.setGeometry(50,50,50,100)
        quitBtn.setToolTip('plug out<b>GlaDOS')
        quitBtn.clicked.connect(QCoreApplication.instance().quit)

        self.statusBar().showMessage('There you are')

        # 기본창
        self.setWindowTitle('GlaDOS')
        self.setWindowIcon(QIcon('PyQt/01-basic/image/aperture.png'))
        self.setGeometry(300,300,400,200)
        self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
   