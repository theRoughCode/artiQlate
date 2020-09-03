from typing import Union
from artiqlate.operation import Operation
import json


class Circuit(object):
    def __init__(self, num_qubits=0, operations=[]):
        super().__init__()
        self.num_qubits = num_qubits
        self.operations = operations

    @staticmethod
    def from_json(json_obj: Union[str, dict]):
        if isinstance(json_obj, str):
            json_obj = json.loads(json_obj)
        num_qubits = json_obj.get("num_qubits", 0)
        operations = [Operation.from_json(x)
                      for x in json_obj.get("operations", [])]
        circ = Circuit(num_qubits, operations)
        return circ

    def __str__(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__, sort_keys=True)

    def __repr__(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__, sort_keys=True)

    def __eq__(self, other):
        if not isinstance(other, Circuit):
            return False
        if self.num_qubits != other.num_qubits:
            return False
        if len(self.operations) != len(other.operations):
            return False
        for a, b in zip(self.operations, other.operations):
            if a != b:
                print(a, b, a == b, a.__eq__(b), type(a), type(b))
                return False
        return True

    def add_qubits(self, num_qubits: int = 1):
        self.num_qubits += num_qubits

    def add_operation(self, operation: Operation):
        self.operations.append(operation)
