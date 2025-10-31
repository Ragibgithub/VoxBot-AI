from flask import Flask, request, jsonify
from main import process_user_input  # Yeh tumhare backend ka main function hoga
import features  # Tumhara features.py

app = Flask(__name__)

@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' in request"}), 400
    user_input = data["text"]
    try:
        response = process_user_input(user_input)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/features", methods=["GET"])
def get_features():
    try:
        feat_list = features.get_feature_list()  # Tumhare features.py me ek function hona chahiye
        return jsonify({"features": feat_list})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
