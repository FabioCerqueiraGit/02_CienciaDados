import torch
import pandas as pd
from models.train_model import FraudDetectionModel

# Carregar o modelo treinado
model = FraudDetectionModel()
model.load_state_dict(torch.load('../models/model.pth'))
model.eval()

# Função para detectar fraudes
def detect_fraud(transaction):
    transaction = torch.tensor(transaction, dtype=torch.float32)
    with torch.no_grad():
        prediction = model(transaction)
        return (prediction > 0.5).item()

# Exemplo de uso
transaction = [1000, 5000, 4000, 10000, 11000]
is_fraud = detect_fraud(transaction)
print(f'Is Fraud: {is_fraud}')