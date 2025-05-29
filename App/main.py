
from flask import Flask, jsonify
from App.db import get_connection

app = Flask(__name__)

@app.route('/users')
def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify([{"id": u[0], "name": u[1]} for u in users])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

