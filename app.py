from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

@app.route("/save-result", methods=["POST"])
def save_result():
    data = request.json

    device_id = data.get("device_id")
    name1 = data.get("name1")
    gender1 = data.get("gender1")
    name2 = data.get("name2")
    gender2 = data.get("gender2")
    percentage = data.get("percentage")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO love_results 
        (device_id, name1, gender1, name2, gender2, percentage)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (device_id, name1, gender1, name2, gender2, percentage))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"status": "ok"}), 201


if __name__ == "__main__":
    app.run()
