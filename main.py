from artiqlate.cirq_agent import generate_circuit
import artiqlate.wit_agent as WitAgent

circ = WitAgent.handle_message('create circuit with 3 qubits')
circ = WitAgent.handle_message('apply x gate on qubit 1')
circ = WitAgent.handle_message('apply CNOT gate on qubit 0 and 2')
print(circ)

qc = generate_circuit(circ)
img = qc.draw('mpl', filename="circuit.png")
