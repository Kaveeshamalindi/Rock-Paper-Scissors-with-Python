
import tkinter as tk
import random

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)

    if user_choice == computer:
        result = "It's a Draw! 🤝"

    elif (user_choice == "Rock" and computer == "Scissors") or \
         (user_choice == "Paper" and computer == "Rock") or \
         (user_choice == "Scissors" and computer == "Paper"):

        result = "You Win! 🎉"
        user_score += 1

    else:
        result = "Computer Wins! 🤖"
        computer_score += 1

    result_label.config(
        text=f"You: {user_choice}\nComputer: {computer}\n\n{result}"
    )

    score_label.config(
        text=f"Your Score: {user_score}  |  Computer: {computer_score}"
    )

def reset():
    global user_score, computer_score
    user_score = 0
    computer_score = 0

    result_label.config(text="Choose Rock, Paper or Scissors!")
    score_label.config(text="Your Score: 0  |  Computer: 0")

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.config(bg="#EAF2F8")

# Heading
title = tk.Label(
    root,
    text="✊ Rock Paper Scissors ✌️",
    font=("Arial", 18, "bold"),
    bg="#EAF2F8"
)
title.pack(pady=20)

# Instructions
tk.Label(
    root,
    text="Choose your move!",
    font=("Arial", 12),
    bg="#EAF2F8"
).pack(pady=10)

# Buttons
for choice in ["Rock", "Paper", "Scissors"]:
    tk.Button(
        root,
        text=choice,
        font=("Arial", 12, "bold"),
        width=15,
        command=lambda c=choice: play(c)
    ).pack(pady=5)

# Result
result_label = tk.Label(
    root,
    text="Choose Rock, Paper or Scissors!",
    font=("Arial", 12),
    bg="#EAF2F8",
    justify="center"
)
result_label.pack(pady=15)

# Score
score_label = tk.Label(
    root,
    text="Your Score: 0  |  Computer: 0",
    font=("Arial", 11, "bold"),
    bg="#EAF2F8"
)
score_label.pack(pady=5)

# Reset
tk.Button(
    root,
    text="Restart Game",
    command=reset
).pack(pady=10)

root.mainloop()
