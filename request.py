# Import the requests library to send HTTP requests
import requests

# Define the input text that you want to predict the label for
text = "5 more suspected omicron cases in tn among the five is a woman passenger who flew from the republic of congo in africa the other four are the relatives of the person who has already tested positive"

# Send a GET request to the FastAPI server running at http://localhost:8000/predict
response = requests.get(f"http://localhost:8000/predict/?text={text}")

# Parse the response JSON data returned by the server
data = response.json()

# Extract the predicted label from the response data
predicted_label = data["predicted_label"]

# Print the predicted label
print(f"Predicted label: {predicted_label}")
