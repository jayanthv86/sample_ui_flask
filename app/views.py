from flask import render_template, flash, redirect, request
from app import app
from app.forms import RegistrationForm
from nfc_write import main

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
                           
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        print('Thanks for registering' + form.firstname.data)
        json_str = repr({'First Name': form.firstname.data,
                    'Last Name': form.lastname.data,
                    'Tag ID': form.tag_id.data})
        main(json_str)
    return render_template('register.html', form=form)
