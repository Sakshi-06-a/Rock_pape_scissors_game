# Rock_pape_scissors_game
Rock-Paper-Scissors CLI Game built in Python. User plays against computer with random choice generation. Includes game logic, score tracking, and multiple rounds. Handles invalid input and provides clear user feedback. Simple command-line interface to demonstrate Python basics.

# 🎮 Rock Paper Scissors Game

A simple **Rock-Paper-Scissors game built using Python**.
The player competes against the computer, which randomly selects rock, paper, or scissors.

## 📌 Features

* 🎯 Player vs Computer gameplay
* 🎲 Random computer choices using Python's `random` module
* 🏆 Automatic winner determination
* 📊 Score tracking for both player and computer
* 🔄 Option to play multiple rounds
* ❌ Input validation for invalid choices
* 👋 Displays the final score when the game ends

## 🛠️ Technologies Used

* **Python**
* `random` module
* Functions
* Conditional statements
* While loop
* User input
* String methods
* f-strings

## 📂 Project Structure

```text
Rock-Paper-Scissors/
│
├── rock_paper_scissors.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository
   git clone https://github.com/Sakshi-06-a/Rock_paper_scissors_game.git

### 2. Open the project folder

```bash
   cd Rock_paper_scissors_game
```

### 3. Run the Python program

```bash
python rock_paper_scissors.py
```

## 🎮 How to Play

1. Run the program.
2. Enter one of the following choices:

   * `rock`
   * `paper`
   * `scissors`
3. The computer randomly selects its choice.
4. The game determines the winner.
5. Your score and the computer's score are displayed.
6. Choose whether you want to play another round.

## 🧠 Game Rules

| Player             | Computer    | Result           |
| ------------------ | ----------- | ---------------- |
| Rock               | Scissors    | 🏆 Player Wins   |
| Scissors           | Paper       | 🏆 Player Wins   |
| Paper              | Rock        | 🏆 Player Wins   |
| Same choice        | Same choice | 🤝 Tie           |
| Other combinations | —           | 😢 Computer Wins |

## 💡 Concepts Practiced

This project helped practice important Python concepts such as:

* Defining and calling functions
* `if`, `elif`, and `else`
* `while` loops
* `break` and `continue`
* Lists
* `random.choice()`
* User input using `input()`
* String methods such as `.lower()`
* Variables and score tracking
* f-strings

## 🚀 Future Improvements

Some possible improvements for this project:

* Add a **Best of 3 / Best of 5** mode
* Add difficulty levels
* Add player names
* Store game history
* Create a graphical user interface (GUI)
* Add more detailed statistics

## 👩‍💻 Author

**Sakshi**

This project was created as a beginner Python project to practice programming fundamentals and logical problem-solving.

