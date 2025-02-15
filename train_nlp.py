import torch
from transformers import GPT4LMHeadModel, GPT4Tokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# Load dataset
dataset = load_dataset('path/to/your/dataset')

# Preprocess dataset
def preprocess_function(examples):
    return tokenizer(examples['text'], truncation=True)
    
tokenizer = GPT4Tokenizer.from_pretrained('gpt-4')
tokenized_datasets = dataset.map(preprocess_function, batched=True)

# Load model
model = GPT4LMHeadModel.from_pretrained('gpt-4')

# Set up training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    weight_decay=0.01,
)

# Train model
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
)

trainer.train()

# Save model
model.save_pretrained("path/to/save/model")
tokenizer.save_pretrained("path/to/save/model")
