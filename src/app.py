from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [
    {
        "label": "Sample Todo 1",
        "done": True
    },
    {
        "label": "Sample Todo 2",
        "done": False
    }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
        todos.pop(position)
        return jsonify(todos)
    else:
        return jsonify({"error": "Invalid position"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
