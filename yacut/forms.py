from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

from settings import MIN_LENGTH, ORIGINAL_LINK_LENGTH, CUSTOM_ID_LENGTH


class URLMapForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(MIN_LENGTH, ORIGINAL_LINK_LENGTH)]

    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(MIN_LENGTH, CUSTOM_ID_LENGTH), Optional()]
    )
    submit = SubmitField('Создать')
