from flask import Flask, request, jsonify
import joblib  # Or appropriate library for loading your model

app = Flask(__name__)

# Load your machine learning model
model = joblib.load('model_Motor.pkl')

@app.route('/')
def home():
    return 'Machine Learning Model API'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['input']])
    return jsonify({'prediction': str(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
