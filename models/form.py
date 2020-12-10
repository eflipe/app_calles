from wtforms import Form
from wtforms import StringField
from wtforms import validators


def numeric_validator(form, field):
    field = field.data

    if field.isnumeric():
        raise validators.ValidationError('Ingrese un valor no númerico.')


class SearchForm(Form):
    search_item = StringField('calle',
                              [validators.length(min=3, max=30,
                               message='Ingrese un nombre válido.'),
                               numeric_validator
                               ])
