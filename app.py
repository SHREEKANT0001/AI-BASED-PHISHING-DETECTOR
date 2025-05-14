from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os

# Load model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    vectorizer, classifier = pickle.load(file)

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from Flutter

@app.route('/')
def index():
    return "Phishing Detector Backend Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    email_content = data.get('email_content')

    if not email_content:
        return jsonify({'error': 'No email content provided'}), 400

    # Preprocess and predict
    features = vectorizer.transform([email_content])
    prediction = classifier.predict(features)[0]

    return jsonify({'phishing': bool(prediction)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=False, host='0.0.0.0', port=port)

