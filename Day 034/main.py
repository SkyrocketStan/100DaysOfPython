import data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizUI

question_data = data.get_data()


def get_question_bank():
    q_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        q_bank.append(new_question)
    return q_bank


question_bank = get_question_bank()
quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
