from typing import Union
import json


class Operation(object):
    def __init__(self, label="", targets=[]):
        super().__init__()
        self.label = label
        self.targets = targets

    @staticmethod
    def from_json(json_obj: Union[str, dict]):
        if isinstance(json_obj, str):
            json_obj = json.loads(json_obj)
        label = json_obj.get("label", "")
        targets = json_obj.get("targets", [])
        return Operation(label, targets)

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return json.dumps(self.__dict__)

    def __eq__(self, other):
        if not isinstance(other, Operation):
            return False
        if self.label != other.label:
            return False
        if len(self.targets) != len(other.targets):
            return False
        return all([a == b for (a, b) in zip(self.targets, other.targets)])
