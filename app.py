from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from artiqlate.circuit import Circuit
from artiqlate.cirq_agent import generate_circuit
from artiqlate.wit_agent import handle_message
import json

app = Flask(__name__)
cors = CORS(app)


@app.route('/message', methods=['POST'])
@cross_origin()
def receive_message():
    message = request.form['message']
    if "circuit" in request.form:
        circuit_str = json.loads(request.form['circuit'])
        print(circuit_str)
        circuit = Circuit.from_json(circuit_str)
        circuit = handle_message(message, circuit)
    else:
        circuit = handle_message(message)
    if circuit is None:
        return jsonify(circuit=str(circuit))
    qc = generate_circuit(circuit)
    if qc is None:
        return jsonify(circuit=str(circuit))
    img = qc.draw()
    return jsonify(circuit=str(circuit), img=str(img))

@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
