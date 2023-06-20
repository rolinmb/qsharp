namespace HostPython {

    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Intrinsic;

    operation RandomBit() : Int {
        use q = Qubit();
        H(q);
        return MResetZ(q) == Zero ? 0 | 1;
    }
} // namespace HostPython