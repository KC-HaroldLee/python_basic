import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton # 하나 추가
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        quitBtn = QPushButton('Quit', self) # 2번째 인자는 MyApp / QPushButton도 클래스
        quitBtn.setGeometry(50,50,50,100) # 도 됨
        # quitBtn.move(50, 50)
        # quitBtn.resize(quitBtn.sizeHint())
        quitBtn.clicked.connect(QCoreApplication.instance().quit)
        # https://wikidocs.net/22020
        # 'clicked' 시그널은 어플리케이션을 종료하는 quit() 메서드에 연결됨


        self.setWindowTitle('windowTitle')
        self.setWindowIcon(QIcon('PyQt/01-basic/image/aperture.png'))
        self.setGeometry(300,300,400,200)
        self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
   