from flask import Flask, render_template
from flask_mail import Mail, Message

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import os


app = Flask(__name__)

#credential =  DefaultAzureCredential()
#keyVaultName = os.environ["KEY_VAULT_NAME"]
#client     =  SecretClient(vault_url=f"https://{keyVaultName}.vault.azure.net/", credential=credential)

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'transitionalimentairebe@gmail.com',
    MAIL_PASSWORD = 'helloworld'#client.get_secret("passwordmail"),
))


mail = Mail(app)

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/apropos')
def aProposPage():
    return render_template('apropos.html')

@app.route('/enquete')
def enquetePage():
	return render_template('enquete.html')

@app.route('/contact')
def contactPage():
	return render_template('contact.html')

@app.route("/testmail")
def testmailPage():
  msg = Message('AZURE - Hello from the other side!', sender =   'transitionalimentairebe@gmail.com', recipients = ['transitionalimentairebe@gmail.com'])
  msg.body = "This is a test that the mailing functions correctly"
  mail.send(msg)
  return "Message sent!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
