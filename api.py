from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from ibn_sina_dict import get_response

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    response = get_response(message)
    return jsonify({'reply': response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
