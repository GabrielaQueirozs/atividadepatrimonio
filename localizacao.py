from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout , QMessageBox


import sys

class Localizacao(QWidget):
    def __init__(self):
        super().__init__() 
        
        # Localização Equipamentos
        self.setGeometry(10,40,400,300)

         # Nome da barra

        self.setWindowTitle("Localização dos Equipamentos")
        # gerenciador de layout vertical
        self.localizacao_v = QVBoxLayout()


         # labels para a localização dos esquipamentos
        self.label_id = QLabel("ID:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")

        self.label_empresa = QLabel("Empresa:")
        self.label_empresa.setStyleSheet("QLabel{font-size:12pt}")

        self.label_logradouro = QLabel("Logradouro:")
        self.label_logradouro.setStyleSheet("QLabel{font-size:12pt}")

        self.label_número = QLabel("Número:")
        self.label_número.setStyleSheet("QLabel{font-size:12pt}")

        
        self.label_prédio = QLabel("Prédio:")
        self.label_prédio.setStyleSheet("QLabel{font-size:12pt}")

        
        self.label_andar = QLabel("Andar:")
        self.label_andar.setStyleSheet("QLabel{font-size:12pt}")
        
        self.label_sala = QLabel("Sala:")
        self.label_sala.setStyleSheet("QLabel{font-size:12pt}")




          # line edit para a localização dos patrimônios

        
        self.edit_id =  QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{Font-size:12pt}")

        self.edit_empresa = QLineEdit()
        self.edit_empresa.setStyleSheet("QLineEdit{Font-size:12pt}")

        self.edit_logradouro = QLineEdit()
        self.edit_logradouro.setStyleSheet("QLineEdit{font-size:12pt}")
        
        self.edit_número = QLineEdit()
        self.edit_número.setStyleSheet("QLineEdit{font-size:12pt}")
        

        self.edit_prédio = QLineEdit()
        self.edit_prédio.setStyleSheet("QLineEdit{font-size:12pt}")

        self.edit_andar = QLineEdit()
        self.edit_andar.setStyleSheet("QLineEdit{font-size:12pt}")

        self.edit_sala = QLineEdit()
        self.edit_sala.setStyleSheet("QLineEdit{font-size:12pt}")


          # Botão para cadastrar localização
        self.button = QPushButton("Localização")
        self.button.setStyleSheet("QPushButton{background-color:red;color:white;font-size:12pt;font-weight:bold}")


            # Chamar a função do botao
        self.button.clicked.connect(self.localizar)
        

         #  Adicionar a label nome e o lineedit no layout vertical
        self.localizacao_v.addWidget(self.label_id)
        self.localizacao_v.addWidget(self.edit_id)

     
        self.localizacao_v.addWidget(self.label_empresa)
        self.localizacao_v.addWidget(self.edit_empresa)

        self.localizacao_v.addWidget(self.label_logradouro)
        self.localizacao_v.addWidget(self.edit_logradouro)

        self.localizacao_v.addWidget(self.label_número)
        self.localizacao_v.addWidget(self.edit_número)

        self.localizacao_v.addWidget(self.label_prédio)
        self.localizacao_v.addWidget(self.edit_prédio)
        

        self.localizacao_v.addWidget(self.label_andar)
        self.localizacao_v.addWidget(self.edit_andar)

        self.localizacao_v.addWidget(self.label_sala)
        self.localizacao_v.addWidget(self.edit_sala)

        
        # botão
        self.localizacao_v.addWidget(self.button)


         # adicionar o layout
        self.setLayout(self.localizacao_v)

    def localizar(self):
        if(self.edit_id.text()== "" or self.edit_empresa.text()=="" or self.edit_logradouro.text()=="" or  self.edit_número.text()=="" or )
        #  Arquivo de texto

        arquivo = open("localizacao.txt","+a",encoding="utf8")
        arquivo.write(f"ID: {self.edit_id.text()}\n")
        arquivo.write(f"Empresa:{self.edit_empresa.text()}\n")
        arquivo.write(f"Lagradouro: {self.edit_logradouro.text()}\n")
        arquivo.write(f"Número: {self.edit_número.text()}\n")
        arquivo.write(f"Prédio: {self.edit_prédio.text()}\n")
        arquivo.write(f"Andar: {self.edit_andar.text()}\n")
        arquivo.write(f"Sala: {self.edit_sala.text()}\n")
        arquivo.write("----------------------------------------\n")
        arquivo.close()
        
     


# app = QApplication(sys.argv)

# iniciar a janela
# tela = Localizacao() 
# Exibir na tela durante a execução

# tela.show()
# clicar e sair da tela e sair da memória
# app.exec() 






       