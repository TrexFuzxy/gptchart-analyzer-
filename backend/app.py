from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ✅ Health check route
@app.route("/api/test", methods=["GET"])
def test_api():
    return jsonify({"message": "API working!"}), 200

# Example future endpoint
@app.route("/api/analyze", methods=["POST"])
def analyze_chart():
    return jsonify({"message": "Chart analysis coming soon"}), 200

# 🟢 Required for Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
