from transformers import Trainer, TrainingArguments
from dotenv import load_dotenv
import os
from src.FineTuning.data.prepare_data import load_and_prepare_data
from src.FineTuning.models.tokenizer import get_tokenizer
from src.FineTuning.models.llama_model import get_model
from src.FineTuning.data.dataset import GameRecommendationDataset

def train_model(data_file, model_path):
    # Carregar e preparar dados
    train_texts, val_texts, train_labels, val_labels = load_and_prepare_data(data_file)

    # Carregar variáveis de ambiente do arquivo .env
    load_dotenv()
    token = os.getenv('HUGGINGFACE_TOKEN')

    # Inicializar tokenizer e modelo
    tokenizer = get_tokenizer(token=token)
    model = get_model(token=token)

    # Adicionar tokens especiais ao modelo
    model.resize_token_embeddings(len(tokenizer))

    # Tokenizar dados
    train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=512)
    val_encodings = tokenizer(val_texts, truncation=True, padding=True, max_length=512)
    train_dataset = GameRecommendationDataset(train_encodings, train_labels)
    val_dataset = GameRecommendationDataset(val_encodings, val_labels)

    # Configurar argumentos de treinamento
    training_args = TrainingArguments(
        output_dir=model_path,          # Diretório para salvar os resultados
        num_train_epochs=3,             # Número de épocas
        per_device_train_batch_size=8,  # Tamanho do lote para treinamento
        per_device_eval_batch_size=8,   # Tamanho do lote para avaliação
        warmup_steps=500,               # Passos de aquecimento
        weight_decay=0.01,              # Decaimento de peso
        logging_dir='./logs',           # Diretório de logs
        logging_steps=10,
    )

    # Inicializar treinador
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        tokenizer=tokenizer
    )

    # Treinar modelo
    trainer.train()

    # Salvar modelo
    trainer.save_model(model_path)

if __name__ == "__main__":
    data_file = 'game_recommendation_queries_unique.csv'
    model_path = './llama3-sft'
    train_model(data_file, model_path)
