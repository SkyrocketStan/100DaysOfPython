class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_q.text} ("
                       f"True/False)?: ")
        correct_answer = current_q.answer
        self.check_answer(answer, correct_answer)

    def still_have_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {c_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
