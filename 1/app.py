from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Estado inicial do chatbot
initial_conversation = [
    "Bom dia, clique:",
    "1 para telefone",
    "2 para internet",
    "3 para encerrar"
]

@app.route('/')
def index():
    return render_template('index.html', conversation=initial_conversation)

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message')

    if user_message == '1':
        response = "Você escolheu telefone. Para consumo tecle 1; Para valor fatura tecle 2; Para encerrar tecle 3."
        clear_chat = False  # Reset chat after showing response
    elif user_message == '2':
        response = "Você escolheu internet. A sua fatura é de 50 reais."
        response += "\n" + "\n".join(initial_conversation[1:])  # Show only the first two options
        clear_chat = False  # Do not clear the chat, just prompt the options again
    elif user_message == '3':
        response = "Conexão encerrada."
        response += "\n" + "\n".join(initial_conversation)  # Reset the conversation to the initial state
        clear_chat = True  # Signal to clear the chat and reset the conversation
    else:
        response = "Opção inválida. Tente novamente."
        clear_chat = False

    return jsonify({"response": response, "clear_chat": clear_chat, "initial_conversation": initial_conversation})

if __name__ == '__main__':
    app.run(debug=True)
