from flask import Flask, render_template, request, jsonify
from spellchecker import SpellChecker
import re

app = Flask(__name__)

spell_checker = SpellChecker(language='pt')

def correct_sentence(frase):
    tokens = re.findall(r'\w+|[^\w\s]', frase, re.UNICODE)
    corrected_tokens = []
    errors_found = False

    for token in tokens:
        if not re.match(r'\w+', token):
            corrected_tokens.append(token)
            continue

        if not spell_checker.known([token.lower()]):
            correction = spell_checker.correction(token.lower())
            corrected_tokens.append(correction if correction else token)
            errors_found = True
        else:
            corrected_tokens.append(token)

    final_sentence = "".join([" " + token if not re.match(r'[^\w\s]', token) and index > 0 else token 
                           for index, token in enumerate(corrected_tokens)]).strip()

    if not errors_found:
        return "Parabéns, sua frase está gramaticalmente correta"
    else:
        return f"Será que você não quis dizer: {final_sentence}"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/correct', methods=['POST'])
def correct():
    data = request.get_json()
    frase = data.get('frase', '')
    resposta = correct_sentence(frase)
    return jsonify({'response': resposta})

if __name__ == '__main__':
    app.run(debug=True)