namespace HostPython {

    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Intrinsic;

    operation RandomBit() : Int {
        use q = Qubit();
        H(q);
        return MResetZ(q) == Zero ? 0 | 1;
    }

    operation ObserveRegister(numQubits : Int) : Int {
        use register = Qubit[numQubits] {
            for qubit in register {
                H(qubit);
            }
            let sum = 0;
            for i in 0 .. numQubits - 1 {
                let result = MResetZ(register[i]) == Zero ? 0 | 1;
                sum += result*(1 <<< i);
            }
        
            return sum;
        }
    }
}