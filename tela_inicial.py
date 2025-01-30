import sys 
from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QPushButton , QVBoxLayout
from patrimonio import Patrimonio
from localizacao import Localizacao
from localizar_patrimonio import Localizar_patrimonio
class TelaInicial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciar")
        self.setGeometry(300,200,200,150)
        self.layout_v = QVBoxLayout()
        self.button_localizar = QPushButton("Localizar Patrimônio")
                                            

        self.label_titulo = QLabel("Clique para abrir a janela")
        self.button = QPushButton("Abrir Patrimônio")

        self.button1= QPushButton("Abrir Localização")
        self.button_localizar = QPushButton("Buscar Patrimônio")
                                           

        self.layout_v.addWidget(self.label_titulo)
        self.layout_v.addWidget(self.button)

        self.layout_v.addWidget(self.button1)
        self.layout_v.addWidget(self.button_localizar)
        
        
        self.button.clicked.connect(self.abrir_cadastro)
        self.button1.clicked.connect(self.abrir_localizacao)
        self.button_localizar.clicked.connect(self.localizar_patrimonio)
       
        
        # colocar na tela

        self.setLayout(self.layout_v)
        #  outra função
    def abrir_cadastro(self):
        self.pat = Patrimonio()
        self.pat.show()
    def abrir_localizacao(self):
        self.pat1 = Localizacao()
        self.pat1.show()
    def localizar_patrimonio(self):
        self.pat2 = Localizar_patrimonio()
        self.pat2.show()



app = QApplication(sys.argv)
tela = TelaInicial()
tela.show()
app.exec()        