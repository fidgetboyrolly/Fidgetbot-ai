from flask import Flask, request, render_template, jsonify
from main import generate_chat_message  # Make sure generate_chat_message is importable

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = generate_chat_message(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
