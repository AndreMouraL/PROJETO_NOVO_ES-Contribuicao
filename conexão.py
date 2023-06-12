from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ConexaoBancoDados:
    def __init__(self):
        try:
            engine = create_engine('mysql+pymysql://andre:andre3080&@192.168.0.103/estoque')
            Session = sessionmaker(bind=engine)
            self.session = Session()
            #print("Conexão realizada com Sucesso!")
        except Exception as e:
            print("Erro ao conectar ao banco de dados:", e)
        

    def fecharConexao(self):
        self.session.close()
        return 'Operação realizada com Sucesso!'




    
