from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

model = ChatGoogleGenerativeAI(google_api_key="AIzaSyA1aRoJIbD5zPt0kEZCugKNtTvCjG7QJpM", model="gemini-1.5-flash")

chat_history = []
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    query = data['question']
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
