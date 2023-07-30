from fastapi import FastAPI
import torch
from transformers import GPT2Tokenizer, GPT2ForSequenceClassification

app = FastAPI()

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_path = "weights/garr-epoch-0"
model = GPT2ForSequenceClassification.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

@app.get("/predict")
async def predict(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    inputs = inputs.to(device)
    with torch.no_grad():
        outputs = model(**inputs)
        
    predicted_labels = torch.argmax(outputs.logits, dim=-1)
    predicted_label = predicted_labels.item()
    return {"predicted_label": predicted_label}
 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
