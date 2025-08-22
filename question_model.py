
class Question:
    """Class creates question objects to format each question"""
    def __init__(self, text:str, correct_answer:str, answers:list[str]):
        self.text = text
        self.correct = correct_answer
        self.answers = answers


class QuestionBank:
    """Class that handles creating the Databank objects to hold all the question objects"""
    def __init__(self, data, question_key:str = 'question', correct_answer_key:str='correct_answer', choices_key='answers'):
        self.data = []
        for question in data:
            self.data.append(
                Question(
                    text=question[question_key], 
                    correct_answer=question[correct_answer_key], 
                    answers=question[choices_key]
                    ))

        