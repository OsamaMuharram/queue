# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/osama/Desktop/pro.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(877, 563)
        Form.setStyleSheet(_fromUtf8(""))
        self.Enter_Button = QtGui.QPushButton(Form)
        self.Enter_Button.setGeometry(QtCore.QRect(110, 320, 121, 71))
        self.Enter_Button.setStyleSheet(_fromUtf8(""))
        self.Enter_Button.setObjectName(_fromUtf8("Enter_Button"))
        self.Arrival_Time = QtGui.QLineEdit(Form)
        self.Arrival_Time.setGeometry(QtCore.QRect(170, 70, 79, 29))
        self.Arrival_Time.setObjectName(_fromUtf8("Arrival_Time"))
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(100, 240, 141, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(89, 74, 66, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Clear_botton = QtGui.QPushButton(Form)
        self.Clear_botton.setGeometry(QtCore.QRect(130, 420, 88, 29))
        self.Clear_botton.setStyleSheet(_fromUtf8(""))
        self.Clear_botton.setObjectName(_fromUtf8("Clear_botton"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(89, 124, 69, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(390, 270, 361, 231))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.servies_Time = QtGui.QLineEdit(Form)
        self.servies_Time.setGeometry(QtCore.QRect(170, 120, 79, 29))
        self.servies_Time.setObjectName(_fromUtf8("servies_Time"))
        self.layoutWidget_2 = QtGui.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(760, 270, 71, 231))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lcd_L = QtGui.QLCDNumber(self.layoutWidget_2)
        self.lcd_L.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_L.setObjectName(_fromUtf8("lcd_L"))
        self.verticalLayout.addWidget(self.lcd_L)
        self.lcd_Lq = QtGui.QLCDNumber(self.layoutWidget_2)
        self.lcd_Lq.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_Lq.setObjectName(_fromUtf8("lcd_Lq"))
        self.verticalLayout.addWidget(self.lcd_Lq)
        self.lcd_p0 = QtGui.QLCDNumber(self.layoutWidget_2)
        self.lcd_p0.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_p0.setObjectName(_fromUtf8("lcd_p0"))
        self.verticalLayout.addWidget(self.lcd_p0)
        self.lcd_w = QtGui.QLCDNumber(self.layoutWidget_2)
        self.lcd_w.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_w.setObjectName(_fromUtf8("lcd_w"))
        self.verticalLayout.addWidget(self.lcd_w)
        self.lcd_wq = QtGui.QLCDNumber(self.layoutWidget_2)
        self.lcd_wq.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_wq.setObjectName(_fromUtf8("lcd_wq"))
        self.verticalLayout.addWidget(self.lcd_wq)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(350, 320, 16, 112))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(670, 60, 111, 41))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.Model_Name = QtGui.QLabel(Form)
        self.Model_Name.setGeometry(QtCore.QRect(410, 130, 276, 111))
        self.Model_Name.setStyleSheet(_fromUtf8("font:35 italic 30pt \"Century Schoolbook L\";"))
        self.Model_Name.setObjectName(_fromUtf8("Model_Name"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(89, 184, 69, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.capacity = QtGui.QLineEdit(Form)
        self.capacity.setGeometry(QtCore.QRect(170, 180, 79, 29))
        self.capacity.setObjectName(_fromUtf8("capacity"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Queue", None))
        self.Enter_Button.setText(_translate("Form", "Calculate", None))
        self.label_5.setText(_translate("Form", "Arrival rate ", None))
        self.Clear_botton.setText(_translate("Form", "RESET", None))
        self.label_6.setText(_translate("Form", "Service rate ", None))
        self.label.setText(_translate("Form", "Average number of customers in system (L) ", None))
        self.label_3.setText(_translate("Form", "Average number of customers waiting in line (Lq)", None))
        self.label_4.setText(_translate("Form", "Probability of no customers in system (P0)", None))
        self.label_2.setText(_translate("Form", "Average time in system (W)", None))
        self.label_7.setText(_translate("Form", "Average time waiting in line (wq)", None))
        self.comboBox.setItemText(4, _translate("Form", "D / D / 1 / k-1", None))
        self.comboBox.setItemText(2, _translate("Form", "M/ M / 1", None))
        self.comboBox.setItemText(3, _translate("Form", "M / M / c / K", None))
        self.comboBox.setItemText(0, _translate("Form", "M / M / c", None))
        self.comboBox.setItemText(1, _translate("Form", "M / M / 1 / K", None))
        self.label_9.setText(_translate("Form", "capacity", None))

