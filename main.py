from artiqlate.cirq_agent import generate_circuit
import artiqlate.wit_agent as WitAgent

circ = WitAgent.handle_message('create circuit with 3 qubits')
circ = WitAgent.handle_message('apply x gate on qubit 1', circ)
circ = WitAgent.handle_message('apply CNOT gate on qubit 0 and 2', circ)
print(circ)

qc = generate_circuit(circ)
print(qc.draw())
