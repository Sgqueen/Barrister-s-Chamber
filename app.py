from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def ai_legal_response(question):
    if "tenant" in question.lower():
        return "Tenants have the right to live in a safe, well-maintained home. Landlords cannot evict without notice."
    elif "consumer" in question.lower():
        return "Consumers have the right to return defective products and get refunds under consumer protection laws."
    else:
        return "I'm not sure. Please consult a lawyer for accurate advice."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_question = request.json.get("question")
        response = ai_legal_response(user_question)
        return jsonify({"response": response})
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
