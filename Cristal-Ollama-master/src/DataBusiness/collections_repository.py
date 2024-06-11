from .index import MongoDBConnectionFactory


class BaseConnection:

    def __init__(self):
        self.db = MongoDBConnectionFactory.get_db()
        self.games = self.db['Games']  # Conectando à coleção 'Games'
        self.embeddings = self.db['Embeddings']
