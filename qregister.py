from qubit import *

def validateRegister(qbits):
    sum = 0;
    for q in qbits:
        sum += (abs(q.c0)**2 + abs(q.c1)**2)
    return True if int(round(sum, 0)) == 1 else False

class qRegister:
    def __init__(self, qbits):
        if validateRegister(qbits):
            raise Exception(f"-> Qubits not valid to form a Quantum Register.")
        self.qubits = qbits
        self.probs = []
        # Find probability amplitudes of each qubit using tensor product
        for q in self.qubits:
            factors = []
            for p in self.qubits:
                if q is p:
                    continue
                else:
                    factors.append(np.array(p.c0, p.c1))
            self.probs.append(np.tensordot(np.array(q.c0, q.c1), np.array(factors)))
        self.n_qubits = len(qbits)

if __name__ == "__main__":
    register = qRegister([qubit(1/np.sqrt(2), -1/np.sqrt(2)), qubit(-1/np.sqrt(2), 1/np.sqrt(2))])
    for i in range(0, len(register.qubits)):
        print(f"Qubit: {register.qubits[i]} Amplitude: {register.probs[i]}")