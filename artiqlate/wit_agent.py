from wit import Wit
from dotenv import load_dotenv
from pathlib import Path
from circuit import Circuit
import os
import entities as ENTITIES
import intents as INTENTS

env_path = Path('.') / '.env'
load_dotenv(env_path)
WIT_API_KEY = os.getenv("WIT_API_KEY")

client = Wit(WIT_API_KEY)
circuit = Circuit()


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
    return int(num_qubits)


def handle_intent(intent: str, entities: dict):
    if intent == INTENTS.ADD_QUBITS:
        pass
    elif intent == INTENTS.APPLY_GATE:
        pass
    elif intent == INTENTS.CREATE_CIRCUIT:
        print("Creating new circuit...")
        circuit = Circuit()
        num_qubits = get_num_qubits(entities)
        circuit.add_qubits(num_qubits)
        print(num_qubits)
    elif intent == INTENTS.DELETE_QUBITS:
        pass
    else:
        print("Invalid intent: {}".format(intent))


def handle_message(message: str) -> str:
    resp = client.message(message)
    print(resp)
    if len(resp['intents']) == 0:
        return "Invalid message."
    intent = resp['intents'][0]['name']
    entities = resp['entities']
    handle_intent(intent, entities)
    return str(circuit)


handle_message('create new circuit with 3 qubits')
print(str(circuit))
