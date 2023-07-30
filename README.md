# GPT-2 Text Classification API

## Introduction

This repository contains code to deploy a RESTful API for text classification using the GPT-2 model. The API is built using FastAPI, and it allows users to make predictions on text input.

## Instructions to Run the Container

To run the API using Docker, follow these steps:

1. Clone this repository to your local machine.
2. Download the pre-trained model weights from [this link](https://drive.google.com/drive/folders/1Asd376CiAx-us3oFozPMBlTEytnBRYGM?usp=sharing) and place them inside the `weights` folder in the project directory.
3. Open a terminal or command prompt and navigate to the project directory.
4. Build the Docker image using the following command: docker build -t my_fastapi_app .
5. Run the Docker container with the following command: docker run -d -p 8000:8000 --name clasher my_fastapi_app

## Making Predictions

Once the Docker container is running, you can make predictions using the API. To do this, you can use the provided `request.py` script or any other HTTP client, such as Postman.

### Using `request.py`

The `request.py` script allows you to make HTTP POST requests to the API and receive predictions. Follow these steps to use the script:

1. Make sure you have Python installed on your machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Edit the `text` variable in the `request.py` script to provide the input text you want to classify.
4. Run the script with the following command:

### Using Postman or other HTTP clients

You can also use Postman or any other HTTP client to make requests to the API. Send a POST request to `http://localhost:8000/predict` with the input text in the request body as JSON. The response will contain the predicted label.


