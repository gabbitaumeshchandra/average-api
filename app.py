
from flask import Flask, request, jsonify
import math

app = Flask(__name__)

# Store numbers received from requests
numbers = []


@app.route("/average", methods=["POST"])
def average():
    """Add a number and return the average of all numbers."""

    if not request.is_json:
        return jsonify({"error": "Please send JSON data"}), 415

    data = request.get_json(silent=True)

    # Accept either a number or {"number": number}
    if isinstance(data, dict):
        number = data.get("number")
    else:
        number = data

    # Check whether the input is a valid number
    if isinstance(number, bool) or not isinstance(number, (int, float)):
        return jsonify({"error": "Please provide a valid number"}), 400

    if not math.isfinite(number):
        return jsonify({"error": "Number must be finite"}), 400

    numbers.append(number)

    result = sum(numbers) / len(numbers)

    return jsonify({"average": result})


if __name__ == "__main__":
    app.run(debug=True)
