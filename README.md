# ArtiQlate - Design quantum algorithms with your voice!

<div style="text-align:center">
    <img src="https://github.com/theRoughCode/artiQlate/blob/master/assets/circuit.png?raw=true" />
</div>

## Table of contents
* [Motivation](#motivation)
* [How to use](#how-to-use)
* [Technologies](#technologies)

## Motivation
Quantum computers have the ability to revolutionize our future by providing exponential speed-up on current algorithms. One such example is [Shor's algorithm](https://youtu.be/lvTqbM5Dq4Q) which can perform integer factorization in polynomial-time by utilizing the properties of quantum effects, such as superposition and interference. On the other hand, the fastest known classical algorithms take exponential time and is what current encryption schemes depend on for security. 

In the past decade, interest in quantum computing from both public and private sectors have grown exponentially. There is a growing need to educate the public on quantum computing concepts to prepare for this "quantum revolution".

When learning about quantum computing, quantum algorithms are generally visualized as quantum circuits. For example, the image above is the quantum circuit representing the [quantum teleportation](https://www.amarchenkova.com/2019/12/25/quantum-teleportation-q-microsoft/) algorithm.

Currently, to be able to write quantum algorithms, you would have to pick up one of the quantum programming languages like [Q\#](https://docs.microsoft.com/en-us/quantum/user-guide/), [Qiskit](https://qiskit.org/), or [Cirq](https://cirq.readthedocs.io/en/stable/). This web app makes it easy for anyone to pick up and learn about quantum algorithms without writing code! All you need is your voice to design your quantum algorithm within the browser.

## How to use
1. Open the app at https://www.raphaelkoh.me/artiQlate.
2. Click on "Start Command".
3. To create a new circuit, say "create a new circuit".
4. To add qubits to your circuit, say "add {n} qubits" where `n` is the number of qubits you want to add. Alternatively, you can perform steps 3 and 4 simultaneously by saying "create a new circuit with 3 qubits".
5. To add gates to your circuit, say "apply {gate} to {qubits}". For example, "apply X gate to qubit 1" or "apply CNOT gate to qubits 0 and 2" (note: the order matters for `CNOT` to determine the control and target qubits).
6. To measure the qubits, say "measure {qubit}" (e.g. "measure qubit 2") or "measure all qubits".
	
## Technologies
This project is created with:
* Python (backend)
* Flask (server)
* Qiskit (visualization)
* JavaScript (frontend)
* Wit.ai (NLP)
