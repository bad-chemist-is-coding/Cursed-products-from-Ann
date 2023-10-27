class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Câu hỏi {self.question_number}: {current_question.text} \n(Gõ 'Đúng' hoặc 'Sai'): ")
        self.check_question(user_answer, current_question.answer, current_question.explain)

    def check_question(self, user_answer, correct_answer, explaination):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Bạn có tố chất làm luật sư đấy!")
        else:
            print('Sai mất tiêu rồi...')
        print(f"Đáp án là {correct_answer}.\n{explaination}")
        print(f"Điểm của bạn là {self.score}/{self.question_number}")
        print("\n")