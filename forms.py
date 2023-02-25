from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm): 
    """Form for adding pets"""

    name = StringField(
        "Pet Name", 
        validators=[InputRequired()]
        )
    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("bunny","Bunny")]
        )
    photo_url = StringField (
        "Photo URL",
        validators=[Optional(), URL()]
        )
    age = IntegerField(
        "Age", 
        validators=[Optional(), NumberRange(min=0, max=30)]
        )
    notes = TextAreaField (
        "Additional Notes",
        validators=[Optional(), Length(min=10)]
        )
    
class EditPetForm(FlaskForm): 
    """Form for editing pet information"""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()]
    )

    notes = TextAreaField (
        "Additional Notes",
        validators=[Optional(), Length(min=10)]
        )
    
    available = BooleanField("Available?")
    
