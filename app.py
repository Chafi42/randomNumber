from flask import Flask, request, jsonify, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre_cle_secrete'
csrf = CSRFProtect(app)

# Générer un nombre entier aléatoire entre 1 et 100
nombre_aleatoire = random.randint(1, 100)

class GuessForm(FlaskForm):
    guess = StringField('guess', validators=[DataRequired()])

@app.route('/')
def index():
    form = GuessForm()
    return render_template('index.html', form=form)

@app.route('/deviner', methods=['POST'])
def deviner():
    form = GuessForm()
    if form.validate_on_submit():
        supposition = int(form.guess.data)
        if supposition < nombre_aleatoire:
            message = "Trop bas!"
        elif supposition > nombre_aleatoire:
            message = "Trop haut!"
        else:
            message = "Félicitations! Vous avez deviné le nombre."
        return jsonify(message=message)
    return jsonify(message="Formulaire invalide"), 400

if __name__ == '__main__':
    app.run(debug=True)