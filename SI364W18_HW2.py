## SI 364
## Winter 2018
## HW 2 - Part 1

## This homework has 3 parts, all of which should be completed inside this file.

## Add view functions and any other necessary code to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided are inside the templates/ directory, where they should stay).

## As part of the homework, you may also need to add templates (new .html files) to the templates directory.

#############################
##### IMPORT STATEMENTS #####
#############################

from flask import Flask, request, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, ValidationError
from wtforms.validators import Required

#####################
##### APP SETUP #####
#####################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstring'

####################
###### FORMS #######
####################

class AlbumEntryForm(FlaskForm):
    album_name = StringField('Enter the name of an album', validators=[ Required() ])
    rating = RadioField('How much do you like this item? (1 low, 3 high)', choices=[(1, '1'), (2, '2'), (3, '3')], validators=[ Required() ])
    submit = SubmitField('Submit')

####################
###### ROUTES ######
####################

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}</h1>'.format(name)

@app.route('/album_entry')
def view_album_entry():
    form_var = AlbumEntryForm()
    return render_template('album_entry.html', form=form_var)

@app.route('/album_result', methods=['GET','POST'])
def view_results():
    form_var = AlbumEntryForm(request.form)
    if request.method == 'GET' and form_var.validate_on_submit():
        album_name = form_var.album_name.data
        rating = form_var.rating.data
        return render_template('album_data.html', album_name=album_name, rating=rating)
    flash('All fields are required!')
    return redirect(url_for('view_album_entry'))

if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)
