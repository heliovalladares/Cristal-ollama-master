from .index import MongoDBConnectionFactory
import pandas as pd

class BaseConnection():
    df_games = pd.DataFrame()
    def __init__(self):
        self.db = MongoDBConnectionFactory.get_db()
        self.collection = self.db['Games']  # Conectando à coleção 'Games'
        self.embeddings = self.db['Embeddings']


    def returning(self):
        try:
            document = self.collection.find_one({"title": "Elden Ring"})
            if document:
                return document
            else:
                print("Documento não encontrado.")
        except Exception as e:
            print(f"Erro ao consultar o banco de dados: {e}")

    @classmethod
    def charging_collections_in_dataframe(cls):
        try:
            games = list(cls().collection.find())
            cls.df_games = pd.DataFrame(games)
            print(f"{len(games)} documentos carregados no DataFrame.")
        except Exception as e:
            print(f"Erro ao carregar os dados no DataFrame: {e}")



