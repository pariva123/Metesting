from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox,QErrorMessage
@pyqtSlot()
def on_click(self):
    try: ab=self. textbx.text()
        ac=self. textbox.text()
        ad=self. textboxi.text()
        if(ab. isalpha()==False):
            raise Exc("Please check the name field")
        if(ac. isnumeric()==False):
            raise Exc("Please check the rollno field")
        if(ad. isalpha()==False):
            raise Exc("Please check the address field")
    except Exc as m:
        QMessageBox.question(self, 'Message-From Students',m.a, QMessageBox.Ok,QMessageBox .Ok)


    count=0
    try:

        t1=self. textbox1.text()
        t2=self. textbox2.text()
        if(t1.isnumeric () and t2.isnumeric()):
            if(int(t1)>=0 and int(t2 ) >=0 and int(t1 ) <=25 and int( t2) <=75):
                a1=int(t1)+int( t2 )
                a1=str(a1);count +=1
                self.textbox3.setText(a1)
            else:
                raise Ex("C box: Please enter within the range")
        else:
            raise Exc("C box:Please enter something")
    except Exc as e:
        QMessageBox.question(self, 'Message-From Students',e.a,QMessageBox .Ok, QMessageBox.Ok)
    except Ex as en:
        QMessageBox.question(self, 'Message-From Students',en.b, QMessageBox.Ok, QMessageBox.Ok)

    try:
        t3=self.textbox4. text()
        t4=self.textbox5. text()
        if(t3.isnumeric() and t4.isnumeric()):
            if(int(t3)>=0 and int(t4)>=0 and int(t3)<=25 and int(t4)<=75) : a2=int(t3)+int(t4)
                a2= str (a2); count+=1
                self. textbox6. setText(a2) else:
                raise Ex("C++ box: Please enter within the range")
        else:
            raise Exc("C++ box:Please enter something")
    except Exc as e:
        QMessageBox.question(self,'Message-From Students',e.a,QMessageBox.Ok,QMessageBox.Ok)
    except Ex as en: QMessageBox.question( self, 'Message-From Students',en.b,QMessageBox.Ok,QMessageBox.Ok)
    try:
        t5= self.textbox7.text() t6=self.textbox8.text()
        if(t5.isnumeric() and t6. isnumeric()):
            if(int(t5) >=0 and int(t6)>=0 and int(t5)<= 25 and int(t6)<=75):
                a3=int(t5)+int( t6)
                a3= str(a3);count+=1 self.textbox9.setText(a3) else: raise Ex( "Java box: Please enter within the range") else:
            raise Exc("Java box:Please enter something")
    except Exc as e:
        QMessageBox.question(self,'Message-From Students',e.a,QMessageBox.Ok,QMessageBox.Ok)
    except Ex as en:
        QMessageBox.question(self,'Message-From Students',en.b, QMessageBox.Ok,QMessageBox.Ok) try:
        t7=self. textbox10.text()
        t8=self.textbox11.text()
        if(t7. isnumeric() and t8.isnumeric()) :
            if(int (t7)>=0 and int(t8)>=0 and int(t7)<= 25 and int(t8)<=75):
                a4=int(t7)+int(t8)
                a4=str(a4);count+=1
                self. textbox12. setText(a4)
            else: raise Ex( "PHP box: Please enter within the range")
        else:
            raise Exc( "PHP box:Please enter something")
    except Exc as e:
        QMessageBox.question(self,'Message-From Students',e.a,QMessageBox.Ok,QMessageBox.Ok)
    except Ex as en:
        QMessageBox.question(self,'Message-From Students',en.b,QMessageBox.Ok,QMessageBox.Ok)


    try:
        t9= self.textbox13.text() t10=self.textbox14.text( )
        if(t9.isnumeric() and t10.isnumeric()):
            if(int(t9 )>=0 and int(t10)>=0 and int( t9)<=25 and int (t10)<=75):
                a5=int(t9 ) +int(t10)
                a5=str( a5);count+=1
                self. textbox15.setText(a5)
            else: raise Ex( "MySql box: Please enter within the range")
        else:
            raise Exc( "Mysql box:Please enter something")
    except Exc as e:
        QMessageBox.question(self,'Message-From Students',e.a,QMessageBox.Ok,QMessageBox.Ok)
    except Ex as en:
        QMessageBox.question(self,'Message-From Students',en.b,QMessageBox.Ok,QMessageBox.Ok)