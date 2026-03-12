from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a 2-qubit circuit
qc = QuantumCircuit(2, 2)

# Step 1: Put qubit 0 into superposition
qc.h(0)

# Step 2: Entangle qubit 0 and qubit 1
qc.cx(0, 1)

# Step 3: Measure both qubits
qc.measure(0, 0)
qc.measure(1, 1)

# Draw the circuit
print("Bell State Circuit:")
print(qc.draw())

# Simulate
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

print("\nSimulation Results (1000 shots):")
print(counts)
print("\nInterpretation:")
print(f"|00> probability: {counts.get('00', 0) / 1000 * 100:.1f}%")
print(f"|11> probability: {counts.get('11', 0) / 1000 * 100:.1f}%")
