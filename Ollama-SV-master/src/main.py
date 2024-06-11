import joblib
from flask import Flask, request, jsonify
from LanguageModel.vector_store import VectorStore
from LanguageModel.embeddings import gerar_embedding, GamesEmbedding, process_and_store_embeddings
from DataBusiness import preprocess, BaseConnection
import torch

app = Flask(__name__)
vector_store = VectorStore()


# Carregue o vectorizer e o modelo treinado
vectorizer = joblib.load('vectorizer.joblib')
input_dim = len(vectorizer.get_feature_names_out())
embedding_dim = 100
model = GamesEmbedding(input_dim, embedding_dim)
model.load_state_dict(torch.load('model.pth'))
model.eval()

@app.route('/recommend', methods=['POST'])
def recommend():
    user_query = request.json['query']
    processed_query = preprocess.preprocess_text(user_query)

    # Gerar embedding da query
    query_embedding = gerar_embedding(processed_query, model, vectorizer)

    # Log para verificar as dimensões do embedding da query
    print(f"Dimensão do embedding da query: {query_embedding.shape}")
    print(f"Embedding da query: {query_embedding[:5]}...")

    # Buscar recomendações
    recommendations = vector_store.search_similar(query_embedding)

    return jsonify(recommendations)



if __name__ == '__main__':
    app.run(debug=True)
