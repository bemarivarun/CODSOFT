import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiple Choice Quiz")
        
        self.question_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)
        
        self.radio_var = tk.IntVar()
        self.radio_buttons = []
        
        for i in range(4):
            radio_button = tk.Radiobutton(root, text="", variable=self.radio_var, value=i)
            self.radio_buttons.append(radio_button)
            radio_button.pack(anchor=tk.W)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)
        
        self.score = 0
        self.question_number = 0
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "Berlin", "London", "Rome"],
                "answer": 0
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Jupiter", "Venus"],
                "answer": 1
            },
            {
                "question": "What is 2 + 2?",
                "options": ["3", "4", "5", "6"],
                "answer": 1
            }
        ]
        
        self.display_question()
    
    def display_question(self):
        if self.question_number < len(self.questions):
            question_data = self.questions[self.question_number]
            question = question_data["question"]
            options = question_data["options"]
            
            self.question_label.config(text=question)
            
            for i, option_text in enumerate(options):
                self.radio_buttons[i].config(text=option_text)
            
            self.radio_var.set(-1)
        else:
            messagebox.showinfo("Quiz Finished", f"Quiz finished! Your score: {self.score}")
    
    def check_answer(self):
        user_answer = self.radio_var.get()
        correct_answer = self.questions[self.question_number]["answer"]
        
        if user_answer == correct_answer:
            self.score += 1
        
        self.question_number += 1
        self.display_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
