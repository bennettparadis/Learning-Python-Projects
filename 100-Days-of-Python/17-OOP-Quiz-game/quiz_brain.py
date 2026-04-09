class QuizBrain:

    def __init__(self, question_list):
        #list starts off with index 0, so we start at question 0 --> default attributes
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    

    def still_has_questions(self):
        #can skip the if/else statement -- returns Boolean of the expression below, whether or not the question number is greater than the length of the list
        return self.question_number < len(self.question_list)
    

    def next_question(self):
        #looks up the current question object based on the index number within the question list
        #this is a question object, so it has text and answer attributes
        current_question = self.question_list[self.question_number]
        
        #adds 1 to the question number --> accomplishes two things: 1) gives correct number in display, instead of index value; 2) updates the question number to look up for the next question
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False): ").lower() 

        #call check answer method, pass over user answer and correct answer to question; interacting methods
        self.check_answer(user_answer, current_question.answer)
    

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You are correct!")
            self.score += 1
        else:
            print("Whoops that's wrong.")
        #print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
