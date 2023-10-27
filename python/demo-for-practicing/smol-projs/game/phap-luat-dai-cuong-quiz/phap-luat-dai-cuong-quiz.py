from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

print("BÀI KIỂM TRA THỬ PHÁP LUẬT ĐẠI CƯƠNG\n")

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_explanation = question["explain"]
    new_question = Question(question_text, question_answer, question_explanation)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("Bạn đã hoàn thành bài ôn tập")
print(f"Nếu đây là bài thi thật thì bạn đạt được {quiz.score} điểm!")
