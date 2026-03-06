from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return "Task Manager API is running!"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    tasks.append(data)
    return jsonify({"message": "Task added", "task": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)