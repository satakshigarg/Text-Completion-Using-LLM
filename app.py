# app.py

from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_suggestions', methods=['POST'])
def get_suggestions():
    user_input = request.form['user_input']
    
    # Use OpenAI GPT-3 to get text suggestions
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=50
    )
    
    suggestion = response['choices'][0]['text'].strip()
    
    return jsonify({'suggestion': suggestion})

if __name__ == '__main__':
    app.run(debug=True)
