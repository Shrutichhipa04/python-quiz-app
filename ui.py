from tkinter import*
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300,height=250)
        self.question_text = self.canvas.create_text(150,125,width=280,text="some question",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        
        self.true_img = PhotoImage(file="C:/Users/shruti/python tutorial/new_folder/100days/day34/images/true.png")
        self.true_button = Button(image=self.true_img,highlightthickness=0,command=self.true_answer)
        self.true_button.grid(column=0,row=2)
        
        self.false_img = PhotoImage(file="C:/Users/shruti/python tutorial/new_folder/100days/day34/images/false.png")
        self.false_button = Button(image=self.false_img,highlightthickness=0,command=self.false_answer)
        self.false_button.grid(column=1,row=2)
        
        self.score = Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score.grid(column=1,row=0)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz ")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))
  

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else :
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
