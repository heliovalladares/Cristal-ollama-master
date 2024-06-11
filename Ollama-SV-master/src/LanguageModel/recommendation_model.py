# Define e treina o modelo de recomendação.
import torch
import torch.nn as nn
import torch.optim as optim

class RecommendationModel(nn.Module):
    def __init__(self, embedding_dim):
        super(RecommendationModel, self).__init__()
        self.fc = nn.Linear(embedding_dim, 1)

    def forward(self, x):
        return torch.sigmoid(self.fc(x))

def train_model(train_embeddings, train_labels, embedding_dim, num_epochs=10):
    model = RecommendationModel(embedding_dim)
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters())

    for epoch in range(num_epochs):
        optimizer.zero_grad()
        outputs = model(train_embeddings)
        loss = criterion(outputs, train_labels)
        loss.backward()
        optimizer.step()

    return model