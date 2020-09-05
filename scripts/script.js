const BASE_URL = 'https://artiqlate.herokuapp.com';

let circuit = null;

const container = document.getElementById('circuit-container');
const imgContainer = document.getElementById('circuit-image');
const speechOutput = document.getElementById('output');
const startBtn = document.getElementById('start-btn');

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
    if (res.img == null) {
      imgContainer.removeAttribute('src');
      container.classList.remove('active');
      return;
    }
    container.classList.add('active');
    setTimeout(() => imgContainer.src = `data:image/jpg;base64, ${res.img}`, 100);
  })
  .catch(err => console.log(err));
}

function onStartSpeech() {
  startBtn.innerText = 'Listening...';
  startBtn.disabled = true;
}

function onStopSpeech() {
  startBtn.innerText = 'Start Command';
  startBtn.disabled = false;
}

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
speechRecognitionList.addFromString(grammar, 1);

recognition.grammars = speechRecognitionList;
recognition.continuous = false;
recognition.lang = 'en-CA';
recognition.interimResults = false;
recognition.onresult = function(event) {
  const transcript = event.results[0][0].transcript;
  speechOutput.textContent = `Command received: ${transcript}.`;
  drawCircuit(transcript);
  console.log('Confidence: ' + event.results[0][0].confidence);
};
recognition.onspeechend = function() {
  recognition.stop();
  onStopSpeech();
};
recognition.onnomatch = function(event) {
  console.log('Failed to recognize command.');
  onStopSpeech();
};
recognition.onerror = function(event) {
  console.log('Error occurred in recognition: ' + event.error);
  onStopSpeech();
};

startBtn.onclick = function() {
  onStartSpeech();
  recognition.start();
};


