from flask import Flask, request, make_response, redirect, render_template
import platform #system name across windows etc
#system
import os
#Template related
from flask_bootstrap import Bootstrap
#FORM RELATED IMPORTS
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
#MySQL IMPORTS
from flask_sqlalchemy import SQLAlchemy
#Module used to hide my passwords from github
import up_import as upi
uspa = upi.log_me_in_local(r'C:\UPTemphold\up.txt')
#Module  with local nmap cmds etc
import doscmds as dc

"""Initilization of the application"""
#App
app = Flask(__name__)
#Bootstrap
bootstrap = Bootstrap(app)
#MYSQL configuration and initilization
#SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
#.format to insert user and password mysql://user:password@ip:port/database
app.config['SQLALCHEMY_DATABASE_URI'] =\
'mysql://{}:{}@{}:{}/{}'.format(uspa[0],uspa[1],uspa[2],uspa[3],uspa[4])
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
"""
The db object corelated to the database and comes with flask_sqlalchemy
access and functionality of flask_sqlalchemy
"""

#route for the about device page
@app.route('/devicedata') #Decorator handlers event
def deviceinfo(things=''):
    #Get the network info , enumerate ('1',data,'2')
    arp = dc.getARP()
    netinfo = "Netinfo"
    #enumerate creates a iterated list.
    for idx, x in enumerate(arp):\
    netinfo += "<br /> {}: {} ".format(idx,str(x))
    #web browser information
    user_agent = request.headers.get('User-Agent')
    #get the operating system information
    user_os = platform.uname()
    Webstring = 'Computer Info! Your browser is %s \
    machine is  %s ' % (user_agent, user_os) #the response
    Compstring= "Arp table is: {}".format(arp)
    Netstring= "netinfo.split('b\'')"
    #this returns the extension of base html
    return render_template('extension_of-base.html',Webthings=Webstring\
    ,Compthings=arp, Netthings=Netstring)


#keep the redirec view
@app.route('/redirect')
def changeit():
    return redirect('http://google.com')

#keep the redirec view
@app.route('/8light')
def light():
    return redirect('http://8light.com')


"""
variable
"""

#the class of form define the forms them self.
class UserForm(Form):
    field1 = StringField('What is your name?', validators=[Required()])
    field2 = StringField('What is you user name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET','POST'])
def user_example(name='new', user=': please register'):
    form_name = name
    form_user = user
    user_form = UserForm()


    if user_form.validate_on_submit():
        #set the form data to variable
        form_name = user_form.field1.data
        form_user = user_form.field2.data
        #clear the form fields
        user_form.field1.data = ''
        user_form.field2.data = ''


    return render_template('boot_base.html', name=form_name, user=form_user, form=user_form)

"""CROSS SITE REQUEST FORGERY"""

#Flask-WTF protects against CSRF needs the app to configure an encription primary_key

app.config['SECRET_KEY'] = 'This string will be hard to guess!'

#the app.config dictionary is a general purpose place to store config Variables
#SECRET_KEY is general purpose and used by FLASK and several 3rd party applications
#added security key should be stored in a enviroment variable instead of stored
#in code


#Lauch the integrated Flask web develoment server

if __name__=='__main__':
    app.run(debug=True)
