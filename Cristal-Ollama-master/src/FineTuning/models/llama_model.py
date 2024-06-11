from transformers import LlamaForSequenceClassification
from dotenv import load_dotenv
import os

load_dotenv()
use_auth_token = os.getenv('HUGGINGFACE_TOKEN')

def get_model(token):
    model = LlamaForSequenceClassification.from_pretrained('meta-llama/Meta-Llama-3-8B-Instruct', token=token)
    return model
