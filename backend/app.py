from flask import Flask, request, jsonify
from flask_cors import CORS
from api.vision import analyze_chart
from api.backtest import run_backtest

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    image = data.get('imageBase64')
    uid = data.get('uid')
    result = analyze_chart(image, uid)
    return jsonify(result)

@app.route('/api/backtest', methods=['POST'])
def backtest():
    file = request.files['file']
    entry = float(request.form.get('entry'))
    sl = float(request.form.get('stop_loss'))
    tp = float(request.form.get('take_profit'))
    result = run_backtest(file, entry, sl, tp)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)