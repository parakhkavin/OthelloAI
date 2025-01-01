
# Othello AI Agents

This project involves the design and implementation of intelligent agents to play the strategy board game Othello. These agents employ various AI strategies, including Minimax, Alpha-Beta Pruning, and iterative deepening search under time constraints. The goal is to demonstrate the effectiveness of different algorithms in competitive and time-constrained gaming environments.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Algorithms](#algorithms)
   - [Minimax Agent](#minimax-agent)
   - [Alpha-Beta Pruning Agent](#alpha-beta-pruning-agent)
   - [Time-Constrained Search Agent (kkp56)](#time-constrained-search-agent-kkp56)
4. [Algorithm Complexity Analysis](#algorithm-complexity-analysis)
5. [Testing Results](#testing-results)
6. [Installation and Usage](#installation-and-usage)
7. [Extras and Limitations](#extras-and-limitations)
8. [License](#license)
9. [Author](#author)

---

## Introduction

The Othello AI project explores how various AI techniques can enhance decision-making in strategy games. By implementing and comparing multiple agents, we investigate trade-offs in computational efficiency, strategic depth, and adaptability under constraints.

---

## Features

- **AI Agents**: Three types of agents implemented—Minimax, Alpha-Beta Pruning, and kkp56 (time-constrained).
- **Strategic Play**: Evaluate moves using advanced search algorithms.
- **Adaptability**: Time-constrained agent adapts its depth dynamically.
- **Performance Insights**: Analyze and compare the efficiency and effectiveness of each agent.

---

## Algorithms

### Minimax Agent
- Uses a depth-first search approach to evaluate game states.
- Selects optimal moves based on a worst-case scenario.

### Alpha-Beta Pruning Agent
- Enhances Minimax efficiency by pruning irrelevant branches.
- Allows deeper exploration of the game tree within the same time.

### Time-Constrained Search Agent (kkp56)
- Employs iterative deepening search to optimize decision-making within a strict time limit.
- Dynamically adjusts depth based on available time.

---

## Algorithm Complexity Analysis

1. **Minimax and Alpha-Beta Pruning**:
   - Time complexity: \(O(b^d)\), where \(b\) is the branching factor and \(d\) is the depth.
   - Alpha-Beta Pruning reduces the effective branching factor.

2. **kkp56**:
   - Complexity adapts dynamically, balancing breadth and depth to optimize within the time constraint.

---

## Testing Results

- **Alpha-Beta Pruning**: Outperformed Minimax by reducing unnecessary searches and exploring deeper levels, resulting in more strategic moves.
- **kkp56**: Demonstrated exceptional performance in time-critical scenarios, making rapid yet strategic decisions.

---

## Installation and Usage

### Prerequisites
- **Python Version**: 3.6 or later.

### Steps to Run
1. Clone the repository and navigate to the `Othello_Code` directory.
2. Run the desired agent script. For example:
   ```bash
   python minimax_agent.py
   python alpha_beta_agent.py
   python kkp56_agent.py
   ```

---

## Extras and Limitations

### Extras
- Implemented a dynamic, time-constrained agent (`kkp56`) for extra credit.

### Limitations
- Performance of the time-constrained agent may vary under extreme time restrictions.

---

## Conclusion

This project highlights the capabilities of AI in strategy games:
- Minimax provides a baseline for decision-making.
- Alpha-Beta Pruning enhances depth and efficiency.
- The kkp56 agent excels in time-sensitive situations, showcasing adaptability and real-time decision-making.

---

## License
This project is licensed under the GNU 3.0 License. See the LICENSE file for details.

---

## Author
- Kavin Parakh
