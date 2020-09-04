import artiqlate.wit_agent as WitAgent

circ = WitAgent.handle_message('create circuit with 3 qubits')
circ = WitAgent.handle_message('apply x gate on qubit 1')
print(circ)
