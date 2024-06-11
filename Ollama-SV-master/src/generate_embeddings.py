import torch

from LanguageModel.embeddings import process_and_store_embeddings

if __name__ == "__main__":
    model = process_and_store_embeddings()
    torch.save(model.state_dict(), 'model.pth')
    print("Embeddings gerados e armazenados com sucesso.")
