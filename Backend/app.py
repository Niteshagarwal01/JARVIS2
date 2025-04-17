from flask import Flask, request, jsonify
from Chatbot import ChatBot  # Import the ChatBot function directly from your Chatbot.py file
from flask_cors import CORS  # You'll need to install this: pip install flask-cors


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Check if 'message' is in the request data
        if 'message' not in data:
            return jsonify({'error': 'No message provided'}), 400
        
        # Get the user's message
        user_message = data['message']
        
        # Get response from ChatBot function imported from Chatbot.py
        response = ChatBot(user_message)
        
        # Return the response as JSON
        return jsonify({'response': response})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)