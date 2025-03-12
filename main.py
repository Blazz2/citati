from flask import Flask, render_template
import random
import json

aplikacija = Flask(__name__)

with open('citati.json', 'r', encoding='utf-8') as file:
    CITATI = json.load(file)

def pridobi_prikazane_citate():
    if not hasattr(aplikacija, 'prikazani_citati'):
        aplikacija.prikazani_citati = []
    return aplikacija.prikazani_citati

@aplikacija.route("/")
def domov():
    prikazani_citati = pridobi_prikazane_citate()
    
    if len(prikazani_citati) >= len(CITATI):
        prikazani_citati.clear()
    
    razpolozljivi_citati = [c for c in CITATI if c["citat"] not in prikazani_citati]
    izbran_citat = random.choice(razpolozljivi_citati)
    prikazani_citati.append(izbran_citat["citat"])
    
    return render_template("quote.html", 
                         citat=izbran_citat["citat"], 
                         avtor=izbran_citat["avtor"])

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    aplikacija.run(debug=False, host='0.0.0.0', port=port)