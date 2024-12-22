import redis
import uuid
import json
from datetime import datetime


class RedisOperations:
    def __init__(self, host='localhost', port=6380):
        self.redis_client = redis.Redis(host=host, port=port, decode_responses=True)

    def store_chat_history(self, session_id, question, response):
        """Store chat history in Redis."""
        history_key = f"chat_history:{session_id}"
        chat_entry = {
            "id": str(uuid.uuid4()),
            "question": question,
            "response": response,
            "timestamp": datetime.utcnow().isoformat()  # Add UTC timestamp
        }
        self.redis_client.rpush(history_key, json.dumps(chat_entry))

    def get_chat_history(self, session_id):
        """Retrieve chat history from Redis, sorted by timestamp."""
        history_key = f"chat_history:{session_id}"
        chat_history = self.redis_client.lrange(history_key, 0, -1)
        parsed_history = [json.loads(entry) for entry in chat_history]
        return sorted(parsed_history, key=lambda x: x['timestamp'])

    def clear_chat_history(self, session_id):
        """Remove chat history for a session ID."""
        history_key = f"chat_history:{session_id}"
        self.redis_client.delete(history_key)
