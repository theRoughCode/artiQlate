from artiqlate.circuit import Circuit
from artiqlate.operation import Operation
from artiqlate.wit_agent import handle_message
import pytest


def test_create_circuit():
    assert handle_message('invalid') is None
    expected = Circuit
    assert handle_message('invalid', expected) == expected

    expected = Circuit(3)
    assert handle_message('create circuit with 3 qubits') == expected

    expected = Circuit(1)
    assert handle_message('create circuit with 1 qubit') == expected
    assert handle_message('create circuit with a qubit') == expected

def test_add_qubits():
    expected = Circuit()
    circ = handle_message('create new circuit')
    assert circ == expected
    expected = Circuit(1)
    circ = handle_message('add 1 qubit', circ)
    assert circ == expected
    expected = Circuit(3)
    circ = handle_message('add 2 qubits', circ)
    assert circ == expected

def test_apply_gates():
    expected = Circuit(3)
    circ = handle_message('create new circuit with 3 qubits')
    assert circ == expected

    # Test single qubit
    expected.add_operation(Operation('H', [0]))
    circ = handle_message('apply H gate on qubit 0', circ)
    assert circ == expected
    expected.add_operation(Operation('X', [1]))
    circ = handle_message('apply X gate on qubit 1', circ)
    assert circ == expected

    # Test no qubits
    assert handle_message('apply X gate', circ) == expected

    # Test invalid qubits
    assert handle_message('apply X gate on qubit 3', circ) == expected

    # Test multiple qubits
    expected.add_operation(Operation('CNOT', [1, 2]))
    circ = handle_message('apply CNOT on qubits 1 and 2', circ)
    assert circ == expected
    # Add qubit
    expected.add_qubits(1)
    circ = handle_message('add 1 qubit', circ)
    assert circ == expected
    expected.add_operation(Operation('U', [1, 2, 3]))
    circ = handle_message('apply U gate on qubits 1, 2, and 3', circ)
    assert circ == expected
    expected.add_operation(Operation('U', [1, 2, 0]))
    circ = handle_message('apply U gate on qubits 1, 2, and 3', circ)
    assert circ != expected

