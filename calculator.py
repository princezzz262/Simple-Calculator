
from PyQt5 import QtCore, QtGui, QtWidgets
import pyperclip

#mispelled subtract button --> SUBTACTbtn 

class Ui_Calculator(object):
     
    def __init__(self):
         self.question =""
         self.result=""
            
    def copy(self):
         self.restring = self.RESULTview.text()
         pyperclip.copy(self.restring)
         
         
    def Allclear(self):
         self.question = ""    
         self.RESULTview.setText("")
         self.QUESTIONview.setText("0")

    def clear(self):
         self.question = self.question[:-1]
         self.QUESTIONview.setText(self.question)

    def percentage(self):
         self.question += "/100"
         self.QUESTIONview.setText(self.question)
            
    def one(self):
            self.question += "1"
            self.QUESTIONview.setText(self.question)
    
    def two(self):
            self.question += "2"
            self.QUESTIONview.setText(self.question)

    def three(self):
             self.question += "3"
             self.QUESTIONview.setText(self.question)
            
    def four(self):
             self.question += "4"
             self.QUESTIONview.setText(self.question)       
            
    def five(self):
             self.question += "5"
             self.QUESTIONview.setText(self.question)     
            
    def six(self):
             self.question += "6"
             self.QUESTIONview.setText(self.question)
             
    def seven(self):
             self.question += "7"
             self.QUESTIONview.setText(self.question)
             
    def eight(self):
             self.question += "8"
             self.QUESTIONview.setText(self.question)
             
    def nine(self):
             self.question += "9"
             self.QUESTIONview.setText(self.question)
             
    def zero(self):
             self.question += "0"
             self.QUESTIONview.setText(self.question)
    
    def plus(self):
             self.question += "+"
             self.QUESTIONview.setText(self.question)         
    def subtraction(self):
             self.question += "-"
             self.QUESTIONview.setText(self.question)
             
    def division(self):
             self.question += "/"
             self.QUESTIONview.setText(self.question)
    
    def multiplication(self):
             self.question += "*"
             self.QUESTIONview.setText(self.question)
        
    def dot(self):
             self.question += "."
             self.QUESTIONview.setText(self.question)
             
    def M(self):
             self.hold = self.result
             self.question = ""
             self.question += self.hold
             self.QUESTIONview.setText(self.question)
        
    def equals(self):
        try:
            self.result = str(eval(self.question))
            self.RESULTview.setText(self.result)
            self.question = ""
            self.QUESTIONview.setText("0")
        except Exception as e:
            self.RESULTview.setText("Error")
            self.question = ""
            self.QUESTIONview.setText("0")
             
       

                  
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(300, 500)
        Calculator.setMinimumSize(QtCore.QSize(300, 500))
        Calculator.setMaximumSize(QtCore.QSize(300, 500))
        Calculator.setWindowOpacity(0.7)
        Calculator.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 180, 281, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.EQUALTObtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.EQUALTObtn.clicked.connect(self.equals)
        self.EQUALTObtn.setMinimumSize(QtCore.QSize(50, 50))
        self.EQUALTObtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 85, 0);")
        self.EQUALTObtn.setObjectName("EQUALTObtn")
        self.gridLayout.addWidget(self.EQUALTObtn, 4, 3, 1, 1)
        self.FULLSTOPbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.FULLSTOPbtn.clicked.connect(self.dot)
        self.FULLSTOPbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.FULLSTOPbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.FULLSTOPbtn.setObjectName("FULLSTOPbtn")
        self.gridLayout.addWidget(self.FULLSTOPbtn, 4, 2, 1, 1)
        self.ACbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ACbtn.clicked.connect(self.Allclear)
        self.ACbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.ACbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.ACbtn.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ACbtn.setObjectName("ACbtn")
        self.gridLayout.addWidget(self.ACbtn, 0, 0, 1, 1)
        self.PERCENTbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PERCENTbtn.clicked.connect(self.percentage)
        self.PERCENTbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.PERCENTbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.PERCENTbtn.setObjectName("PERCENTbtn")
        self.gridLayout.addWidget(self.PERCENTbtn, 0, 2, 1, 1)
        self.Cbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Cbtn.clicked.connect(self.clear)
        self.Cbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.Cbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.Cbtn.setObjectName("Cbtn")
        self.gridLayout.addWidget(self.Cbtn, 0, 1, 1, 1)
        self.SEVENbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SEVENbtn.clicked.connect(self.seven)
        self.SEVENbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.SEVENbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.SEVENbtn.setObjectName("SEVENbtn")
        self.gridLayout.addWidget(self.SEVENbtn, 1, 0, 1, 1)
        self.FIVEbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.FIVEbtn.clicked.connect(self.five)
        self.FIVEbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.FIVEbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.FIVEbtn.setObjectName("FIVEbtn")
        self.gridLayout.addWidget(self.FIVEbtn, 2, 1, 1, 1)
        self.EIGHTbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.EIGHTbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.EIGHTbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.EIGHTbtn.setObjectName("EIGHTbtn")
        self.gridLayout.addWidget(self.EIGHTbtn, 1, 1, 1, 1)
        self.MULTIPLYbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MULTIPLYbtn.clicked.connect(self.multiplication)
        self.MULTIPLYbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.MULTIPLYbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"background-color: rgb(0, 173, 83);")
        self.MULTIPLYbtn.setObjectName("MULTIPLYbtn")
        self.gridLayout.addWidget(self.MULTIPLYbtn, 1, 3, 1, 1)
        self.SUBTACTbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SUBTACTbtn.clicked.connect(self.subtraction)
        self.SUBTACTbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.SUBTACTbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"background-color: rgb(0, 173, 83);")
        self.SUBTACTbtn.setObjectName("SUBTACTbtn")
        self.gridLayout.addWidget(self.SUBTACTbtn, 2, 3, 1, 1)
        self.DIVIDEbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.DIVIDEbtn.clicked.connect(self.division)
        self.DIVIDEbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.DIVIDEbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"background-color: rgb(0, 173, 83);")
        self.DIVIDEbtn.setObjectName("DIVIDEbtn")
        self.gridLayout.addWidget(self.DIVIDEbtn, 0, 3, 1, 1)
        self.SIXbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.EIGHTbtn.clicked.connect(self.eight)
        self.SIXbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.SIXbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.SIXbtn.setObjectName("SIXbtn")
        self.gridLayout.addWidget(self.SIXbtn, 2, 2, 1, 1)
        self.NINEbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SIXbtn.clicked.connect(self.six)
        self.NINEbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.NINEbtn.clicked.connect(self.nine)
        self.NINEbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.NINEbtn.setObjectName("NINEbtn")
        self.gridLayout.addWidget(self.NINEbtn, 1, 2, 1, 1)
        self.FOURbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.FOURbtn.clicked.connect(self.four)
        self.FOURbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.FOURbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.FOURbtn.setObjectName("FOURbtn")
        self.gridLayout.addWidget(self.FOURbtn, 2, 0, 1, 1)
        self.ONEbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ONEbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.ONEbtn.clicked.connect(self.one)
        self.ONEbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
        
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.ONEbtn.setObjectName("ONEbtn")
        self.gridLayout.addWidget(self.ONEbtn, 3, 0, 1, 1)
        self.TWObtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.TWObtn.clicked.connect(self.two)
        self.TWObtn.setMinimumSize(QtCore.QSize(50, 50))
        self.TWObtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.TWObtn.setObjectName("TWObtn")
        self.gridLayout.addWidget(self.TWObtn, 3, 1, 1, 1)
        self.PLUSbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PLUSbtn.clicked.connect(self.plus)
        self.PLUSbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.PLUSbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"background-color: rgb(0, 173, 83);")
        self.PLUSbtn.setObjectName("PLUSbtn")
        self.gridLayout.addWidget(self.PLUSbtn, 3, 3, 1, 1)
        self.THREEbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.THREEbtn.setMinimumSize(QtCore.QSize(50, 50))     
        self.THREEbtn.clicked.connect(self.three)
        self.THREEbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.THREEbtn.setObjectName("THREEbtn")
        self.gridLayout.addWidget(self.THREEbtn, 3, 2, 1, 1)
        self.ZERObtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ZERObtn.clicked.connect(self.zero)
        self.ZERObtn.setMinimumSize(QtCore.QSize(50, 50))
        self.ZERObtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.Mbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Mbtn.clicked.connect(self.M)
        self.Mbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.gridLayout.addWidget(self.Mbtn, 4, 1, 1, 1)
        self.Mbtn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius: 10px;")
        
        self.ZERObtn.setObjectName("ZERObtn")
        self.gridLayout.addWidget(self.ZERObtn, 4, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 281, 163))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.clicked.connect(self.copy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.RESULTview = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.RESULTview.setMinimumSize(QtCore.QSize(0, 30))
        self.RESULTview.setMaximumSize(QtCore.QSize(16777215, 50))
        self.RESULTview.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.RESULTview.setObjectName("RESULTview")
        self.verticalLayout.addWidget(self.RESULTview)
        self.QUESTIONview = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.QUESTIONview.setMinimumSize(QtCore.QSize(0, 40))
        self.QUESTIONview.setMaximumSize(QtCore.QSize(16777215, 50))
        self.QUESTIONview.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.QUESTIONview.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.QUESTIONview.setWordWrap(True)
        self.QUESTIONview.setObjectName("QUESTIONview")
        self.verticalLayout.addWidget(self.QUESTIONview)
        Calculator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.EQUALTObtn.setText(_translate("Calculator", "="))
        self.FULLSTOPbtn.setText(_translate("Calculator", "."))
        self.ACbtn.setText(_translate("Calculator", "AC"))
        self.PERCENTbtn.setText(_translate("Calculator", "%"))
        self.Cbtn.setText(_translate("Calculator", "C"))
        self.SEVENbtn.setText(_translate("Calculator", "7"))
        self.FIVEbtn.setText(_translate("Calculator", "5"))
        self.Mbtn.setText(_translate("Calculator", "M"))
        self.EIGHTbtn.setText(_translate("Calculator", "8"))
        self.MULTIPLYbtn.setText(_translate("Calculator", "x"))
        self.SUBTACTbtn.setText(_translate("Calculator", "-"))
        self.DIVIDEbtn.setText(_translate("Calculator", "/"))
        self.SIXbtn.setText(_translate("Calculator", "6"))
        self.NINEbtn.setText(_translate("Calculator", "9"))
        self.FOURbtn.setText(_translate("Calculator", "4"))
        self.ONEbtn.setText(_translate("Calculator", "1"))
        self.TWObtn.setText(_translate("Calculator", "2"))
        self.PLUSbtn.setText(_translate("Calculator", "+"))
        self.THREEbtn.setText(_translate("Calculator", "3"))
        self.ZERObtn.setText(_translate("Calculator", "0"))
        self.pushButton.setText(_translate("Calculator", "Copy"))
        self.RESULTview.setText(_translate("Calculator", " "))
        self.QUESTIONview.setText(_translate("Calculator", "0"))


        
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
