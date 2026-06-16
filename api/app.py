from flask import Flask, jsonify
import random

app = Flask(__name__)

with open("generated.txt", "r", encoding="utf-8") as f:
    GEN = [line.strip() for line in f if line.strip()]

with open("words.txt", "r", encoding="utf-8") as f:
    WORDS = [line.strip() for line in f if line.strip()]

@app.route("/")
def home():
    return "Polish words API is running"

@app.route("/favicon.ico")
def favicon():
    return "", 204

@app.route("/pl/gen")
def gen():
    words = random.sample(GEN, min(10, len(GEN)))
    return jsonify({"gen": words})

@app.route("/pl/real")
def real():
    words = random.sample(WORDS, min(10, len(WORDS)))
    return jsonify({"words": words})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    