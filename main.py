from __future__ import division
from twisted.persisted.aot import _selfOfMethod
from PyQt4.QtCore import *
import math
from PyQt4.QtGui import *
import sys
from GUI import Ui_Form
from GUI import Ui_Form


class main(QWidget,Ui_Form):

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.comboBox.currentIndexChanged.connect(self.switch_Model)
        # calculat button
        #start program
        self.Enter_Button.clicked.connect(self.play)
        #clear buttun
        self.Clear_botton.clicked.connect(self.clear)
        #read current text in cobobox
        text = str(self.comboBox.currentText())
        #write current model name in lable
        self.Model_Name.setText(text)
    #start calculate a model had choised
    def play(self):
        l = float(self.Arrival_Time.text())
        m = float(self.servies_Time.text())
        try:
            k = float(self.capacity.text())
        except ValueError:
            pass

        text = str(self.comboBox.currentText())
        if text == "M / M / c":
            self.M_M_c_Model(l, m, k)
        elif text == "M/ M / 1":
            self.M_M_1_Model(l,m)
        elif text == "M / M / 1 / K":
            self.M_M_1_K_Model(l,m,k)
        elif text == "M / M / c / K":
            self.M_M_C_k(l,m,k)




    def M_M_1_Model(self,l,m):

        ## M / M / 1

        # Average number of customers in system (L)
        L = (l / (m - l))
        # Average number of customers waiting in line (Lq)
        Lq = (l * l) / (m * (m - l))
        # Probability of no customers in system (P0)
        p0 = (1 - (l/m)) * 100
        # Average time in system (W)
        W = 1 / (m - l)
        # Average time waiting in line (wq)
        Wq = l / (m * (m - l))
        #function --> display resulats on lcd number
        self.display(L, Lq, W, Wq, p0)

    def M_M_1_K_Model(self,l,m,k):
        p = (l / m)
        if p == 1:
            # Average number of customers in system (L)
            L = k / 2
            pk = (1) / (1 + k)
        else:
            # Average number of customers in system (L)
            L = ((1 - (k + 1) * math.pow(p, k)) + (k * math.pow(p,( k + 1)))) / ((1 - p) * (1 - math.pow(p, (k + 1))))
            L=L*p
            pk = math.pow(p, k) * ((1 - p) / (1 - math.pow(p, k + 1)))

        l_dash = l * (1 - pk)
        # Probability of no customers in system (P0)
        p0 = (1 / (m - l)) * 100
        # Average time in system (W)
        W = L / l_dash
        # Average time waiting in line (wq)
        Wq = W - (1 / m)
        # Average number of customers waiting in line (Lq)
        Lq = l_dash * Wq
        # function --> display resulats on lcd number
        self.display(L, Lq, W, Wq, p0)

    def M_M_c_Model(self,l,m,k):

        ## M / M / c
        c=k
        r = l / m
        p = r / c

        if p < 1:
            count = 0
            for i in range(0, int(c)):
                div = math.pow(r, i) / math.factorial(i)
                count = count + div
            p0 = count + ((c * math.pow(r, c)) / (math.factorial(c) * (c - r)))
            p0 = 1 / p0

        else:
            count = 0
            for i in range(0, int(c)):
                div = (1 / math.factorial(i)) * math.pow((l / m), i)
                count = count + div
        div_2 = (1 / math.factorial(c)) * math.pow((l / m), c) * ((c * m) / ((c * m) - l))
        p0 = count + div_2
        p0 = 1 / p0

        # Average number of customers waiting in line (Lq)
        Lq = ((math.pow(r, (c + 1)) / c) / (math.factorial(c) * math.pow(((1 - r) / c), 2)))* p0


        # Probability of no customers in system (P0)
        p0 = (c-r)/c * 100
        # Average time in system (W)
        W = (Lq / l) + (1 / m)
        # Average time waiting in line (wq)
        Wq = Lq / l
        # Average number of customers waiting in line (Lq)
        L = Lq + (l / m)
        # function --> display resulats on lcd number
        self.display(L,Lq,W,Wq,p0)




    def M_M_C_k(self,l,m,k):
        ## M/M/c/K
        c=k-1
        r = l / m
        p = r / c

        if p !=1:
            count = 0
            for i in range(0, c):
                div = math.pow(r, i) / math.factorial(i)
                count = count + div
            div_2 = (math.pow(r, c) / math.factorial(c)) * ((1 - math.pow(p, (k - c + 1))) / (1 - p))
            p0 = count + div_2
            p0 = 1 / p0

        else:
            count = 0
            for i in range(0,int(c) ):
                div = (1 / math.factorial(i)) * math.pow((l / m), i)
                count = count + div
        div_2 = (math.pow(r, c) / math.factorial(c)) * (k - c + 1)
        p0 = count + div_2
        p0 = 1 / p0

        # Average number of customers waiting in line (Lq)
        div_1 = (p * math.pow(r, c) * p0) / (math.factorial(c) * math.pow((1 - p), 2))
        div_2 = math.pow((1 - p), (k - c + 1)) - (1 - p) * (k - c + 1) * math.pow(p, k - c)
        Lq = div_2 * div_1

        pk = (math.pow(r, k) / math.factorial(k)) * p0
        # Probability of no customers in system (P0)
        p0 = (1 / (m - l)) * 100
        # Average time in system (W)
        W = l / 1 - pk
        # Average time waiting in line (wq)
        Wq = Lq / 1 - pk
        # Average number of customers waiting in line (Lq)
        count = 0
        for x in range(0,int(c) ):
            count = count + ((c - i) * (math.pow(r, i) / math.factorial(i)))

        L = Lq + c - (p0 * count)
        self.display(L, Lq, W, Wq, p0)

    # display output on lcd number
    def display(self,L,Lq,W,Wq,p0):
        self.lcd_L.display(L)
        self.lcd_Lq.display(Lq)
        self.lcd_p0.display(p0)
        self.lcd_w.display(W)
        self.lcd_wq.display(Wq)


    ## select model from comBox
    def switch_Model(self):
        #clear all output and input
        self.clear()
        self.label_4.setText("Probability of no customers in system (P0)")
        text = str(self.comboBox.currentText())
        if text == "M / M / c":

            self.Model_Name.setText(text)
            self.show_1()
            self.label_9.setText('capacity')
            self.label_4.setText("Average number of idle server")

        elif text == "M/ M / 1":
            self.Model_Name.setText(text)
            self.show_1()
            self.capacity.hide()
            self.label_9.hide()
        elif text == "M / M / 1 / K":
            self.Model_Name.setText(text)
            self.show_1()
            self.label_9.setText('Buffer size')


    def show_1(self):
        self.label_2.show()
        self.label_4.show()
        self.label_7.show()
        self.capacity.show()
        self.label_9.show()


    # clear all output and input
    def clear(self):
        #lcd number
        self.lcd_L.display(0)
        self.lcd_Lq.display(0)
        self.lcd_w.display(0)
        self.lcd_wq.display(0)
        self.lcd_p0.display(0)
        #text lines
        self.Arrival_Time.clear()
        self.servies_Time.clear()
        self.capacity.clear()



app = QApplication(sys.argv)
window = main()
window.setWindowIcon(QIcon('logo.png'))
window.show()
app.exec_()
