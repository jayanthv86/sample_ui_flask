from wtforms import Form, BooleanField, StringField, PasswordField, validators, TextAreaField
import uuid

class RegistrationForm(Form):
    firstname = StringField('First Name', [validators.Length(min=4, max=25)])
    lastname = StringField('Last Name', [validators.Length(min=4, max=25)])
    company = StringField('Company', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    phone_num = StringField('Phone number', [validators.DataRequired()])
    tag_id = TextAreaField('Tag ID', default=uuid.uuid1())