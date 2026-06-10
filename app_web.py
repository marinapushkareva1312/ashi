from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/journal')
def get_journal():
    try:
        with open("journal.json", "r") as f:
            data = json.load(f)
        return jsonify(data)
    except:
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)