from artiqlate.operation import Operation
import pytest


def test_equality():
    a = Operation()
    b = Operation()
    assert a == b

    a = Operation("H")
    b = Operation("H")
    assert a == b
    b = Operation("X")
    assert a != b

    a = Operation(targets=[0])
    b = Operation(targets=[0])
    assert a == b
    b = Operation(targets=[1])
    assert a != b

    a = Operation(targets=[0, 2])
    b = Operation(targets=[0, 2])
    assert a == b
    b = Operation(targets=[1, 2])
    assert a != b
    b = Operation(targets=[0, 1])
    assert a != b

    a = Operation("H", [0])
    b = Operation("H", [0])
    assert a == b

def test_operation_from_json():
    expected = Operation()
    assert Operation.from_json('{}') == expected

    expected = Operation("H")
    assert Operation.from_json('{"label": "H"}') == expected
    assert Operation.from_json('{"label": "Z"}') != expected

    expected = Operation(targets=[0])
    op = Operation.from_json('{"targets": [0]}')
    assert isinstance(op.targets[0], int)
    assert Operation.from_json('{"targets": [0]}') == expected
    assert Operation.from_json('{"targets": [1]}') != expected
