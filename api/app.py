from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

# Get the absolute path to the directory where this file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Read files using absolute paths
with open(os.path.join(BASE_DIR, "..", "generated.txt"), "r", encoding="utf-8") as f:
    GEN = [line.strip() for line in f if line.strip()]

with open(os.path.join(BASE_DIR, "..", "words.txt"), "r", encoding="utf-8") as f:
    WORDS = [line.strip() for line in f if line.strip()]

@app.route("/")
def home():
    return "Polish words API is running"

@app.route("/pl/gen")
def gen():
    words = random.sample(GEN, min(10, len(GEN)))
    return jsonify({"gen": words})

@app.route("/pl/real")
def real():
    words = random.sample(WORDS, min(10, len(WORDS)))
    return jsonify({"words": words})

# This is the key part for Vercel – export the app object
# DO NOT call app.run() here! 
