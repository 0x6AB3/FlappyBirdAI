# Flappy Bird AI

A classic Flappy Bird game implemented in Python using Pygame, featuring a simple rule-based AI agent that attempts to play the game.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [How to Run](#how-to-run)
- [AI Agent Explanation](#ai-agent-explanation)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Classic Flappy Bird Gameplay:** Experience the familiar mechanics of the popular game.
- **Rule-Based AI Agent:** An integrated AI that plays the game based on predefined rules.
- **AI Sensor Visualization:** Visual rays show what the AI "sees" (distance to bars and ground).

## Technologies Used
- Python 3.x
- Pygame library

## How to Run

### Prerequisites
- Python 3 installed on your system.
- `pygame` library installed. You can install it using pip:
  ```bash
  pip install pygame
  ```

### Installation and Execution
1. Clone this repository (or download the project files):
   ```bash
   git clone <repository_url> # Replace with actual repository URL if available
   cd FlappyBird
   ```
2. Run the main game file:
   ```bash
   python main.py
   ```
   Press the `SPACE` bar to start the game and control the bird manually, or observe the AI playing.

## AI Agent Explanation

The AI in this Flappy Bird project is a **rule-based agent**, not a machine learning model that learns through experience (e.g., reinforcement learning or neural networks). Its "intelligence" is derived from a set of hard-coded logical conditions that dictate its actions.

### How the AI "Plays"
The agent makes decisions based on its current state (bird's position, velocity) and the position of upcoming obstacles (bars). It uses the following primary rules:

1.  **Avoid Top Bar:** The AI attempts to maintain a position that allows it to pass through the gap without hitting the top bar.
2.  **Avoid Bottom Bar:** If the bird is falling (`velocity > 0`) and its bottom edge is within a certain buffer distance (e.g., 10 pixels) from the top of the bottom bar, the AI will trigger a jump. This rule aims to keep the bird from colliding with the bottom obstacle.
3.  **Avoid Ground:** If the bird is falling (`velocity > 0`) and is too close to the bottom of the screen (ground), it will also trigger a jump to prevent a collision.

These rules are designed to keep the bird within the playable area and guide it through the bar gaps. The AI's "learning" is not dynamic; it simply executes these predefined strategies.

### Sensor Visualization
The red and blue lines emanating from the bird are visual representations of the AI's "sensors."
- **Red Lines:** Indicate the bird's perception of the upcoming bar's corners.
- **Blue Lines:** Show the bird's distance to the top and bottom of the screen (ceiling and ground).

These visualizations help in understanding the information the rule-based agent uses to make its decisions.

## Project Structure
```
.
├── bars.py         # Defines the Bar class (pipes)
├── bird.py         # Defines the Bird class (player character)
├── birdjump.png    # Image for the bird when jumping
├── birdnormal.png  # Image for the bird in normal state
└── main.py         # Main game loop, initializes game objects, handles events, and contains AI logic
```

## Contributing
Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features (e.g., implementing a true learning AI), please feel free to open an issue or submit a pull request.

## License
This project is open-source and available under the GNU License.
