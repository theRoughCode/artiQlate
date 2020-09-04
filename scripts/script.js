const BASE_URL = 'https://artiqlate.herokuapp.com';

let circuit = null;

const container = document.querySelector('#circuit-container');

function getCircuit(message) {
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
    container.innerHTML = res.img;
  })
  .catch(err => console.log(err));
}

getCircuit('create new circuit with 5 qubits')
