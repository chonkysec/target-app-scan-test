import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.get("/v1/merchants/lookup")
def lookup_merchant():
    """Look up a merchant by trading name."""
    name = request.args.get("name", "")
    conn = sqlite3.connect("paylink.db")
    sql = "SELECT id, display_name FROM merchants WHERE display_name = ?"
    rows = conn.execute(sql, (name,)).fetchall()
    return jsonify([{"id": r[0], "name": r[1]} for r in rows])
