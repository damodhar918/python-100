from data import question_data
from Question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
  
    
quiz = QuizBrain(question_bank)

while quiz.still_has_qustion():
    quiz.next_question()

print('You have completed the quiz')
print(f'you final score is: {quiz.score}/{quiz.question_number}\n')