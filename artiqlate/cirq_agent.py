from qiskit import QuantumCircuit, ClassicalRegister
from artiqlate.circuit import Circuit
from artiqlate.operation import Operation
import numpy as np


def apply_operation(qc: QuantumCircuit, op: Operation):
    label = op.label.lower()
    targets = op.targets
    if len(targets) == 0:
        raise Exception(
            "No target qubits found for operation: {}".format(str(op)))
    if label == "h":
        for t in targets:
            qc.h(t)
    elif label == "x":
        for t in targets:
            qc.x(t)
    elif label == "y":
        for t in targets:
            qc.y(t)
    elif label == "z":
        for t in targets:
            qc.z(t)
    elif label == "cnot":
        if len(targets) != 2:
            raise Exception(
                "CNOT requires 2 target qubits. Found: {}".format(len(targets)))
        qc.cnot(*targets)
    elif label == "ccnot":
        if len(targets) != 3:
            raise Exception(
                "CNOT requires 3 target qubits. Found: {}".format(len(targets)))
        qc.ccx(*targets)
    elif label == 'measure':
        cr = ClassicalRegister(len(targets))
        qc.add_register(cr)
        qc.measure(targets, cr)
    else:
        u = np.eye(pow(2, len(targets)))
        qc.unitary(u, targets, label=op.label)


def generate_circuit(circuit: Circuit) -> QuantumCircuit:
    if circuit.num_qubits == 0:
        print("No qubits found. Please add more qubits!")
        return None
    qc = QuantumCircuit(circuit.num_qubits)
    for op in circuit.operations:
        apply_operation(qc, op)
    return qc
