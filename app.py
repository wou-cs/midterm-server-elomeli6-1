from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/api/calcs/<int:id>", methods=["GET"])
def method_name(id):
    number = int(id)
    num_To_hex = hex(number)
    decrement_num = number - 1

    num_transformations = [{
        "hex": num_To_hex,
        "minus_one": decrement_num
    }]
    return jsonify(num_transformations),200
