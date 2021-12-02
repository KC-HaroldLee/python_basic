import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout # 뭐 준비하래서 준비하는 거지만...

class MainWindow(QWidget):

    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&btn1', self) # &은 ALT를 의미한다. 그렇다면 ? #?
        btn1.setCheckable(True)
        btn1.toggle() # on/off가 가능한 스위치가 된다.

        btn2 = QPushButton(self)
        btn2.setText('btn&2') # init할 때 하지 않아도 되긴한다.

        btn3 = QPushButton('btn3', self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())