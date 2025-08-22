from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

class QuizForm(FlaskForm):
    answers = RadioField(choices=[], validators=[DataRequired()])
    submit = SubmitField('Next')