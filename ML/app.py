from flask import Flask, request, jsonify, render_template
from chat import chatbot

app = Flask(__name__)

@app.route("/")
def start():
    return render_template('home.html')

@app.route("/chat", methods=['GET'])
def chat_page():
    return render_template('chat.html')

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("messageText")  
    response = chatbot(user_input) 
    
    return jsonify({"answer": response})  


if __name__ == '__main__':
    app.run(debug=True)
