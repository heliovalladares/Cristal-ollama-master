from transformers import AutoTokenizer

def get_tokenizer(token):
    tokenizer = AutoTokenizer.from_pretrained('meta-llama/Meta-Llama-3-8B-Instruct', token=token)
    tokenizer.add_special_tokens({'pad_token': tokenizer.eos_token})
    return tokenizer
