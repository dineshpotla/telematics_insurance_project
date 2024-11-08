from flask import Flask, request, jsonify
import pickle

# Load the model
model = pickle.load(open("models/gb_model.pkl", "rb"))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [data['avg_speed'], data['risk_score']]
    prediction = model.predict([features])
    return jsonify({'risk_prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
