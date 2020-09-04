from artiqlate.circuit import Circuit
from artiqlate.operation import Operation
from artiqlate.wit_agent import handle_message
import pytest


def test_create_circuit():
    expected = Circuit()
    assert handle_message('invalid') == expected

    expected = Circuit(3)
    assert handle_message('create circuit with 3 qubits') == expected

    expected = Circuit(1)
    assert handle_message('create circuit with 1 qubit') == expected
    assert handle_message('create circuit with a qubit') == expected

def test_add_qubits():
    expected = Circuit()
    assert handle_message('create new circuit') == expected
    expected = Circuit(1)
    assert handle_message('add 1 qubit') == expected
    expected = Circuit(3)
    assert handle_message('add 2 qubits') == expected

def test_apply_gates():
    expected = Circuit(3)
    assert handle_message('create new circuit with 3 qubits') == expected

    # Test single qubit
    expected.add_operation(Operation('H', [0]))
    assert handle_message('apply H gate on qubit 0') == expected
    expected.add_operation(Operation('X', [1]))
    assert handle_message('apply X gate on qubit 1') == expected

    # Test no qubits
    assert handle_message('apply X gate') == expected

    # Test invalid qubits
    assert handle_message('apply X gate on qubit 3') == expected

    # Test multiple qubits
    expected.add_operation(Operation('CNOT', [1, 2]))
    assert handle_message('apply CNOT on qubits 1 and 2') == expected
    # Add qubit
    expected.add_qubits(1)
    assert handle_message('add 1 qubit') == expected
    expected.add_operation(Operation('U', [1, 2, 3]))
    assert handle_message('apply U gate on qubits 1, 2, and 3') == expected
    expected.add_operation(Operation('U', [1, 2, 0]))
    assert handle_message('apply U gate on qubits 1, 2, and 3') != expected

