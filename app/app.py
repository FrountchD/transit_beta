from flask import Flask, render_template, flash, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
#from wtforms.fields.html5 import EmailField
from flask_mail import Mail, Message
import os
from flask_pymongo import pymongo




from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

credential =  DefaultAzureCredential()
keyVaultName = os.environ["KEY_VAULT_NAME"]
client     = SecretClient(vault_url=f"https://{keyVaultName}.vault.azure.net/", credential=credential)


app = Flask(__name__)
app.config['SECRET_KEY']=client.get_secret('passwordcfr').value


class contactForm(FlaskForm):
    name        =  StringField("Nom Prénom", validators=[DataRequired()])
    adresseMail =  StringField("Adresse mail", validators=[DataRequired()])
    codePost    =  StringField("Code Postal", validators=[DataRequired()])
    textMess    =  TextAreaField("Ton Message", validators=[DataRequired()])
    submit      =  SubmitField("Envoi")

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'transitionalimentairebe@gmail.com',
    MAIL_PASSWORD = client.get_secret('passwordmail').value,
))


mail = Mail(app)

DB_USER = client.get_secret('dbuser')
DB_PWD = client.get_secret('dbpwd')

CONNECTION_STRING = "mongodb+srv://"+DB_USER+":"+DB_PWD+"@transitalim2022.nn8r0.mongodb.net/customerdb?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db=client.get_database('customerdb')
user_collection = pymongo.collection.Collection(db, 'user_collection')




@app.route('/', methods=["GET","POST"])
def indexPage():

    form = contactForm()
    name = False

    if form.validate_on_submit():
        name = form.name.data
        email= form.adresseMail.data
        codepost = form.codePost.data
        messageM = form.textMess.data


        newline= '\n'

        msg = Message(f"Initiative Reseau Social Transtion Alimentaire. Nouveau message de {name.upper()}", sender =   'transitionalimentairebe@gmail.com', recipients = ['transitionalimentairebe@gmail.com'])
        msg.body = f"This is a message from {name}, code postal {codepost}, email {email} with message {newline}{newline} {messageM}"
        mail.send(msg)

        flash("Un énorme merci à toi !")
        flash("T'oublies pas le questionnaire ? ")

        form.name.data = ''
        form.name.data = ''
        form.adresseMail.data = ''
        form.codePost.data = ''
        form.textMess.data = ''

        submission_successful = True #or False. you can determine this.
        return redirect(url_for('indexPage', _anchor="Contact" ))


    return render_template('index.html', form=form, name=name)

@app.route('/testdb')
def test():
    db.collection.insert_one({"name":"John5"})
    db.DataPro.insert_one({"name":"Hello World 3", "tvanum":"qqchose", "type":"autre" })
    return "connected to the data base"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
