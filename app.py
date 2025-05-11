
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
vectorizer, model = pickle.load(open("model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    email_content = data.get("email", "")
    features = vectorizer.transform([email_content])
    prediction = model.predict(features)[0]
    return jsonify({"phishing": bool(prediction)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
