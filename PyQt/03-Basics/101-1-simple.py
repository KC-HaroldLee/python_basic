import sys
# from PyQt5.QTWidgets import QApplication, QWidget # ???
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):

    def __init__(self): # self는 MyApp 클래스를 의미한다.
        super().__init__()
        self.initUI()
    
    def initUI(self): # self는? 무엇을?
        self.setWindowTitle('windowTitle')
        self.move(300,300)
        # self.show() # 느린 컴퓨터에서 확인해보자
        self.resize(400,200)
        self.show() # 뵈줌

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
   