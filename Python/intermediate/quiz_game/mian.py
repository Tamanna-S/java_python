from que_model import Quetion
from data import question_data
from quiz_brain import QuizBrain

quetion_bank = []

for que in question_data:
    que_text = que["question"]
    que_ans = que["correct_answer"]
    new_que = Quetion(que_text, que_ans)
    quetion_bank.append(new_que)

quiz = QuizBrain(quetion_bank)

while quiz.still_has_que():
    quiz.next_que()

print("you've completed the quiz..")
print(f"your final score is : {quiz.score}")