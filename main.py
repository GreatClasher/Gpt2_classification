# Import necessary libraries
from fastapi import FastAPI
import torch
from transformers import GPT2Tokenizer, GPT2ForSequenceClassification

# Create FastAPI app
app = FastAPI()

# Define the path to the saved model directory
model_path = "weights/garr-epoch-0"

# Load the fine-tuned GPT-2 model and tokenizer from the saved directory
model = GPT2ForSequenceClassification.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Set the padding token to be the EOS token
tokenizer.pad_token = tokenizer.eos_token

# Check if CUDA (GPU) is available, otherwise use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Move the model to the appropriate device (GPU or CPU)
model.to(device)

# Define the /predict endpoint for text classification
@app.get("/predict")
async def predict(text: str):
    # Tokenize the input text and convert it into a PyTorch tensor
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    # Move the tensor to the appropriate device (GPU or CPU)
    inputs = inputs.to(device)

    # Disable gradient computation during prediction
    with torch.no_grad():
        # Use the model to make predictions on the input text
        outputs = model(**inputs)
    
    # Extract the predicted label from the model's output
    predicted_labels = torch.argmax(outputs.logits, dim=-1)

    # Convert the predicted label from a tensor to an integer
    predicted_label = predicted_labels.item()

    # Return the predicted label as a JSON response
    return {"predicted_label": predicted_label}

# Run the FastAPI app using uvicorn server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)