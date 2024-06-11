from transformers import LlamaForSequenceClassification, LlamaTokenizer

def load_model_and_tokenizer(model_path):
    model = LlamaForSequenceClassification.from_pretrained(model_path)
    tokenizer = LlamaTokenizer.from_pretrained(model_path)
    return model, tokenizer

def predict(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    predictions = outputs.logits.argmax(dim=-1)
    return predictions.item()

if __name__ == "__main__":
    model_path = './llama3-sft'
    model, tokenizer = load_model_and_tokenizer(model_path)

    test_text = "Descrição de um jogo de exemplo"
    prediction = predict(test_text, model, tokenizer)
    print(f"Predição: {prediction}")
