import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('windowTitle')
        self.setWindowIcon(QIcon('PyQt/01-basic/image/aperture.png')) # 아이콘 지정
        # self.move(300,300) 
        # self.resize(400,200)
        self.setGeometry(300,300,400,200) # 초기의 move와 resize를 동시에 지정한다. 차라리 튜플 2개면 더 좋았을거 같다.
        self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
   