#pyrcc5 images.qrc -o images.py
#python -m PyQt5.uic.pyuic -x converter_screen.ui -o ekran.py

from PyQt5.QtWidgets import *
from ekran import Ui_Form
import ctypes


class Ekran(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ap = Ui_Form()
        self.ap.setupUi(self)
        self.ap.hesabla.clicked.connect(self.hesabla)
        self.setFixedSize(1144, 599)
        self.setWindowTitle("Number System Converter    |Gcosx.js|")
        
    def cevirici(self, eded, birinci_secim, ikinci_secim):
        try:
          onluq = int(eded, birinci_secim)
          yeni_eded = ""
          while onluq > 0:
              q = onluq % ikinci_secim
              if q >= 10:
                  herf = chr(ord("A") + q - 10)
                  yeni_eded = herf + yeni_eded
              else:
                  yeni_eded = str(q) + yeni_eded
              b = onluq // ikinci_secim
              onluq = b
          return yeni_eded
        except:
          self.ap.main_label.setText("None")
          self.ap.eded.setText("")
          self.ap.birinci.setCurrentIndex(0)
          self.ap.ikinci.setCurrentIndex(0)
          ikon = 0x10
          alfa = 0x100
          self.ap.main_label.setText('')
          mesaj = "Etməyə çalışdığınız hər hansısa uyğunsuz prosesə görə proqram dayandı!"
          basliq = "Converter dayandı!"
          ctypes.windll.user32.MessageBoxW(None, mesaj, basliq, ikon | alfa, 500, 300)
  
      
    def hesabla(self):
        if self.ap.birinci.currentText() != '' and self.ap.ikinci.currentText() != '' and self.ap.eded.text() != '':
            self.ap.main_label.setText(str(self.cevirici(self.ap.eded.text(), int(self.ap.birinci.currentText()), int(self.ap.ikinci.currentText()))))
        else:
            ikon = 0x10
            alfa = 0x100
            self.ap.main_label.setText('None')
            mesaj = "Etməyə çalışdığınız hər hansısa uyğunsuz prosesə görə proqram dayandı!"
            basliq = "Converter dayandı!"
            ctypes.windll.user32.MessageBoxW(None, mesaj, basliq, ikon | alfa, 500, 300)
  

app = QApplication([])
ekran = Ekran()
ekran.show()
app.exec_()
