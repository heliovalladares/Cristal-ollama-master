# Gera embeddings das descrições dos jogos.
from DataBusiness import BaseConnection, preprocess
import torch
import torch.nn as nn
import numpy as np
from LanguageModel.vector_store import VectorStore
import joblib


class GamesEmbedding(nn.Module):
    def __init__(self, input_dim, embedding_dim):
        super(GamesEmbedding, self).__init__()
        self.embedding = nn.Linear(input_dim, embedding_dim)

    def forward(self, x):
        embedded = self.embedding(x)
        return embedded


def gerar_embedding(descricao, model, vectorizer):
    descricao_vector = vectorizer.transform([descricao]).toarray()
    descricao_tensor = torch.from_numpy(descricao_vector).float()
    embedding = model(descricao_tensor)
    return embedding.squeeze(0).detach().numpy()


def process_and_store_embeddings():
    BaseConnection.charging_collections_in_dataframe()
    df_games = BaseConnection.df_games

    df_games['cleaned_description'] = df_games['description'].apply(preprocess.preprocess_text)

    X, vectorizer = preprocess.vectorize_texts(df_games['cleaned_description'])

    # Configurar a Vector Store
    vector_store = VectorStore()
    input_dim = X.shape[1]
    embedding_dim = 100
    model = GamesEmbedding(input_dim, embedding_dim)

    # Gerar e armazenar embeddings
    for index, row in df_games.iterrows():
        embedding = gerar_embedding(row['cleaned_description'], model, vectorizer)

        # Log para verificar os valores dos embeddings
        print(f"Embedding para {row['title']}: {embedding[:5]}...")

        metadata = {
            "title": row['title'],
            "description": row['description'],
            "genres": row['genres'],
            "platforms": row['plataforms']
        }
        vector_store.save_embedding(str(row['_id']), embedding, metadata)

    # Salvando o vectorizer treinado
    joblib.dump(vectorizer, 'vectorizer.joblib')
    return model

