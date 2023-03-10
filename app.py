
from flask import Flask, jsonify, request,render_template
from flask_ngrok import run_with_ngrok
import os
import openai
app = Flask(__name__)

run_with_ngrok(app)
openai.api_key = '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'
book = ("reply only from shreemad bhagvad gita book")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prompt', methods=['POST'])
def prompt():
    # Get the prompt from the request
    prompt = request.form.get("prompt")

    # Use OpenAI API to generate a response from the Shreemad Bhagvad Gita book
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt + book ,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Return the response
    return response.choices[0].text

if __name__ == '__main__':
    app.run()
# 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