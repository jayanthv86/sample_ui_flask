from flask import render_template, flash, redirect, request, url_for
from app import app
from app.forms import RegistrationForm
from nfc_write import main, connect_reader
connected = False
clf = None

@app.route('/')
@app.route('/index')
def index():
    messages = request.args['messages']
    return "Thanks for registering " + messages
                           
@app.route('/register', methods=['GET', 'POST'])
def register():
    global connected
    global clf
    if not connected:
        clf = connect_reader('usb:072F:2200')
        connected = True
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        print('Thanks for registering' + form.firstname.data)
        json_str = repr({'First Name': form.firstname.data,
                    'Last Name': form.lastname.data,
                    'Tag ID': form.tag_id.data})
        main(json_str, clf)
        return redirect(url_for('index', messages=form.firstname.data))
    return render_template('register.html', form=form)
