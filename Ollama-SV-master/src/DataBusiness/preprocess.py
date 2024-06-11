# Preprocessa as descrições dos jogos para tokenização e vetorização.
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_text(text):
    if not isinstance(text, str):
        text = str(text) if text is not None else ''
    text = text.lower()  # Converter para minúsculas
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)  # Remover pontuação
    text = re.sub(r'\d+', '', text)  # Remover números
    text = text.strip()  # Remover espaços em branco extra
    return text

def vectorize_texts(texts):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    return X, vectorizer
