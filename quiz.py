from question_model import QuestionBank
import random

class QuizModel:
    """A Quiz Object to provide a structure to contruct a quiz."""
    def __init__(self, data):
        self.question_number = 0
        self.score = 0
        self.question_list = QuestionBank(data=data)
        self.current_question = ''

    def next_question(self):
        """Retrieves the next question to continue the qwuiz."""
        self.current_question = self.get_question()
        self.question_number+=1
        question = [self.format_question(), self.get_choices()]
        return question
    
    def check_answer(self, response):
        """Checks the answer of the question to see if it is correct"""
        is_correct = response == self.current_question.correct
        self.increase_score(is_correct)
    
    def increase_score(self, answer:bool):
        """A method for increasing the score for every correct answer"""
        if answer:
            self.score+=1
    
    def get_final_score(self):
        """Calculates the final score of the quiz

        :returns score: the ammount correct and the percentage
        """
        return f"{self.score}/{self.question_number} = {int((self.score / self.question_number) * 100)}%"
    
    def get_question(self):
        """Retrieves the question from the data passed to the quiz.
        
        :returns question: the current question from the quiz data.
        """
        question = self.question_list.data[self.question_number]
        return question
    
    def format_question(self):
        "Formats the question for visibility on the page"
        return f"{self.question_number}# {self.current_question.text}"

    def get_choices(self):
        """Retrieves the current question's [choices | answers].

        :return choices: both right and wrong answers 
        """
        choices = self.current_question.answers
        random.shuffle(choices)
        return choices
    
    def is_complete(self):
        """Checks the quiz to see if it has been completed."""
        return self.question_number >= len(self.question_list.data)
    
    def reset(self):
        """Resets the quiz to start from the beginning"""
        self.question_number = 0
        self.score = 0