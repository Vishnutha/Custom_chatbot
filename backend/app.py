from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Load your model and other necessary components here
import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']

preprocessed_words = data['preprocessed_words']


tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Paaru"
# print("Let's chat! (type 'quit' to exit)")
def get_response_message(sentence):
    
    response_message = ''
    # sentence = input("You: ")
    print("User: "+ sentence )
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, preprocessed_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.45:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response_message = random.choice(intent['responses'])
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        response_message = "I do not understand..."
        print(f"{bot_name}: I do not understand...")
    return response_message

@app.route('/chat', methods=['POST'])
def chat():
    # Get the user input from the request
    user_input = request.json['text']
    print(user_input)
    # Process the user input using your chatbot model
    # Replace this with your actual chatbot logic
    user_input = user_input.lower()
    response = get_response_message(user_input)
    # Return the response
    return jsonify({"response": response})

@app.route('/chat', methods=['GET'])
def chat2():
    # Get the user input from the request
    # user_input = request.json['message']
    # print(user_input)
    # Process the user input using your chatbot model
    # Replace this with your actual chatbot logic
    # response = get_response_message()
    # Return the response
    return jsonify({"response": "Hi This is Virtual Assistant from Paarukutty Bus Travels"})
    

if __name__ == '__main__':
    app.run(debug=True)
