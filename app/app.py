from flask import Flask, render_template

app = Flask(__name__)

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
	
	
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)