from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

@app.route("/")
def home():
    return "GCP Platform Migration App is running"

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/data")
def data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT now();")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(time=str(result[0]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

