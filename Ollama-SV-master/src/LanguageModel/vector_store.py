# Gerencia o armazenamento e recuperação de embeddings
import numpy as np
from DataBusiness import MongoDBConnectionFactory

class VectorStore:
    def __init__(self):
        self.db = MongoDBConnectionFactory.get_db()
        self.collection = self.db['Embeddings']  # Conectando à coleção 'Embeddings'

    def save_embedding(self, game_id, embedding, metadata):
        document = {
            "game_id": game_id,
            "embedding": embedding.tolist(),  # Convertendo array numpy para lista
            "metadata": metadata
        }
        self.collection.insert_one(document)

    def get_embedding(self, game_id):
        document = self.collection.find_one({"game_id": game_id})
        if document:
            return np.array(document['embedding'])
        return None

    def search_similar(self, query_embedding, top_n=5):
        cursor = self.collection.find()
        similarities = []
        for document in cursor:
            embedding = np.array(document['embedding'])

            # Log para verificar as dimensões dos embeddings armazenados
            print(f"Dimensão do embedding armazenado: {embedding.shape}")

            if embedding.shape != query_embedding.shape:
                print(f"Dimensões incompatíveis: {embedding.shape} vs {query_embedding.shape}")
                continue  # Pule embeddings com dimensões incompatíveis

            similarity = self.cosine_similarity(query_embedding, embedding)
            similarities.append((document, similarity))
        similarities.sort(key=lambda x: x[1], reverse=True)
        return [doc['metadata'] for doc, sim in similarities[:top_n]]

    @staticmethod
    def cosine_similarity(vec1, vec2):
        vec1 = vec1.flatten()  # Flatten para garantir que sejam vetores
        vec2 = vec2.flatten()

        dot_product = np.dot(vec1, vec2)
        norm_vec1 = np.linalg.norm(vec1)
        norm_vec2 = np.linalg.norm(vec2)
        similarity = dot_product / (norm_vec1 * norm_vec2)

        # Log para verificar valores intermediários
        print(f"dot_product: {dot_product}, norm_vec1: {norm_vec1}, norm_vec2: {norm_vec2}, similarity: {similarity}")

        return similarity
