from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class MovieForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title.label = "title"
        self.title.validators = [InputRequired()]
        self.description.label = "description"
        self.description.validators = [InputRequired()]
        self.poster.label = "poster"
        self.poster.validators = [FileRequired(), FileAllowed(['jpg', 'png'])]

    title = StringField()
    description = TextAreaField()
    poster = FileField()
