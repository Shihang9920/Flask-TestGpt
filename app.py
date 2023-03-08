from flask import Flask, render_template, request
import os
import openai

app = Flask(__name__)

openai.api_key = " "
model_engine = "text-davinci-003"


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route("/chat", methods=['POST', 'GET'])
def chat():
    prompt = request.form['prompt']
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,

    )
    message = response.choices[0].text.strip()
    return message


if __name__ == '__main__':
    app.run()
