from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer once (globally)
model_name = "GroNLP/mdebertav3-subjectivity-arabic"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def predict_subjectivity(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    probs = torch.nn.functional.softmax(logits, dim=1)
    predicted_class = torch.argmax(probs, dim=1).item()
    labels = {0: "Objective", 1: "Subjective"}
    return labels[predicted_class], probs[0][predicted_class].item()
