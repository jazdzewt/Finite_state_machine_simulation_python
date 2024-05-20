# Finite State Machine Simulator

## Project description

This project simulates a finite automaton M = (Q, Σ, δ, q_0, F). The simulator processes input strings consisting of input symbols, draws the transition diagram, and highlights the current state. After processing, it displays whether the input string is accepted.

Transitions: 

| Current State | Input Symbol | Next State |
|---------------|--------------|------------|
| q0            | 0            | q1         |
| q0            | 1            | q2         |
| q1            | 0            | q3         |
| q1            | 1            | q0         |
| q2            | 0            | q0         |
| q2            | 1            | q3         |
| q3            | 0            | q1         |
| q3            | 1            | q2         |

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.
