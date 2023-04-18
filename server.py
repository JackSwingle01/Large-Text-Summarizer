from flask import Flask, render_template, request
from completions import get_summary

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.get_json().get('text')
    if not text:
        return "No text provided"
    print(f"TEXT: {text}")
    summary = get_summary(text)
    print (summary)
    return summary


if __name__ == '__main__':
    app.run()
