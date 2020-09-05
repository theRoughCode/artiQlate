from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from artiqlate.circuit import Circuit
from artiqlate.cirq_agent import generate_circuit
from artiqlate.wit_agent import handle_message
import io
import base64
import json
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)
cors = CORS(app)


@app.route('/message', methods=['POST'])
@cross_origin()
def receive_message():
    message = request.form['message']
    if "circuit" in request.form:
        circuit_str = json.loads(request.form['circuit'])
        circuit = Circuit.from_json(circuit_str)
        circuit = handle_message(message, circuit)
    else:
        circuit = handle_message(message)
    if circuit is None:
        return jsonify(circuit=request.form['circuit'])
    qc = generate_circuit(circuit)
    if qc is None:
        return jsonify(circuit=str(circuit))
    img = qc.draw('mpl')
    output = io.BytesIO()
    FigureCanvas(img).print_png(output)
    img_str = base64.b64encode(output.getvalue()).decode()
    return jsonify(circuit=str(circuit), img=img_str)

@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
