from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout , QMessageBox


import sys
import csv

class Localizar_patrimonio(QWidget):
    def __init__(self):
        super().__init__() 
        
        # Cadastro equipamentos
        self.setGeometry(10,40,400,300)


    # Nome da barra

        self.setWindowTitle("Cadastro Equipamentos")

  # gerenciador de layout vertical
        self.patrimonio_v = QVBoxLayout()


    # labels para os dados dos produtos
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



        
        

         #  Adicionar a label nome e o lineedit no layout vertical
        self.patrimonio_v.addWidget(self.label_id)
        self.patrimonio_v.addWidget(self.edit_id)
        self.btnbuscar = QPushButton("Localizar Patrimônio")
        self.patrimonio_v.addWidget(self.btnbuscar)
        self.btnbuscar.clicked.connect(self.localizar)

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

       
        # adicionar o layout
        self.setLayout(self.patrimonio_v)

    def localizar(self):


       arquivo = open("Produtos.csv", "+a" , encoding="utf8")
       linhas = csv.reader(arquivo)



       for i in linhas:
           lin = str(i).replace("['","").replace("']","").split(";")
           if(lin[0]==self.edit_id.text()): 
                self.edit_serie.setText(lin[1])
                self.edit_patrimonio.setText(lin[2])
                self.edit_tipo.setText(lin[3])
                self.edit_descricao.setText(lin[4])
                self.edit_localizacao.setText(lin[5])
                self.edit_fabricacao.setText(lin[6])
                self.edit_aquisicao.setText(lin[7])



  


# app = QApplication(sys.argv)

# iniciar a janela
# tela = Patrimonio() 
# Exibir na tela durante a execução

# tela.show()
# clicar e sair da tela e sair da memória
# app.exec() 
        


        
        
        
        

        


        
        

    

        


        





