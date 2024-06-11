def save_model(model, tokenizer, model_path='./llama3-sft'):
    model.save_pretrained(model_path)
    tokenizer.save_pretrained(model_path)

def preprocess_text(text):
    # Função para pré-processar textos, se necessário
    return text.lower().strip()
