from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
model = load_model("model_diabetes.h5")

@app.route("/", methods=["GET"])
def home():
    return "API is running! Use POST /predict to get predictions."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        input_data = np.array(data["input"]).reshape(1, -1)
        prediction = model.predict(input_data)
        result = prediction.tolist()
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
