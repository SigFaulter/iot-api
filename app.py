from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return "test"

if __name__ == '__main__':
    app.run(debug=True)
