from flask import Flask, request, jsonify, abort


app = Flask(__name__)


@app.route("/api/calcs/<id>", methods=["GET"])
def integer_transformation(id):
    try:
        number = int(id)
    except ValueError:
        abort(400)
    else:
        number = int(id)
        num_To_hex = hex(number)
        decrement_num = number - 1
        num_transformations = {
            "hex": num_To_hex,
            "dec": decrement_num
        }
    return jsonify(num_transformations),200
