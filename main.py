from flask import Flask, render_template
import random

aplikacija = Flask(__name__)

CITATI = [
    {"citat": "Včasih zmagaš, včasih se učiš", "avtor": "John C. Maxwell"},
    {"citat": "Naredi ali ne naredi, poskusov ni.", "avtor": "Yoda"},
    {"citat": "Edini način za odlično delo je, da ljubiš, kar počneš.", "avtor": "Steve Jobs"},
    {"citat": "Uspeh ni končen, neuspeh ni usoden: pomembna je le pogumnost za nadaljevanje.", "avtor": "Winston Churchill"},
    {"citat": "Zgrešiš 100 % strelov, ki jih ne sprožiš.", "avtor": "Wayne Gretzky"},
    {"citat": "Verjemi, da zmoreš, in že si na pol poti.", "avtor": "Theodore Roosevelt"},
    {"citat": "Sreča je odvisna od nas samih.", "avtor": "Aristotel"},
    {"citat": "Ni pomembno, kako počasi greš, dokler se ne ustaviš.", "avtor": "Konfucij"},
    {"citat": "Težave v življenju so namenjene temu, da nas naredijo boljše, ne zagrenjene.", "avtor": "Dan Reeves"},
    {"citat": "Tisoč milj dolgo potovanje se začne s prvim korakom.", "avtor": "Lao Tzu"},
    {"citat": "Bodi sprememba, ki jo želiš videti v svetu.", "avtor": "Mahatma Gandhi"},
    {"citat": "Sreča je, ko to, kar misliš, govoriš in delaš, tvori harmonijo.", "avtor": "Mahatma Gandhi"},
    {"citat": "Nihče se ne more vrniti in začeti znova, vsak pa lahko začne danes in ustvari nov konec.", "avtor": "Maria Robinson"},
    {"citat": "Ne čakaj. Pravi čas nikoli ne bo pravi čas.", "avtor": "Napoleon Hill"},
    {"citat": "Tisto, kar nas ne ubije, nas okrepi.", "avtor": "Friedrich Nietzsche"},
    {"citat": "Življenje ni problem, ki ga je treba rešiti, ampak resničnost, ki jo je treba doživeti.", "avtor": "Søren Kierkegaard"},
    {"citat": "Največja slava ni v tem, da nikoli ne pademo, ampak da se vsakič poberemo.", "avtor": "Konfucij"},
    {"citat": "Ne boj se popolnosti, saj je nikoli ne boš dosegel.", "avtor": "Salvador Dalí"},
    {"citat": "Nič ni nemogoče, beseda sama pravi 'možno je'!", "avtor": "Audrey Hepburn"},
    {"citat": "Ne štejte dni, poskrbite, da bodo dnevi šteli.", "avtor": "Muhammad Ali"},
    {"citat": "Bolj ko treniraš, več sreče imaš.", "avtor": "Gary Player"},
    {"citat": "Znanje govori, modrost posluša.", "avtor": "Jimi Hendrix"},
    {"citat": "Nikoli ne dovoli, da majhen prepir uniči veliko prijateljstvo.", "avtor": "Dalajlama"},
    {"citat": "Če hočeš leteti, se moraš odreči vsemu, kar te vleče k tlom.", "avtor": "Toni Morrison"},
    {"citat": "Edina omejitev našega jutrišnjega uspeha so naši današnji dvomi.", "avtor": "Franklin D. Roosevelt"},
    {"citat": "Kdor hoče premikati svet, najprej premakne sebe.", "avtor": "Sokrat"},
    {"citat": "Življenje ni merjeno s številom vdihov, temveč s trenutki, ki nam vzamejo sapo.", "avtor": "Maya Angelou"},
    {"citat": "Moč ne prihaja iz fizične sposobnosti, temveč iz neomajne volje.", "avtor": "Mahatma Gandhi"},
    {"citat": "Priložnost zamujena ne pride več nazaj.", "avtor": "William Shakespeare"},
    {"citat": "Vedno se zdi nemogoče, dokler ni narejeno.", "avtor": "Nelson Mandela"},
    {"citat": "Če sanjaš sam, je to samo sanje. Če sanjamo skupaj, je to začetek nove resničnosti.", "avtor": "Japonski pregovor"},
    {"citat": "Neuspeh je začimba, ki da uspehu pravi okus.", "avtor": "Truman Capote"},
    {"citat": "Če ne znaš leteti, teci. Če ne znaš teči, hodi. Če ne znaš hoditi, se plazi. Ampak vedno se premikaj naprej.", "avtor": "Martin Luther King Jr."},
    {"citat": "Viharji naredijo drevesa močnejša.", "avtor": "Seneka"},
    {"citat": "Ne išči napak, išči rešitve.", "avtor": "Henry Ford"},
    {"citat": "Delo nas osvobaja, a le, če ga ljubimo.", "avtor": "Albert Camus"},
    {"citat": "Ne merite svojega bogastva s tistim, kar imate, ampak s tistim, kar dajete.", "avtor": "Neznan avtor"},
    {"citat": "Uspeh pomeni iti od neuspeha do neuspeha brez izgube navdušenja.", "avtor": "Winston Churchill"},
    {"citat": "Brez sanj ne moremo imeti prihodnosti.", "avtor": "Malala Yousafzai"},
    {"citat": "Ljubezen in prijaznost nikoli ne gresta v nič.", "avtor": "Helen Keller"},
    {"citat": "Pravi moški ni tisti, ki osvaja ženske, ampak tisti, ki zna ljubiti eno žensko celo življenje.", "avtor": "Neznan avtor"},
    {"citat": "Najboljša maščevanje je ogromen uspeh.", "avtor": "Frank Sinatra"},
    {"citat": "Sreča je, ko imaš nekoga, ki te ima rad, kljub tvojim pomanjkljivostim.", "avtor": "Neznan avtor"},
    {"citat": "Če hočeš uspeti, moraš najprej verjeti vase.", "avtor": "Neznan avtor"},
    {"citat": "Ne bojte se življenja. Verjemite, da je vredno živeti, in vaše prepričanje bo ustvarilo dejstvo.", "avtor": "William James"},
    {"citat": "Bodi potrpežljiv. Vse se zgodi ob svojem času.", "avtor": "Neznan avtor"},
    {"citat": "Nikoli ne dovoli, da te strah pred neuspehom ustavi pri poskusu.", "avtor": "Michael Jordan"},
    {"citat": "Le tisti, ki tvegajo iti predaleč, lahko ugotovijo, kako daleč lahko gredo.", "avtor": "T.S. Eliot"},
]

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
    aplikacija.run(debug=True, host='0.0.0.0', port=5000)