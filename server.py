from flask import Flask, request, jsonify

app = Flask(__name__)

current_command = None


@app.route("/")
def home():
    return "BalanceBot server working"


@app.route("/set_command", methods=["GET", "POST"])
def set_command():
    global current_command

    if request.method == "POST":
        data = request.json
        current_command = data.get("command")
    else:
        current_command = request.args.get("command")

    return jsonify({"status": "command set", "command": current_command})

@app.route("/get_command")
def get_command():
    global current_command
    return {"command": current_command}


@app.route("/clear_command")
def clear_command():
    global current_command
    current_command = None
    return {"status": "cleared"}


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)