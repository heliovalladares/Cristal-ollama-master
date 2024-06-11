from transformers import Trainer
from src.FineTuning.data.dataset import GameRecommendationDataset
from src.FineTuning.config import get_training_args
from src.FineTuning.data.prepare_data import load_and_prepare_data
from src.FineTuning.models.tokenizer import get_tokenizer
from src.FineTuning.models.llama_model import get_model

def evaluate_model(data_file, model_path):
    # Carregar e preparar dados
    _, val_texts, _, val_labels = load_and_prepare_data(data_file)

    # Inicializar tokenizer e modelo
    tokenizer = get_tokenizer()
    model = get_model().from_pretrained(model_path)

    # Tokenizar dados
    val_encodings = tokenizer(val_texts, truncation=True, padding=True)
    val_dataset = GameRecommendationDataset(val_encodings, val_labels)

    # Configurar argumentos de treinamento
    training_args = get_training_args()

    # Inicializar treinador
    trainer = Trainer(
        model=model,
        args=training_args,
        eval_dataset=val_dataset,
    )

    # Avaliar modelo
    results = trainer.evaluate()
    print(results)

if __name__ == "__main__":
    data_file = 'game_recommendation_queries_unique.csv'
    model_path = './llama3-sft'
    evaluate_model(data_file, model_path)
