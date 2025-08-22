from flask import Flask, render_template, redirect, request, url_for
from data_handlers import get_json_data
from quiz import QuizModel
from quiz_form import QuizForm
from dotenv import load_dotenv
import os

load_dotenv()
f = "./static/json/infotech.json"
data = get_json_data(json_file=f)
SECRET = os.environ['SECRET_KEY']

# qb = QuestionBank(data)
quiz = QuizModel(data=data)

def create_app(s_key):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = s_key
    return app

app = create_app(s_key=SECRET)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/quiz", methods=["GET", "POST"])
def quiz_page():
    form = QuizForm()
    if request.method=="POST":
        quiz.check_answer(form.answers.data) # prints out the data from the submitted form
    
    if quiz.is_complete():
        score = quiz.get_final_score()
        return redirect(url_for("completed", score=score))

    question = quiz.next_question()
    form.answers.choices = [(a, a) for a in question[1]]
    form.answers.data = None # this needs to be applied, if not it will keep radio buttons selected by default
    return render_template("quiz.html", form=form, question=question[0])
   

@app.route("/completed")
def completed():
    score = request.args.get("score")
    return render_template("complete.html", score=score)

@app.route("/reset")
def reset_quiz():
    quiz.reset()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)