const BASE_URL = 'https://artiqlate.herokuapp.com';

let circuit = null;

const container = document.querySelector('#circuit-container');
const imgContainer = document.querySelector('#circuit-image');
const speechOutput = document.querySelector('#output');

function drawCircuit(message) {
  const data = { message };
  if (circuit != null) data['circuit'] = circuit;

  fetch(`${BASE_URL}/message`, {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: Object.entries(data)
      .map(([key, val]) => `${encodeURIComponent(key)}=${encodeURIComponent(val)}`)
      .join('&'),
    method: 'POST'
  })
  .then(data => data.json())
  .then(res => {
    circuit = res.circuit;
    imgContainer.src = `data:image/jpg;base64, ${res.img}`;
  })
  .catch(err => console.log(err));
}

// getCircuit('create new circuit with 5 qubits')

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const SpeechGrammarList = window.SpeechGrammarList || window.webkitSpeechGrammarList;
const SpeechRecognitionEvent = window.SpeechRecognitionEvent || window.webkitSpeechRecognitionEvent;

const recognition = new SpeechRecognition();
const speechRecognitionList = new SpeechGrammarList();

const commands = ['add', 'create'];
const keywords = ['qubit', 'qubits', 'cubit', 'cubits', 'circuit', 'gate'];
const gates = ['hadarmard', 'cnot', 'ccnot', 'X', 'Y', 'Z', 'H'];
const grammar = `#JSGF V1.0;
grammar artiqlate;
public <number> = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 ;
public <command> = ${commands.join(' | ')} ;
public <keyword> = ${keywords.join(' | ')} ;
public <gate> = ${gates.join(' | ')} ;
public <gatestatement> = (<gate> gate | <gate>) ;
public <qubit> = qubit | qubits | cubit | cubits | cubed | cubeds ;
public <qubitid> = <qubit> <number> ;
public <qubitcount> = <number> <qubit> ;
public <statement> = create a circuit | create a circuit with <qubitcount> | add <number> <keyword> | apply <gate statement> to <qubitid> ;
`;
console.log(grammar)
speechRecognitionList.addFromString(grammar, 1);

recognition.grammars = speechRecognitionList;
recognition.continuous = false;
recognition.lang = 'en-CA';
recognition.interimResults = false;
recognition.onstart = () => console.log('started');
recognition.onresult = function(event) {
  const transcript = event.results[0][0].transcript;
  speechOutput.textContent = 'Result received: ' + transcript + '.';
  drawCircuit(transcript);
  console.log('Confidence: ' + event.results[0][0].confidence);
};
recognition.onspeechend = function() {
  recognition.stop();
};
recognition.onnomatch = function(event) {
  console.log('Failed to recognize command.');
};
recognition.onerror = function(event) {
  console.log('Error occurred in recognition: ' + event.error);
};

document.body.onclick = function() {
  recognition.start();
  console.log('Ready to receive a command.');
};


