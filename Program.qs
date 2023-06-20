namespace qsharp {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Diagnostics;
    
    @EntryPoint()
    operation Main() : Unit {
        //Message("Hello quantum world!");
        //MeasurementDemo();
        //RandomBitDemo();
        //RandomBit();
        //RandomTwoBits();
        //DeutschAlgorithm();

    }

    operation MeasurementDemo() : Unit {
        use q = Qubit();
        H(q); // Superimpose with Hadamard gate
        Message($"{M(q)}"); // Print the measurement/observation of q
        DumpMachine();
    }

    operation RandomBitDemo() : Unit {
        let nBits = 100;
        mutable countOnes = 0;
        use q = Qubit();
        for _ in 1..nBits {
            H(q); // Re-Superimpose each time after collapsing to measure
            if M(q) == One { // Check if measurment is equal to |1> (coillapses superposition from H(q))
                set countOnes += 1;
            }
        }
        Message($"{countOnes} 1s out of {nBits} bits");
    }

    operation RandomBit() : Int {
        use q = Qubit();
        H(q);
        return M(q) == Zero ? 0 | 1;
    }

    operation RandomTwoBits() : Int {
        return RandomBit()*2 + RandomBit();
    }
    // oracle example below (essentially are functions)
    operation ApplyOracleConstzero(x : Qubit) : Unit {}

    operation ApplyOracleIdentity(x : Qubit) : Unit {
        Z(x);
    }

    operation IsFunctionBalanced(oracle : (Qubit => Unit)) : Bool {
        use q = Qubit();
        H(q);
        oracle(q);
        H(q);
        return M(q) == Zero ? false | true;
    }
    // One-Qubit Deutsch Algorithm
    operation DeutschAlgorithm() : Unit {
        Message($"{IsFunctionBalanced(ApplyOracleConstzero)}");
        Message($"{IsFunctionBalanced(ApplyOracleIdentity)}");
    }
    // Helper function for below function
    operation Teleport(msg : Qubit, there : Qubit) : () {
        body {
            using(register = Qubit[1]) {
                let here = register[0];
                // Creating entaglement we can use to send msg
                H(here);
                CNOT(here, there);
                // Move msg into entagled pair
                CNOT(msg, here);
                H(msg);
                // Measure out the entanglement
                if(M(msg) == One) { Z(there);}
                if(M(here) == One) { X(there);}
                // Reset or "here" Qubt before releasing it
                Reset(here);
            }
        }
    }

    // Teleport example
    operation TeleportClassicalMessage(message : Bool) : Bool {
        body {
            mutable measurement = false;

            using(register = Qubit[2]){
                let msg = register[0];
                let there = register[1];
                // Encode msg
                if(message){ X(msg);}
                // Use helper function defined above
                Teleport(msg, there);
                // Collapse by measurement
                if(M(there) == One){ 
                    set measurement = true;
                    ResetAll(register);
                }
            }
            return measurement;
        }
    }

} // namespace qsharp