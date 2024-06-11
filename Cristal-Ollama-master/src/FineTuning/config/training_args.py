from transformers import TrainingArguments

def get_training_args():
    return TrainingArguments(
        output_dir='./results',
        num_train_epochs=3,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,
        save_total_limit=2,
        save_steps=500,
        evaluation_strategy="epoch",
        load_best_model_at_end=True,
    )
