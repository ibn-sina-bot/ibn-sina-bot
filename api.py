from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from ibn_sina_dict import get_response

app = Flask(__name__)
CORS(app)

# ذاكرة مؤقتة بسيطة (قاموس)
chat_memory = {}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    # استخدم user_id لو موجود، وإلا استخدم الـ IP
    user_id = data.get('user_id', request.remote_addr)

    # لو المستخدم جديد، نضيفه في الذاكرة
    if user_id not in chat_memory:
        chat_memory[user_id] = []

    # نضيف سؤال المستخدم للذاكرة
    chat_memory[user_id].append({"role": "user", "message": message})

    # نجيب الرد من البوت
    response = get_response(message)

    # نضيف رد البوت للذاكرة
    chat_memory[user_id].append({"role": "bot", "message": response})

    return jsonify({'reply': response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
