from flask import Flask, request, jsonify
from database.redisDB.redis_operations import RedisOperations
from rag_model import RAGModel
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize Redis and RAGModel
redis_operations = RedisOperations(host='localhost', port=6380)
rag_model = RAGModel("openai")

# API to handle user questions
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get('question')
    session_id = data.get('session_id')

    if not question or not session_id:
        return jsonify({"error": "Both 'question' and 'session_id' are required"}), 400

    # Retrieve chat history
    chat_history = redis_operations.get_chat_history(session_id)

    # Clear old chat history if limit exceeded
    if len(chat_history) >= 8:
        redis_operations.clear_chat_history(session_id)
        chat_history = []

    # Generate response using RAGModel
    rag_response = rag_model.generate_response(question=question, chat_history=chat_history)

    # Store response in Redis
    redis_operations.store_chat_history(session_id, question, rag_response)

    return jsonify({
        "session_id": session_id,
        "question": question,
        "response": rag_response
    })

# API to retrieve chat history
@app.route('/api/history/<session_id>', methods=['GET'])
def history(session_id):
    chat_history = redis_operations.get_chat_history(session_id)
    return jsonify(chat_history)

if __name__ == '__main__':
    app.run(debug=True)
