from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,TelField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class Contato(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    telefone = TelField('telefone', validators=[DataRequired()])
    conteudo = TextAreaField('conteudo') 
    enviar = SubmitField('enviar')

