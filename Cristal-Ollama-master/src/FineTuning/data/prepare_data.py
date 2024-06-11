import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import LlamaTokenizer

def load_and_prepare_data(file_path):
    data = pd.read_csv(file_path)
    train_texts, val_texts, train_labels, val_labels = train_test_split(
        data['text'], data['label'], test_size=0.2
    )
    return train_texts.tolist(), val_texts.tolist(), train_labels.tolist(), val_labels.tolist()
