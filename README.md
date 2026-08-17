# Rock_pape_scissors_game
Rock-Paper-Scissors CLI Game built in Python. User plays against computer with random choice generation. Includes game logic, score tracking, and multiple rounds. Handles invalid input and provides clear user feedback. Simple command-line interface to demonstrate Python basics.

# Rock Paper Scissors Game 🎮

A simple **Rock-Paper-Scissors command-line game built using Python**. The player competes against the computer, which randomly selects rock, paper, or scissors.

## Features

* 🎮 Player vs Computer gameplay
* 🎲 Random computer choice generation
* 🏆 Automatic winner determination
* 📊 Score tracking
* 🔄 Multiple rounds
* ❌ Invalid input handling
* 🖥️ Simple command-line interface

## Technologies Used

* **Python 3**
* `random` module

## 📂 Project Structure

```text
Rock_pape_scissors_game/
│
├── rock_paper_scissors.py
├── README.md
├── LICENSE
└── .gitignore
```

## Concepts Used

This project demonstrates the following Python concepts:

* Functions
* Lists
* Variables
* `if`, `elif`, and `else`
* `while` loop
* `break` and `continue`
* User input
* String methods
* `random.choice()`
* f-strings

## How the Game Works

The game follows the standard Rock-Paper-Scissors rules:

| Player                 | Computer    | Result      |
| ---------------------- | ----------- | ----------- |
| Rock                   | Scissors    | You Win 🏆  |
| Paper                  | Rock        | You Win 🏆  |
| Scissors               | Paper       | You Win 🏆  |
| Same Choice            | Same Choice | Tie 🤝      |
| All Other Combinations | —           | You Lose 😢 |

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Sakshi-06-a/Rock_pape_scissors_game.git
```

### 2. Open the project folder

```bash
cd Rock_pape_scissors_game
```

### 3. Run the program

```bash
python rock_paper_scissors.py
```

## How to Play

1. Run the program.
2. Enter `rock`, `paper`, or `scissors`.
3. The computer randomly selects its choice.
4. The winner is displayed.
5. The scores are updated.
6. Enter `y` to play another round or `n` to exit.

## Example

```text
========================================
Welcome to Rock-Paper-Scissors Game!
========================================

Choose: rock, paper, or scissors: rock

You chose: rock
Computer chose: scissors

You Win! 🎉

Score - You: 1 | Computer: 0
```

## Future Improvements

* Add Best of 3 or Best of 5 mode
* Add player names
* Add game statistics
* Add a graphical user interface (GUI)
* Store previous game results

## Author

**Sakshi**

This project was created to practice **Python programming fundamentals, functions, loops, conditional statements, and basic problem-solving**.


