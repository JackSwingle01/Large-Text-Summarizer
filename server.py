from flask import Flask, render_template, request
from chunking import summarize_long_text
from flask_cors import CORS

# For testing chunking methods
# from chunking import clear_file, save_chunk_summary_to_file, read_file, split_string_to_chunks

app = Flask(__name__)

CORS(app, origins=['http://localhost:5000'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.get_json().get('text')
    summary_size = request.get_json().get('summary_size')
    if not text:
        return "No text provided"

    summary = summarize_long_text(text, max_summary_size=summary_size)

    return summary


if __name__ == '__main__':
    app.run()

    # Chunking methods testing
    # clear_file()
    # save_chunk_summary_to_file("Summary goes here.\n")
    # read_file()
    # split_string_to_chunks(read_file())
