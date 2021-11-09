from flask import Flask, render_template, flash, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
#from wtforms.fields.html5 import EmailField
from flask_mail import Mail, Message
import os

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

credential =  DefaultAzureCredential()
keyVaultName = os.environ["KEY_VAULT_NAME"]
client     = SecretClient(vault_url=f"https://{keyVaultName}.vault.azure.net/", credential=credential)


app = Flask(__name__)
app.config['SECRET_KEY']= client.get_secret('passwordcfr').value


class contactForm(FlaskForm):
    name        = StringField("Nom Prénom")
    adresseMail = StringField("Adresse mail")
    codePost    = StringField("Code Postal")
    textMess    = TextAreaField("Ton Message")
    submit      = SubmitField("Envoi")

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'transitionalimentairebe@gmail.com',
    MAIL_PASSWORD =  client.get_secret('passwordmail').value,
))


mail = Mail(app)

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

        msg = Message(f"Vous avez reçu un nouveau message de {name.upper()}", sender =   'transitionalimentairebe@gmail.com', recipients = ['transitionalimentairebe@gmail.com'])
        msg.body = f"This is a message from {name}, code postal {codepost}, email {email} with message {newline}{newline} {messageM}"
        mail.send(msg)

        flash("ton message a bien été envoyé. Merci a toi.")

        form.name.data = ''
        form.name.data = ''
        form.adresseMail.data = ''
        form.codePost.data = ''
        form.textMess.data = ''

        submission_successful = True #or False. you can determine this.
        return redirect(url_for('indexPage', _anchor="contactFormFinal" ))


    return render_template('index.html', form=form, name=name)

@app.route('/questionnaire')
def questionnaire():
    return render_template('questionnaire.html')


@app.route('/old', methods=["GET","POST"])
def indexPage2():

    form = contactForm()
    name = False

    if form.validate_on_submit():
        name = form.name.data
        email= form.adresseMail.data
        codepost = form.codePost.data
        messageM = form.textMess.data


        newline= '\n'

        msg = Message(f"Vous avez reçu un nouveau message de {name.upper()}", sender =   'transitionalimentairebe@gmail.com', recipients = ['transitionalimentairebe@gmail.com'])
        msg.body = f"This is a message from {name}, code postal {codepost}, email {email} with message {newline}{newline} {messageM}"
        mail.send(msg)

        flash("ton message a bien été envoyé. Merci a toi.")

        form.name.data = ''
        form.name.data = ''
        form.adresseMail.data = ''
        form.codePost.data = ''
        form.textMess.data = ''

        submission_successful = True #or False. you can determine this.
        return redirect(url_for('indexPage2', _anchor="contactFormFinal" ))


    return render_template('index2.html', form=form, name=name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
