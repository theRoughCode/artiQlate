from artiqlate.circuit import Circuit
from artiqlate.operation import Operation
import pytest


def test_equality():
    a = Circuit()
    b = Circuit()
    assert a == b

    a = Circuit(2)
    b = Circuit(2)
    assert a == b
    b = Circuit(1)
    assert a != b

    a = Circuit(operations=[Operation("H", [0])])
    b = Circuit(operations=[Operation("H", [0])])
    assert a == b
    b = Circuit(operations=[Operation("Z", [0])])
    assert a != b

    a = Circuit(2, [Operation("H", [0])])
    b = Circuit(2, [Operation("H", [0])])
    assert a == b


def test_create_circuit():
    circ = Circuit()
    assert circ.num_qubits == 0
    assert circ.operations == []

    circ = Circuit(2)
    assert circ.num_qubits == 2
    assert circ.operations == []

    operations = [Operation('H', [0])]
    circ = Circuit(operations=operations)
    assert circ.num_qubits == 0
    assert circ.operations == operations

    circ = Circuit(2, operations)
    assert circ.num_qubits == 2
    assert circ.operations == operations


def test_circuit_from_json():
    expected = Circuit()
    assert Circuit.from_json('{}') == expected

    expected = Circuit(2)
    assert Circuit.from_json('{"num_qubits": 2}') == expected
    expected = Circuit(1)
    assert Circuit.from_json('{"num_qubits": 2}') != expected

    expected = Circuit(operations=[Operation("H", [0])])
    circ = Circuit.from_json('{"num_qubits": 0, "operations": [{"label": "H", "targets": [0]}]}')
    assert isinstance(circ.operations[0], Operation)
    assert circ == expected, str(circ)
