from transformers import AutoTokenizer, AutoModel
import torch


# Download and load
tokenizer = AutoTokenizer.from_pretrained("UBC-NLP/MARBERT")
marbert = AutoModel.from_pretrained("UBC-NLP/MARBERT")

# Example Arabic sentence
def embeddings(sentence):
    # Tokenize input
    inputs = tokenizer(sentence, return_tensors="pt")

    # Disable gradient calculation
    with torch.no_grad():
        outputs = marbert(**inputs)

    # Get sentence embedding from [CLS] token
    cls_embedding = outputs.last_hidden_state[:, 0, :]  # shape: (1, 768)
    return cls_embedding
