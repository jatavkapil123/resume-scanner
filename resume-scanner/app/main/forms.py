from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired

class ResumeUploadForm(FlaskForm):
    resume = FileField('Upload Resume', validators=[DataRequired()])
    submit = SubmitField('Upload')

class JobDescriptionForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    description = TextAreaField('Job Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

