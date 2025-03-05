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

    {"citat": "Največja slava življenja ni v tem, da nikoli ne pademo, ampak da se vsakič, ko pademo, dvignemo.", "avtor": "Nelson Mandela"},
    {"citat": "Začnite tako, da nehate govoriti in začnete delati.", "avtor": "Walt Disney"},
    {"citat": "Ne joči, ker je konec, ampak se nasmehni, ker se je to zgodilo.", "avtor": "Dr. Seuss"},
    {"citat": "Če želite živeti srečno življenje, ga povežite s ciljem, ne z ljudmi ali stvarmi.", "avtor": "Albert Einstein"},
    {"citat": "Uspeh ni ključ do sreče. Sreča je ključ do uspeha. Če imate radi to, kar počnete, boste uspešni.", "avtor": "Albert Schweitzer"},
    {"citat": "Vedno imej obraz obrnjen proti soncu - in sence bodo padale za teboj.", "avtor": "Walt Whitman"},
    {"citat": "Veliko bolj kot naše sposobnosti so naše odločitve tiste, ki kažejo, kaj v resnici smo.", "avtor": "J. K. Rowling"},
    {"citat": "Uspeh ni dokončen, neuspeh ni usoden: pomemben je pogum za nadaljevanje.", "avtor": "Winston S. Churchill"},
    {"citat": "Bolje je biti sovražen zaradi tega, kar si, kot biti ljubljen zaradi tega, kar nisi.", "avtor": "André Gide"},
    {"citat": "Če govoriš resnico, se ti ni treba ničesar spomniti.", "avtor": "Mark Twain"},
    {"citat": "Bodi sam, vsi drugi so že zasedeni.", "avtor": "Oscar Wilde"},
    {"citat": "Ne hodi tja, kamor vodi pot, ampak pojdi tja, kjer poti ni, in pusti sled.", "avtor": "Ralph Waldo Emerson"},
    {"citat": "Živiš samo enkrat, a če delaš prav, je enkrat dovolj.", "avtor": "Mae West"},
    {"citat": "Nikoli ni prepozno biti to, kar bi lahko bili.", "avtor": "George Eliot"},
    {"citat": "Najboljši način za napovedovanje prihodnosti je, da si jo izmisliš.", "avtor": "Alan Kay"},
    {"citat": "Edino nemogoče potovanje je tisto, ki ga nikoli ne začneš.", "avtor": "Tony Robbins"},
    {"citat": "Spremenite svoje misli in spremenite svoj svet.", "avtor": "Norman Vincent Peale"},
    {"citat": "Življenje je tisto, kar se zgodi, ko si zaposlen z drugimi načrti.", "avtor": "John Lennon"},
    {"citat": "Ne dovolite, da bi vam preživetje preprečilo ustvarjanje življenja.", "avtor": "John Wooden"},
    {"citat": "100 % strelov, ki jih ne izvedeš, zgrešiš.", "avtor": "Wayne Gretzky"},
    {"citat": "Pot tisoč milj se začne z enim samim korakom.", "avtor": "Lao Tzu"},
    {"citat": "Ne štejejo leta v življenju. Pomembno je življenje v letih.", "avtor": "Abraham Lincoln"},
    {"citat": "Kar mislimo, to postanemo.", "avtor": "Buda"},
    {"citat": "Namen našega življenja je biti srečen.", "avtor": "Dalajlama"},
    {"citat": "Vse, kar ste si kdaj želeli, je na drugi strani strahu.", "avtor": "George Addair"},
    {"citat": "Ti moraš biti sprememba, ki jo želiš videti v svetu.", "avtor": "Mahatma Gandhi"},
    {"citat": "Širi ljubezen, kamorkoli greš. Naj nihče ne pride k tebi, ne da bi ostal srečnejši.", "avtor": "Mati Terezija"},
    {"citat": "Kar je za nami in kar je pred nami, je malenkost v primerjavi s tem, kar je v nas.", "avtor": "Ralph Waldo Emerson"},
    {"citat": "Sreča ni nekaj gotovega. Prihaja iz vaših dejanj.", "avtor": "Dalajlama"},
    {"citat": "Življenje je kot vožnja s kolesom. Če želite ohraniti ravnotežje, se morate nenehno premikati.", "avtor": "Albert Einstein"},
    {"citat": "Glavna lekcija v življenju je, da se nikoli ne boj nikogar in ničesar.", "avtor": "Frank Sinatra"},
    {"citat": "Živeti je najredkejša stvar na svetu. Večina ljudi obstaja, to je vse.", "avtor": "Oscar Wilde"},
    {"citat": "Na koncu si ne bomo zapomnili besed naših sovražnikov, ampak molk naših prijateljev.", "avtor": "Martin Luther King Jr."},
    {"citat": "Življenje je dolga lekcija ponižnosti.", "avtor": "James M. Barrie"},
    {"citat": "Ne računajte dni, temveč jih naredite.", "avtor": "Muhammad Ali"},
    {"citat": "Ne gre za dolžino življenja, ampak za globino.", "avtor": "Ralph Waldo Emerson"},
    {"citat": "Življenje je res preprosto, a ga želimo zapletati.", "avtor": "Konfucij"},
    {"citat": "Živite na soncu, plavajte v morju, pijte divji zrak.", "avtor": "Ralph Waldo Emerson"},
    {"citat": "Ne spominjamo se dni, ampak trenutkov.", "avtor": "Cesare Pavese"},
    {"citat": "Življenje je kratko in na vas je, da si ga osladite.", "avtor": "Sarah Louise Delany"},
    {"citat": "Živite polno življenje in se osredotočite na pozitivne stvari.", "avtor": "Matt Cameron"},
    {"citat": "Življenje je najlepša pravljica.", "avtor": "Hans Christian Andersen"},
    {"citat": "Življenje je sestavljeno iz številnih ločitev, ki so varjene skupaj.", "avtor": "Charles Dickens"},
    {"citat": "Smisel življenja je življenje z namenom.", "avtor": "Robert Byrne"},
    {"citat": "Življenje je ali drzna pustolovščina ali nič.", "avtor": "Helen Keller"},
    {"citat": "Najboljša možnost, da predvidite svojo prihodnost, je, da jo ustvarite.", "avtor": "Peter Drucker"},
    {"citat": "V glavi imaš možgane. V čevljih imaš noge. Lahko se usmerite v katerokoli smer.", "avtor": "Dr. Seuss"},
    {"citat": "Edina omejitev za uresničitev jutrišnjega dne so naši dvomi o današnjem.", "avtor": "Franklin D. Roosevelt"},
    {"citat": "Vedno se zdi nemogoče, dokler ni opravljeno.", "avtor": "Nelson Mandela"},
    {"citat": "Najboljše maščevanje je velik uspeh.", "avtor": "Frank Sinatra"},
    {"citat": "Kar je za nami in kar je pred nami, je malenkost v primerjavi s tem, kar je v nas.", "avtor": "Henry David Thoreau"},
    {"citat": "Verjemi, da zmoreš, in že si na pol poti.", "avtor": "Theodore Roosevelt"},
    {"citat": "Skrivnost napredovanja je v tem, da začnete.", "avtor": "Mark Twain"},
    {"citat": "Delujte tako, kot da je to, kar počnete, pomembno. Vpliva.", "avtor": "William James"},
    {"citat": "Ko imaš sanje, jih moraš zgrabiti in nikoli izpustiti.", "avtor": "Carol Burnett"},
    {"citat": "Ni pomembno, kako počasi greš, dokler se ne ustaviš.", "avtor": "Konfucij"},
    {"citat": "Omejite svoje 'vedno' in 'ne'.", "avtor": "Amy Poehler"},
    {"citat": "Začnite tam, kjer ste. Uporabite, kar imate. Naredite, kar lahko.", "avtor": "Arthur Ashe"},
    {"citat": "Bodi obrnjen proti soncu in sence bodo padle za teboj.", "avtor": "Walt Whitman"},
    {"citat": "Uspeh je hoditi od neuspeha do neuspeha brez izgube navdušenja.", "avtor": "Winston Churchill"},
    {"citat": "Edino mesto, kjer je uspeh pred delom, je v slovarju.", "avtor": "Vidal Sassoon"},
    {"citat": "Uspeh običajno pride k tistim, ki so preveč zaposleni, da bi ga iskali.", "avtor": "Henry David Thoreau"},
    {"citat": "Ne bojte se odreči dobremu, da bi dosegli veliko.", "avtor": "John D. Rockefeller"},
    {"citat": "Pot do uspeha in pot do neuspeha sta skoraj povsem enaki.", "avtor": "Colin R. Davis"},
    {"citat": "Uspeh ni le v tem, kar dosežeš v svojem življenju, ampak tudi v tem, k čemu navdihuješ druge.", "avtor": "Neznano"},
    {"citat": "Uspeh ni v tem, kako visoko si se povzpel, ampak v tem, kako pozitivno spreminjaš svet.", "avtor": "Roy T. Bennett"},
    {"citat": "Prihodnost pripada tistim, ki verjamejo v lepoto svojih sanj.", "avtor": "Eleanor Roosevelt"},
    {"citat": "Uspeh je dobiti, kar si želiš, sreča je želeti, kar dobiš.", "avtor": "W. P. Kinsella"},
    {"citat": "Nikoli nisem sanjal o uspehu. Zanj sem delal.", "avtor": "Estée Lauder"},
    {"citat": "Svoj uspeh pripisujem temu: Nikoli nisem dal ali sprejel nobenega izgovora.", "avtor": "Florence Nightingale"},
    {"citat": "Uspeh ni v tem, kaj imaš, ampak v tem, kdo si.", "avtor": "Bo Bennett"},
    {"citat": "Uspeh je vsota majhnih prizadevanj, ki se ponavljajo iz dneva v dan.", "avtor": "Robert Collier"},
    {"citat": "Mislim, torej sem.", "avtor": "René Descartes"},
    {"citat": "Kar nas ne ubije, nas okrepi.", "avtor": "Friedrich Nietzsche"},
    {"citat": "Ne sprašuj, kaj lahko tvoja država stori zate, ampak kaj lahko ti storiš za svojo državo.", "avtor": "John F. Kennedy"},
    {"citat": "Edina stvar, ki se je moramo bati, je strah sam.", "avtor": "Franklin D. Roosevelt"},
    {"citat": "Imam sanje.", "avtor": "Martin Luther King Jr."},
    {"citat": "Ostanite mirni in nadaljujte.", "avtor": "Britanska vlada"},
    {"citat": "Biti ali ne biti, to je vprašanje.", "avtor": "William Shakespeare"},
    {"citat": "Dajte mi svobodo ali smrt!", "avtor": "Patrick Henry"},
    {"citat": "Vsi ljudje so ustvarjeni enaki.", "avtor": "Deklaracija o neodvisnosti, ZDA"},
    {"citat": "Prišel sem, videl sem, zmagal sem.", "avtor": "Julij Cezar"},
    {"citat": "Znanje je moč.", "avtor": "Francis Bacon"},
    {"citat": "Edina prava modrost je v tem, da veš, da ničesar ne veš.", "avtor": "Sokrat"},
    {"citat": "Motiti se je človeško, odpuščati pa božansko.", "avtor": "Alexander Pope"},
    {"citat": "Carpe diem. Izkoristite dan, fantje. Naj bo vaše življenje izjemno.", "avtor": "John Keating (Robin Williams)"},
    {"citat": "Kjer je ljubezen, je življenje.", "avtor": "Mahatma Gandhi"},
    {"citat": "Ljubezen ne pozna ovir. Preskakuje ovire, ograje in zidove, da bi prišla na cilj polna upanja.", "avtor": "Maya Angelou"},
    {"citat": "Veš, da si zaljubljen, ko ne moreš zaspati, ker je resničnost končno boljša od sanj.", "avtor": "Dr. Seuss"},
    {"citat": "Najboljša stvar, ki se je lahko v življenju držimo, je drug drugega.", "avtor": "Audrey Hepburn"},
    {"citat": "Ljubezen je sestavljena iz ene duše, ki živi v dveh telesih.", "avtor": "Aristotel"},
    {"citat": "Ljubiti in biti ljubljen pomeni čutiti sonce z obeh strani.", "avtor": "David Viscott"},
    {"citat": "Vedno se srečajmo z nasmehom, saj je nasmeh začetek ljubezni.", "avtor": "Mati Terezija"},
    {"citat": "Ljubezen je stanje, v katerem je sreča druge osebe bistvena za tvojo lastno srečo.", "avtor": "Robert A. Heinlein"},
    {"citat": "Nekoga ne ljubiš zaradi njegovega videza, oblačil ali prefinjenega avtomobila, ampak zato, ker poje pesem, ki jo lahko slišiš samo ti.", "avtor": "Oscar Wilde"},
    {"citat": "Ljubezen je takrat, ko je sreča druge osebe pomembnejša od tvoje.", "avtor": "H. Jackson Brown Jr."},
    {"citat": "Ljubezen je prijateljstvo v glasbi.", "avtor": "Joseph Campbell"},
    {"citat": "Srce ima svoje razloge, o katerih razum ne ve ničesar.", "avtor": "Blaise Pascal"},
    {"citat": "Ljubezen je neskončno odpuščanje. Odpuščanje je ključ do delovanja in svobode.", "avtor": "Maya Angelou"},
    {"citat": "Ljubiti ni nič. Biti ljubljen je nekaj. Ljubiti in biti ljubljen pa je vse.", "avtor": "T. Tolis"},
    {"citat": "Če te nekdo močno ljubi, ti daje moč, če nekoga globoko ljubiš, pa pogum.", "avtor": "Lao Tzu"},
    {"citat": "Sreča je odvisna od nas samih.", "avtor": "Aristotel"},
    {"citat": "Vsako minuto jeze izgubiš šestdeset sekund sreče.", "avtor": "Ralph Waldo Emerson"},
    {"citat": "Najbolj srečni ljudje nimajo vsega najboljšega, ampak iz vsega naredijo najboljše.", "avtor": "Neznano"},
    {"citat": "Sreča je skrivnost vsake lepote. Brez sreče ni lepote.", "avtor": "Christian Dior"},
    {"citat": "Sreča je topel kuža.", "avtor": "Charles M. Schulz"},
    {"citat": "Sreča ni cilj, temveč stranski produkt dobro preživetega življenja.", "avtor": "Eleanor Roosevelt"},
    {"citat": "Večina ljudi je tako srečna, kot si zamislijo.", "avtor": "Abraham Lincoln"},
    {"citat": "Najboljši način, da se razvedriš, je, da poskušaš razvedriti nekoga drugega.", "avtor": "Mark Twain"},
    {"citat": "Sreča je smer, ne kraj.", "avtor": "Sydney J. Harris"},
    {"citat": "Bodimo hvaležni ljudem, ki nas osrečujejo, saj so očarljivi vrtnarji, zaradi katerih cvetijo naše duše.", "avtor": "Marcel Proust"},
    {"citat": "Veselje življenja je v tem, da človek uporablja svojo energijo, da nenehno raste, se nenehno spreminja in uživa v vsaki novi izkušnji.", "avtor": "Aleister Crowley"},
    {"citat": "Sreča je stanje aktivnosti.", "avtor": "Aristotel"},
    {"citat": "Poznavanje samega sebe je začetek vsake modrosti.", "avtor": "Aristotel"},
    {"citat": "Naložba v znanje se najbolje obrestuje.", "avtor": "Benjamin Franklin"},
    {"citat": "Več ko berem, več ko pridobivam, bolj sem prepričan, da ne vem ničesar.", "avtor": "Voltaire"},
    {"citat": "Ne gre za to, da sem tako pameten. Toda pri vprašanjih ostanem veliko dlje.", "avtor": "Albert Einstein"},
    {"citat": "Modrost se začne v čudenju.", "avtor": "Sokrat"},
    {"citat": "Edina stvar, ki me ovira pri učenju, je moja izobrazba.", "avtor": "Albert Einstein"},
    {"citat": "Znanje govori, modrost pa posluša.", "avtor": "Jimi Hendrix"},
    {"citat": "Modrega nas ne naredi spomin na preteklost, ampak odgovornost za prihodnost.", "avtor": "George Bernard Shaw"},
    {"citat": "Naloga izobraževanja je naučiti človeka intenzivno in kritično razmišljati.", "avtor": "Martin Luther King Jr."},
    {"citat": "Edina prava napaka je tista, iz katere se ničesar ne naučimo.", "avtor": "John Powell"},
    {"citat": "Modrost je nagrada, ki jo dobiš za vse življenje poslušanja, ko bi raje govoril.", "avtor": "Mark Twain"},
    {"citat": "Začetek modrosti je opredelitev pojmov.", "avtor": "Sokrat"},
    {"citat": "Več ko boš bral, več stvari boš vedel. Več kot boš izvedel, več krajev boš obiskal.", "avtor": "Dr. Seuss"},
    {"citat": "Svoje rane spremenite v modrost.", "avtor": "Oprah Winfrey"},
    {"citat": "Vodja je tisti, ki pozna pot, gre po njej in jo kaže.", "avtor": "John C. Maxwell"},
    {"citat": "Naloga vodenja je ustvariti več vodij in ne več sledilcev.", "avtor": "Ralph Nader"},
    {"citat": "Pri vodenju ne gre za to, da ste glavni. Gre za to, da poskrbiš za tiste, ki so ti zaupani.", "avtor": "Simon Sinek"},
    {"citat": "Preden postanete vodja, je uspeh odvisen predvsem od tega, kako se razvijate. Ko postanete vodja, je uspeh povezan z rastjo drugih.", "avtor": "Jack Welch"},
    {"citat": "Največji vodja ni nujno tisti, ki naredi največ. Je tisti, ki ljudi pripravi do tega, da naredijo največje stvari.", "avtor": "Ronald Reagan"},
    {"citat": "Vodja je najboljši, ko ljudje komaj vedo, da obstaja, ko je njegovo delo opravljeno, ko je njegov cilj izpolnjen, bodo rekli: to smo naredili sami.", "avtor": "Lao Tzu"},
    {"citat": "Inovacije razlikujejo med vodjo in sledilcem.", "avtor": "Steve Jobs"},
    {"citat": "Voditeljstvo je sposobnost uresničevanja vizije.", "avtor": "Warren Bennis"},
    {"citat": "Umetnost vodenja je reči ne in ne da. Zelo enostavno je reči da.", "avtor": "Tony Blair"},
    {"citat": "Vodja vodi ljudi tja, kamor želijo. Velik vodja pa ljudi pelje tja, kamor si ne želijo, a bi morali.", "avtor": "Rosalynn Carter"},
    {"citat": "Ne vodite tako, da ljudi udarjate po glavi - to je napad in ne vodenje.", "avtor": "Dwight D. Eisenhower"},
    {"citat": "Vodenje je sprostitev potenciala ljudi, da postanejo boljši.", "avtor": "Bill Bradley"},
    {"citat": "Najboljši vodje so tisti, ki se želijo obkrožiti s pomočniki in sodelavci, ki so pametnejši od njih.", "avtor": "John C. Maxwell"},
    {"citat": "Izziv vodenja je biti močan, a ne grob; biti prijazen, a ne šibak; biti drzen, a ne nasilnež; biti premišljen, a ne len, biti ponižen, a ne bojazljiv; biti ponosen, a ne aroganten; imeti humor, a brez norosti.", "avtor": "Jim Rohn"},
    {"citat": "Pravo vodenje je usmerjanje drugih k uspehu - zagotavljanje, da vsi delajo po svojih najboljših močeh, da opravljajo delo, za katerega so se zavezali, in da ga opravljajo dobro.", "avtor": "Bill Owens"},
    {"citat": "Človek, ki premakne goro, začne z odnašanjem majhnih kamnov.", "avtor": "Konfucij"},
    {"citat": "Sedemkrat padeš, osemkrat vstaneš.", "avtor": "Japonski pregovor"},
    {"citat": "Vztrajnost ni dolga tekma, ampak več kratkih tekem ena za drugo.", "avtor": "Walter Elliot"},
    {"citat": "Težji ko je spopad, večje je zmagoslavje.", "avtor": "George Washington"},
    {"citat": "Veliko življenjskih neuspehov so ljudje, ki se niso zavedali, kako blizu so bili uspehu, ko so obupali.", "avtor": "Thomas A. Edison"},
    {"citat": "Mnogi ljudje z vztrajnostjo dosežejo uspeh iz nečesa, kar se je zdelo obsojeno na neuspeh.", "avtor": "Benjamin Disraeli"},
    {"citat": "Vztrajnost pomeni, da ti 19-krat spodleti, 20-krat pa ti uspe.", "avtor": "Julie Andrews"},
    {"citat": "Reka se ne prebija skozi skalo zaradi svoje moči, temveč zaradi svoje vztrajnosti.", "avtor": "Jim Watkins"},
    {"citat": "Ne obupajte. Pogosto je zadnji ključ v skupini tisti, ki odpre ključavnico.", "avtor": "Neznano"},
    {"citat": "Ko svet reče: 'Obupaj', upanje zašepeta: 'Poskusi še enkrat'.", "avtor": "Neznano"},
    {"citat": "Vztrajnost, skrivnost vseh zmag.", "avtor": "Victor Hugo"},
    {"citat": "Našli bomo pot ali pa jo ustvarili.", "avtor": "Hanibal"},
    {"citat": "Ne ukvarjaj se s preteklostjo, ne sanjaj o prihodnosti, osredotoči se na sedanji trenutek.", "avtor": "Buda"},
    {"citat": "Sedanji trenutek je edini čas, nad katerim imamo oblast.", "avtor": "Thích Nhất Hạnh"},
    {"citat": "Včeraj je zgodovina, jutri je skrivnost, danes pa je dar. Zato se imenuje sedanjost.", "avtor": "Bil Keane"},
    {"citat": "Živeti moraš v sedanjosti, se spustiti na vsak val, najti svojo večnost v vsakem trenutku.", "avtor": "Henry David Thoreau"},
    {"citat": "Globoko se zavedajte, da je sedanji trenutek vse, kar imate.", "avtor": "Eckhart Tolle"},
    {"citat": "Bodite srečni v tem trenutku, to je dovolj. Vsak trenutek je vse, kar potrebujemo, ne več.", "avtor": "Mati Terezija"},
    {"citat": "Čuječnost je način, kako se spoprijateljiti s seboj in s svojim doživljanjem.", "avtor": "Jon Kabat-Zinn"},
    {"citat": "Življenje je ples. Pozornost je opazovanje tega plesa.", "avtor": "Amit Ray"},
    {"citat": "Kjer koli ste, bodite vsi tam.", "avtor": "Jim Elliot"},
    {"citat": "Bodite prisotni v vseh stvareh in hvaležni za vse.", "avtor": "Maya Angelou"},
    {"citat": "Občutki prihajajo in odhajajo kot oblaki na vetrovnem nebu. Zavestno dihanje je moje sidro.", "avtor": "Thích Nhất Hạnh"},
    {"citat": "Poglej mimo svojih misli, da boš lahko pil čisti nektar tega trenutka.", "avtor": "Rumi"},
    {"citat": "Pozornost je ključ do sedanjega trenutka.", "avtor": "Eckhart Tolle"},
    {"citat": "Meditacija ni izogibanje, ampak mirno srečanje z resničnostjo.", "avtor": "Thích Nhất Hạnh"},
    {"citat": "Pozornost ni težka, le spomniti se je moramo.", "avtor": "Sharon Salzberg"},
    {"citat": "Ustvarjalnost je inteligenca, ki se zabava.", "avtor": "Albert Einstein"},
    {"citat": "Domišljija je začetek ustvarjanja. Predstavljaš si, kar si želiš, hočeš, kar si predstavljaš, in končno ustvariš, kar si želiš.", "avtor": "George Bernard Shaw"},
    {"citat": "Ustvarjalnosti ne moreš izčrpati. Več kot je uporabiš, več je imaš.", "avtor": "Maya Angelou"},
    {"citat": "Za ustvarjalnost je potreben pogum.", "avtor": "Henri Matisse"},
    {"citat": "Če želimo živeti ustvarjalno življenje, moramo izgubiti strah pred tem, da bi se motili.", "avtor": "Joseph Chilton Pearce"},
    {"citat": "Logika vas bo pripeljala od točke A do točke B, domišljija pa vas bo popeljala povsod.", "avtor": "Albert Einstein"},
    {"citat": "Vsak otrok je umetnik. Problem je, kako ostati umetnik, ko odrastemo.", "avtor": "Pablo Picasso"},
    {"citat": "Ustvarjalnost je videti, kar so videli vsi, in misliti, kar še nihče ni mislil.", "avtor": "Albert Einstein"},
    {"citat": "Domišljija je vse. Je predogled prihajajočih življenjskih zanimivosti.", "avtor": "Albert Einstein"},
    {"citat": "Ne moreš čakati na navdih. Za njim moraš iti s palico.", "avtor": "Jack London"},
    {"citat": "Pravi znak inteligence ni znanje, temveč domišljija.", "avtor": "Albert Einstein"},
    {"citat": "Bistveni vidik ustvarjalnosti je, da se ne bojimo neuspeha.", "avtor": "Edwin Land"},
    {"citat": "Ustvarjalnost je nalezljiva, prenesite jo naprej.", "avtor": "Albert Einstein"},
    {"citat": "Domišljija je pomembnejša od znanja. Znanje je omejeno. Domišljija obdaja svet.", "avtor": "Albert Einstein"},
    {"citat": "Ne razmišljaj. Razmišljanje je sovražnik ustvarjalnosti. Je samozavestno in vse, kar je samozavestno, je slabo. Ne morete poskušati narediti stvari. Stvari preprosto morate narediti.", "avtor": "Ray Bradbury"},
    {"citat": "Pogum ni odsotnost strahu, temveč odločitev, da je nekaj drugega pomembnejše od strahu.", "avtor": "Ambrose Redmoon"},
    {"citat": "Potreben je pogum, da odrasteš in postaneš to, kar v resnici si.", "avtor": "E.E. Cummings"},
    {"citat": "Kdor ni dovolj pogumen, da bi tvegal, v življenju ne bo dosegel ničesar.", "avtor": "Muhammad Ali"},
    {"citat": "Pogum je milost pod pritiskom.", "avtor": "Ernest Hemingway"},
    {"citat": "Moč, pogum in samozavest si pridobiš z vsako izkušnjo, v kateri se zares ustaviš in pogledaš strahu v obraz.", "avtor": "Eleanor Roosevelt"},
    {"citat": "Vsak dan naredite eno stvar, ki vas je strah.", "avtor": "Eleanor Roosevelt"},
    {"citat": "Pogum ne rjove vedno. Včasih je pogum tihi glas ob koncu dneva, ki pravi: 'Jutri bom poskusil še enkrat'.", "avtor": "Mary Anne Radmacher"},
    {"citat": "Za zapustitev obale je potreben pogum. Toda če ne zapustite obale, ne boste nikoli odkrili novih oceanov.", "avtor": "Neznano"},
    {"citat": "Sreča je naklonjena pogumnim.", "avtor": "Vergilij"},
    {"citat": "Pogum pomeni, da te je na smrt strah, a vseeno osedlaš konj.", "avtor": "John Wayne"},
    {"citat": "Lahko izbereš pogum ali udobje, ne moreš pa izbrati obojega.", "avtor": "Brené Brown"},
    {"citat": "Strah je reakcija. Pogum je odločitev.", "avtor": "Winston Churchill"},
    {"citat": "Pogum je moč, da se znebimo znanega.", "avtor": "Raymond Lindquist"},
    {"citat": "Pogum je odpor proti strahu, obvladovanje strahu, ne pa odsotnost strahu.", "avtor": "Mark Twain"},
    {"citat": "Namen življenja ni biti srečen. Namen je biti koristen, častan, sočuten, da bi bilo pomembno, da ste živeli in živeli dobro.", "avtor": "Ralph Waldo Emerson"},
    {"citat": "Vaš življenjski cilj je najti svoj namen in se mu posvetiti z vsem srcem in dušo.", "avtor": "Buda"},
    {"citat": "Dva najpomembnejša dneva v življenju sta dan, ko se rodiš, in dan, ko izveš, zakaj.", "avtor": "Mark Twain"},
    {"citat": "Kdor ima zakaj živeti, lahko prenese skoraj vsak način.", "avtor": "Friedrich Nietzsche"},
    {"citat": "Smisel življenja je najti svoj dar. Smisel življenja je, da ga podariš.", "avtor": "Pablo Picasso"},
    {"citat": "Prizadevanja in pogum niso dovolj brez cilja in usmeritve.", "avtor": "John F. Kennedy"},
    {"citat": "Pozabiti svoj namen je najpogostejša oblika neumnosti.", "avtor": "Friedrich Nietzsche"},
    {"citat": "Skrivnost uspeha je v stalnosti cilja.", "avtor": "Benjamin Disraeli"},
    {"citat": "Določenost cilja je izhodišče vseh dosežkov.", "avtor": "W. Clement Stone"},
    {"citat": "Duša, ki nima stalnega življenjskega cilja, je izgubljena; biti povsod pomeni biti nikjer.", "avtor": "Michel de Montaigne"},
    {"citat": "Resnične sreče ... ne dosežemo s samozadovoljevanjem, temveč z zvestobo vrednemu cilju.", "avtor": "Helen Keller"},
    {"citat": "Veliki umi imajo cilje, drugi pa želje.", "avtor": "Washington Irving"},
    {"citat": "Skrivnost človeškega obstoja ni le v tem, da ostaneš živ, ampak da najdeš nekaj, za kar lahko živiš.", "avtor": "Fjodor Dostojevski"},
    {"citat": "Življenje nikoli ni neznosno zaradi okoliščin, temveč le zaradi pomanjkanja smisla in cilja.", "avtor": "Viktor Frankl"}
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
    import os
    port = int(os.environ.get("PORT", 5000))
    aplikacija.run(debug=False, host='0.0.0.0', port=port)