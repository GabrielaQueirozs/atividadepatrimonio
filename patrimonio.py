from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout , QMessageBox


import sys

class Patrimonio(QWidget):
    def __init__(self):
        super().__init__() 
        
        # Cadastro equipamentos
        self.setGeometry(10,40,400,300)


    # Nome da barra

        self.setWindowTitle("Cadastro Equipamentos")

  # gerenciador de layout vertical
        self.patrimonio_v = QVBoxLayout()


    # labels para os dados do cliente
        self.label_id = QLabel("ID:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")

        self.label_serie = QLabel("Número de Série:")
        self.label_serie.setStyleSheet("QLabel{font-size:12pt}")

        self.label_patrimonio = QLabel("Nome do Patrimônio:")
        self.label_patrimonio.setStyleSheet("QLabel{font-size:12pt}")

        self.label_tipo = QLabel("Tipo:")
        self.label_tipo.setStyleSheet("QLabel{font-size:12pt}")

        
        self.label_descricao = QLabel("Descrição:")
        self.label_descricao.setStyleSheet("QLabel{font-size:12pt}")

        
        self.label_localizacao = QLabel("Localização do Produto:")
        self.label_localizacao.setStyleSheet("QLabel{font-size:12pt}")
        
        self.label_fabricacao = QLabel("Data de Fabricação:")
        self.label_fabricacao.setStyleSheet("QLabel{font-size:12pt}")

        self.label_aquisicao = QLabel("Data de Aquisição:")
        self.label_aquisicao.setStyleSheet("QLabel{font-size:12pt}")



        # line edit para os nomes dos patrimônios

        
        self.edit_id =  QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{Font-size:12pt}")

        self.edit_serie = QLineEdit()
        self.edit_serie.setStyleSheet("QLineEdit{Font-size:12pt}")

        self.edit_patrimonio = QLineEdit()
        self.edit_patrimonio.setStyleSheet("QLineEdit{font-size:12pt}")
        
        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit{font-size:12pt}")
        

        self.edit_descricao = QLineEdit()
        self.edit_descricao.setStyleSheet("QLineEdit{font-size:12pt}")

        self.edit_localizacao = QLineEdit()
        self.edit_localizacao.setStyleSheet("QLineEdit{font-size:12pt}")

        self.edit_fabricacao = QLineEdit()
        self.edit_fabricacao.setStyleSheet("QLineEdit{font-size:12pt}")

        self.edit_aquisicao = QLineEdit()
        self.edit_aquisicao.setStyleSheet("QLineEdit{font-size:12pt}")



         # Botão para cadastrar patrimonio
        self.button = QPushButton("Cadastrar Patrimônio")
        self.button.setStyleSheet("QPushButton{background-color:black;color:white;font-size:12pt;font-weight:bold}")

        # Chamar a função do botao
        self.button.clicked.connect(self.cadastrar)

         #  Adicionar a label nome e o lineedit no layout vertical
        self.patrimonio_v.addWidget(self.label_id)
        self.patrimonio_v.addWidget(self.edit_id)

        self.patrimonio_v.addWidget(self.label_serie)
        self.patrimonio_v.addWidget(self.edit_serie)

        self.patrimonio_v.addWidget(self.label_patrimonio)
        self.patrimonio_v.addWidget(self.edit_patrimonio)

        self.patrimonio_v.addWidget(self.label_tipo)
        self.patrimonio_v.addWidget(self.edit_tipo)
        

        self.patrimonio_v.addWidget(self.label_descricao)
        self.patrimonio_v.addWidget(self.edit_descricao)

        self.patrimonio_v.addWidget(self.label_localizacao)
        self.patrimonio_v.addWidget(self.edit_localizacao)

        self.patrimonio_v.addWidget(self.label_fabricacao)
        self.patrimonio_v.addWidget(self.edit_fabricacao)

        self.patrimonio_v.addWidget(self.label_aquisicao)
        self.patrimonio_v.addWidget(self.edit_aquisicao)

        # botão
        self.patrimonio_v.addWidget(self.button)


        # adicionar o layout
        self.setLayout(self.patrimonio_v)


    def cadastrar(self):
      if(self.edit_id.text()== "" or self.edit_serie.text()== "" or self.edit_patrimonio.text()=="" or self.edit_tipo.text()=="" or self.edit_descricao.text()=="" or self.edit_fabricacao.text()=="" or self.edit_aquisicao.text()==""):
        QMessageBox.critical(self, "Error" , "Você deve preencher todos os campos")
        #  Arquivo de texto
      else:    
            arquivo = open("Produtos.csv","+a",encoding="utf8")
            arquivo.write(f"{self.edit_id.text()};")
            arquivo.write(f"{self.edit_serie.text()};")
            arquivo.write(f"{self.edit_patrimonio.text()};")
            arquivo.write(f" {self.edit_tipo.text()};")
            arquivo.write(f" {self.edit_descricao.text()};")
            arquivo.write(f" {self.edit_localizacao.text()};")
            arquivo.write(f" {self.edit_fabricacao.text()};")
            arquivo.write(f" {self.edit_aquisicao.text()}\n")
            arquivo.close()

            QMessageBox.information(self,"salvo", "Os dados do patrimônio foram salvos")

# app = QApplication(sys.argv)

# iniciar a janela
# tela = Patrimonio() 
# Exibir na tela durante a execução

# tela.show()
# clicar e sair da tela e sair da memória
# app.exec() 
        


        
        
        
        

        


        
        

    

        


        





