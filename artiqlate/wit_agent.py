from wit import Wit
from dotenv import load_dotenv
from pathlib import Path
from typing import List, Union
from artiqlate.circuit import Circuit
from artiqlate.operation import Operation
from artiqlate.utils import text2int
import os
import artiqlate.entities as ENTITIES
import artiqlate.intents as INTENTS

env_path = Path('.') / '.env'
load_dotenv(env_path)
WIT_API_KEY = os.getenv("WIT_API_KEY")

client = Wit(WIT_API_KEY)


def get_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val


def get_num_qubits(entities: dict) -> int:
    entity_val = get_entity_value(entities, ENTITIES.NUM_QUBITS)
    if entity_val is None:
        return 0
    num_qubits = entity_val.split()[0]
    return int(num_qubits) if num_qubits.isdigit() else text2int(num_qubits)


def get_qubit_ids(entities: dict, max_qubits: int) -> List[int]:
    entity_val = get_entity_value(entities, ENTITIES.QUBIT_ID)
    if entity_val is None:
        return []
    entity_val = entity_val.replace(',', '')
    if "all" in entity_val:
        return list(range(0, max_qubits))
    qubit_ids = [s for s in map(text2int, entity_val.split()) if isinstance(s, int)]
    return qubit_ids


def get_gate_type(entities: dict) -> str:
    entity_val = get_entity_value(entities, ENTITIES.GATE_TYPE)
    if entity_val is None or len(entity_val) == 0:
        return None
    gate_type = entity_val.split()[0]
    return gate_type[0].upper() + gate_type[1:]


def handle_intent(intent: str, entities: dict, circuit: Circuit) -> Circuit:
    if intent == INTENTS.ADD_QUBITS:
        # Add qubits to circuit
        num_qubits = get_num_qubits(entities)
        if circuit is None:
            circuit = Circuit(num_qubits)
        else:
            circuit.add_qubits(num_qubits)
    elif intent == INTENTS.APPLY_GATE:
        # Apply gate to circuit
        if circuit is None:
            print("No circuit created.")
            return circuit
        # Get target qubit IDs
        qubit_ids = get_qubit_ids(entities, circuit.num_qubits)
        if len(qubit_ids) == 0:
            print("No target qubits found.")
            return circuit
        max_id = max(qubit_ids)
        if circuit.num_qubits <= max_id:
            print("Invalid qubit id {} found. Max qubit id: {}.".format(
                max_id, circuit.num_qubits - 1))
            return circuit
        # Get gate type
        gate_type = get_gate_type(entities)
        if gate_type is None:
            print("No gate type found.")
            return circuit
        op = Operation(gate_type, qubit_ids)
        circuit.add_operation(op)
        print("Applied {} on qubit(s) {}".format(
            gate_type, ",".join(map(str, qubit_ids))))
    elif intent == INTENTS.CREATE_CIRCUIT:
        # Create new circuit
        print("Creating new circuit...")
        circuit = Circuit()
        num_qubits = get_num_qubits(entities)
        circuit.add_qubits(num_qubits)
    elif intent == INTENTS.DELETE_QUBITS:
        # Remove qubits from circuit
        pass
    else:
        print("Invalid intent: {}".format(intent))

    return circuit


def handle_message(message: str, circuit: Circuit = None) -> Union[Circuit, None]:
    resp = client.message(message)
    if len(resp['intents']) == 0:
        print("Invalid message.")
        return circuit
    intent = resp['intents'][0]['name']
    entities = resp['entities']
    return handle_intent(intent, entities, circuit)
