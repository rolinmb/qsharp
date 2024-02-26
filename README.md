host.py -> driver program to simulate and compare coinflips and other 2-outcome/probability events (with probabilities that sum to 100%).

qubit.py & qregister.py -> Contain custom qubit and qRegister classes respectively (not by Microsoft, purely inspired
by the wikipedia pages [here (qubits)](https://en.wikipedia.org/wiki/Qubit) and [here (registers)](https://en.wikipedia.org/wiki/Quantum_register))
NOTE: qregister.py is not a valid implementation in any sense and was attempted further in my rolinmb/qubits repo if you are curious

observeregister.py -> intended to call ObserveRegister from HostPython.qs

!! THIS REPO IS DEPRECATED AS OF 2/26/2024 SINCE ObserveRegister DOES NOT WORK; WORKING IN NEW REPO rolinmb/qnn !!

Qubits can essentially represent a state that hasn't yet been observed; but you know what the outcomes are in nature. For example; say you know
a person shows up to work 80% of the time; you could create a qubit that collapses to 1 80% of all observations; and that could help simulate
2-outcome/probabilistic events more accurately.

You could theoretically generate larger random numbers rather than just a single random bit like in these programs; you would just have to concatenate a string of random bits then calculate what that binary number evaluates to in decimal.

HostPython.qs -> function to simulate coinflip/true-false event using Q# SDK

Program.qs -> functions learned from following other tutorials by Microsoft Research on Q# and how qubits work

You need to be able to point to dotnet.exe in order to run

Made after following the video by Microsoft Research on YouTube [here.](https://www.youtube.com/watch?v=c9Df90CVHkc)
