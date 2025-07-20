from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments

# Load the pre-trained DeepSeek model and tokenizer
model_name = "deepseek-ai/deepseek-llm"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Print the model architecture (optional)
print(model)