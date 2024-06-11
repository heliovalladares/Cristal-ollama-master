from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
import faiss

from DataBusiness import BaseConnection

app = Flask(__name__)

connection = BaseConnection()
embeddings_db = connection.embeddings

# Carregar o modelo e o tokenizer
model_path = "./llama3-sft"  # Substitua pelo caminho do seu modelo treinado
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path)


# Carregar embeddings do mongodb
game_embeddings = list(embeddings_db.find({}, {"_id": 0, "embedding": 1, "game": 1}))
embeddings = np.array([game["embedding"] for game in game_embeddings]).astype("float32")
game_names = [game["game"] for game in game_embeddings]


# Criar FAISS
d = embeddings.shape[1] # dimensão dos embeddings
index = faiss.IndexFlatL2(d) # Index de similaridade L2 (distância euclidiana)
index.add(embeddings)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    query = data.get('query')

    # Processar a query e gerar embeddings
    inputs = tokenizer(query, return_tensors="pt", max_length=4096, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).tolist()

    # Aqui você pode adicionar a lógica de recomendação com base nos embeddings
    recommendations = generate_recommendations(embeddings)

    return jsonify(recommendations)


def generate_recommendations(embeddings):
    # Lógica de recomendação
    # Exemplo simples de retorno
    return {"recommendations": ["Game1", "Game2", "Game3"]}


if __name__ == '__main__':
    app.run(debug=True)
