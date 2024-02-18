import tkinter as tk
from quiz_brain import QuizBrain


#Colors used
THEME_COLOR = "#375362"
GREEN="#00FF00"
RED="#FF0000"
DEFAULT_CANVAS_COLOR="#FFFFFF"


class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain

        #Creating Tkinter Window
        self.window=tk.Tk()
        self.window.title("QUIZ APPLICATION")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        #Images
        self.true_image=tk.PhotoImage(file="./images/true.png")
        self.false_image=tk.PhotoImage(file="./images/false.png")

        #Score Label
        self.sc_label=tk.Label(text="Score: 0",bg=THEME_COLOR,fg="#FFFFFF")
        self.sc_label.grid(column=1,row=0)

        #Canvas
        self.qu_canvas=tk.Canvas(width=300,height=250,highlightthickness=0)
        self.question_text=self.qu_canvas.create_text(150,125,text="Question",font=("Arial",20,"italic"),fill=THEME_COLOR,width=275)
        self.qu_canvas.grid(pady=30,column=0,row=1,columnspan=2)

        #True Button
        self.true_button=tk.Button(image=self.true_image,highlightthickness=0,borderwidth=0,command=self.true_pressed)
        self.true_button.grid(column=0,row=2)

        #False Button
        self.false_button=tk.Button(image=self.false_image,highlightthickness=0,borderwidth=0,command=self.false_pressed)
        self.false_button.grid(column=1,row=2)

    
        self.get_next_question()

        self.window.mainloop()

    #Displays next question on canvas
    def get_next_question(self):
        self.qu_canvas.config(bg=DEFAULT_CANVAS_COLOR)
        self.sc_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.qu_canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.qu_canvas.itemconfig(self.question_text,text=f"FINAL SCORE\n        {self.quiz.score}/10")

    #Command for True Button
    def true_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)

    #Command for False Button 
    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    #Feedback
    def give_feedback(self, is_right):
        if is_right:
            self.qu_canvas.config(bg=GREEN)
            self.window.after(500,self.get_next_question)
            
        else:
            self.qu_canvas.config(bg=RED)
            self.window.after(500,self.get_next_question)
    

        