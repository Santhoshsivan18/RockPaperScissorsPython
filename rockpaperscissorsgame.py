import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Global variables for scores
player_score = 0
computer_score = 0


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")

        # Load images
        self.rock_image = ImageTk.PhotoImage(
            Image.open("RockPaperScissor/assets/rock.png").resize(
                (150, 150), Image.LANCZOS
            )
        )
        self.paper_image = ImageTk.PhotoImage(
            Image.open("RockPaperScissor/assets/paper.png").resize(
                (150, 150), Image.LANCZOS
            )
        )
        self.scissors_image = ImageTk.PhotoImage(
            Image.open("RockPaperScissor/assets/scissors.png").resize(
                (150, 150), Image.LANCZOS
            )
        )

        # Create buttons with images
        self.rock_button = tk.Button(
            root, image=self.rock_image, command=lambda: self.play_game("Rock")
        )
        self.rock_button.grid(row=0, column=0)

        self.paper_button = tk.Button(
            root, image=self.paper_image, command=lambda: self.play_game("Paper")
        )
        self.paper_button.grid(row=0, column=1)

        self.scissors_button = tk.Button(
            root, image=self.scissors_image, command=lambda: self.play_game("Scissors")
        )
        self.scissors_button.grid(row=0, column=2)

        # Label to display scores
        self.score_label = tk.Label(
            root,
            text=f"Player-score: {player_score} \t Computer-score: {computer_score}",
        )
        self.score_label.grid(row=1, column=1)

        # Initialize result label with empty text
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=2, column=0, columnspan=3)

    def play_game(self, player_choice):
        global player_score, computer_score
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            result = "Draw match"
        elif (
            (player_choice == "Rock" and computer_choice == "Scissors")
            or (player_choice == "Paper" and computer_choice == "Rock")
            or (player_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "Player wins!"
            player_score += 1
        else:
            result = "Computer wins!"
            computer_score += 1

        # Update result label with the game's outcome
        self.result_label.config(
            text=f"Player: {player_choice} \t Computer: {computer_choice}\n\nResult: {result}"
        )

        # Update score label
        self.score_label.config(
            text=f"Player-score: {player_score} \t Computer-score: {computer_score}"
        )


# Main function to run the application
def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
