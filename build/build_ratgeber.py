#!/usr/bin/env python3
"""smzhHub Ratgeber – Lead-Gen- + SEO-Artikel zu den Entscheidungs-Finanzfragen.

Erstellt je Finanzfrage aus dem Entscheidungs-Karussell einen eigenständigen
Artikel (/de/ratgeber-...). Ziel: maximale Lead-Generierung, sauberes On-Page-SEO
(Title, Meta, H-Struktur, FAQ-/Article-/Breadcrumb-Schema, interne+externe Links).

Schweizer Rechtschreibung (ss). Nutzt das Chrome + V5-CSS via build_hub_v5.build_page.
"""
import re, os, json, html as H
import build_hub_v5 as V

BASE = V.BASE
link = V.link
def esc(s): return H.escape(s or '')

ORG = {'@type': 'Organization', 'name': 'smzh', 'url': 'https://smzh.ch'}
BOOK = '/de/terminvereinbaren/'

# ---------------------------------------------------------------------------
# Inhalt: je Artikel ein Dict. body = Liste von (h2, html). p()/ul()/tbl() Helfer.
# ---------------------------------------------------------------------------
def p(*parts): return ''.join(f'<p>{t}</p>' for t in parts)
def ul(items): return '<ul>'+''.join(f'<li>{t}</li>' for t in items)+'</ul>'
def a(href, text): return f'<a href="{link(href)}">{text}</a>'
def ax(href, text): return f'<a href="{href}" rel="noopener" target="_blank">{text}</a>'

ARTICLES = [
{
 'slug':'ratgeber-saron-oder-festhypothek','img':'/de/artikel/snb-zinsentscheid-juni/','imgalt':'SARON oder Festhypothek 2026: Hypothekarzinsen im Vergleich','rubrik':'Eigenheim & Hypothek','rubrik_href':'/de/smzhub-eigenheim/',
 'title':'SARON oder Festhypothek 2026: Was lohnt sich?',
 'h1':'SARON oder Festhypothek: Welche Strategie passt 2026?',
 'h1_short':'SARON oder Festhypothek',
 'dek':'Tiefe Zinsen oder Planungssicherheit? Was bei der Wahl zwischen SARON- und Festhypothek 2026 wirklich zählt – und wie Sie für Ihre Situation entscheiden.',
 'desc':'SARON oder Festhypothek 2026? Vor- und Nachteile, Kosten, Risiko und für wen sich welche Hypothek lohnt – verständlich erklärt mit Entscheidungshilfe von smzh.',
 'kw':'SARON oder Festhypothek','kw2':['Festhypothek','SARON Hypothek','Hypothek 2026','Hypothekarzinsen'],
 'cta':('/de/hypothekenarten-im-vergleich/','Hypothekenarten vergleichen'),
 'cta_h':'Welche Hypothek passt zu Ihrer Situation?','cta_p':'Lassen Sie Laufzeit, Tragbarkeit und Zinsstrategie unverbindlich prüfen – bevor Sie sich für Jahre festlegen.',
 'lead':'Die Wahl zwischen einer <strong>SARON- und einer Festhypothek</strong> ist 2026 eine der folgenreichsten Finanzentscheidungen für Eigenheimbesitzer. Sie bestimmt über Jahre, wie viel Sie zahlen – und wie viel Planungssicherheit Sie haben. Dieser Ratgeber zeigt, wann sich welche Variante lohnt.',
 'body':[
  ('Was ist der Unterschied?', p(
    'Die <strong>SARON-Hypothek</strong> ist an den kurzfristigen Referenzzinssatz SARON gekoppelt und wird laufend angepasst – sinken die Zinsen, profitieren Sie sofort; steigen sie, zahlen Sie mehr. Die <strong>Festhypothek</strong> fixiert den Zinssatz über eine feste Laufzeit (meist 2 bis 10 Jahre) und gibt Ihnen volle Budgetsicherheit.',
    'Anders gesagt: Bei SARON tragen Sie das Zinsrisiko selbst und sparen dafür im Schnitt die Risikoprämie der Bank. Bei der Festhypothek kaufen Sie sich Sicherheit – und zahlen dafür einen Aufschlag.')),
  ('SARON oder Festhypothek 2026 – die Ausgangslage', p(
    'Nach den Leitzinssenkungen der Schweizerischen Nationalbank ist das Zinsumfeld 2026 vergleichsweise tief. Das macht beide Varianten attraktiv: SARON-Hypotheken sind günstig, gleichzeitig lassen sich auch langfristige Festhypothekarzinsen auf moderatem Niveau sichern.',
    'Entscheidend ist deshalb weniger die Zinsprognose – die niemand sicher kennt – als Ihre persönliche Risikofähigkeit und Ihr Bedürfnis nach Planbarkeit. Aktuelle Einordnungen liefert der '+a('/de/smzhub-eigenheim/','smzhHub-Bereich Eigenheim & Hypothek')+'.')),
  ('Vor- und Nachteile im Überblick',
    '<table class="art-table"><thead><tr><th>Kriterium</th><th>SARON-Hypothek</th><th>Festhypothek</th></tr></thead><tbody>'
    '<tr><td>Zinskosten</td><td>meist tiefer im Schnitt</td><td>Aufschlag für Sicherheit</td></tr>'
    '<tr><td>Planungssicherheit</td><td>gering (schwankt)</td><td>hoch (fix)</td></tr>'
    '<tr><td>Risiko</td><td>Sie tragen das Zinsrisiko</td><td>Bank trägt das Risiko</td></tr>'
    '<tr><td>Flexibilität</td><td>meist kurz kündbar</td><td>an Laufzeit gebunden</td></tr>'
    '<tr><td>Eignung</td><td>finanzielles Polster, Risikotoleranz</td><td>knappes Budget, Sicherheitsbedürfnis</td></tr>'
    '</tbody></table>'),
  ('Für wen sich welche Hypothek lohnt', p(
    '<strong>Die SARON-Hypothek passt</strong>, wenn Sie ein finanzielles Polster haben, schwankende Kosten verkraften und langfristig von tieferen Durchschnittszinsen profitieren möchten.',
    '<strong>Die Festhypothek passt</strong>, wenn Ihr Budget knapp kalkuliert ist, Sie ruhig schlafen wollen oder eine Familienphase mit fixen Ausgaben planen. Viele Eigentümer kombinieren beides und teilen die Hypothek in Tranchen – so streuen Sie das Zinsrisiko über mehrere Laufzeiten.')),
  ('So treffen Sie die Entscheidung', p('Prüfen Sie drei Fragen, bevor Sie unterschreiben:')+ul([
    'Wie viel monatliche Schwankung verträgt mein Budget – ehrlich gerechnet?',
    'Wie lange will ich die Finanzierung halten, und stehen Veränderungen (Umbau, Verkauf, Pensionierung) an?',
    'Wie ist meine Hypothek gestaffelt – laufen alle Tranchen gleichzeitig aus?',
  ])+p('Die offizielle Funktionsweise des Referenzzinssatzes erläutert die '+ax('https://www.snb.ch','Schweizerische Nationalbank')+'. Für die individuelle Rechnung lohnt sich eine neutrale Einordnung.')),
 ],
 'faq':[
  ('Ist eine SARON-Hypothek 2026 günstiger als eine Festhypothek?','Im langjährigen Durchschnitt sind SARON-Hypotheken oft günstiger, weil die Risikoprämie der Festhypothek entfällt. Garantiert ist das aber nicht – steigen die Zinsen, kann SARON teurer werden. Entscheidend sind Ihre Risikofähigkeit und Ihr Budget.'),
  ('Kann ich von SARON zu einer Festhypothek wechseln?','Ja. SARON-Hypotheken lassen sich in der Regel mit kurzer Frist in eine Festhypothek umwandeln. So können Sie ein tiefes Zinsniveau sichern, wenn sich die Lage ändert. Die Konditionen hängen vom Anbieter ab.'),
  ('Was ist eine Tranchen-Strategie?','Sie teilen Ihre Hypothek auf mehrere Laufzeiten oder Modelle auf. So läuft nicht alles gleichzeitig aus, und Sie verteilen das Zinsrisiko – ein bewährter Mittelweg zwischen Sicherheit und Kostenvorteil.'),
 ],
 'related':[('Wie viel Eigenkapital brauche ich wirklich?','/de/ratgeber-eigenkapital-eigenheim/'),
            ('Reicht mein Einkommen für die Bank? Tragbarkeit erklärt','/de/ratgeber-tragbarkeit-hypothek/'),
            ('Hypothek amortisieren oder das Geld investieren?','/de/ratgeber-amortisieren-oder-investieren/')],
},
{
 'slug':'ratgeber-eigenheim-kaufen-oder-warten','img':'/de/artikel/zuercher-wohnungsinitiativen/','imgalt':'Eigenheim kaufen oder warten – Immobilienkauf in der Schweiz 2026','rubrik':'Eigenheim & Hypothek','rubrik_href':'/de/smzhub-eigenheim/',
 'title':'Eigenheim kaufen oder warten? Ratgeber 2026',
 'h1':'Eigenheim kaufen oder warten? Die Entscheidung 2026',
 'h1_short':'Kaufen oder warten?',
 'dek':'Preise, Eigenkapital und Tragbarkeit spielen 2026 zusammen. Woran Sie erkennen, ob sich der Kauf für Sie jetzt lohnt – oder ob Warten die klügere Wahl ist.',
 'desc':'Eigenheim kaufen oder warten 2026? Wie Preise, Zinsen, Eigenkapital und Tragbarkeit zusammenspielen – mit klarer Entscheidungshilfe und Checkliste von smzh.',
 'kw':'Eigenheim kaufen','kw2':['Eigenheim kaufen oder warten','Immobilie kaufen 2026','Tragbarkeit','Eigenkapital'],
 'cta':('/de/immobilienbewertung-rechner/','Tragbarkeit berechnen'),
 'cta_h':'Können Sie sich Ihr Wunschobjekt leisten?','cta_p':'Prüfen Sie Tragbarkeit und Eigenkapital für ein konkretes Objekt – bevor Sie ein Angebot machen.',
 'lead':'<strong>Eigenheim kaufen oder warten?</strong> Diese Frage stellen sich 2026 viele – zwischen schwankenden Preisen, tieferen Zinsen und knappem Angebot. Die ehrliche Antwort hängt weniger vom Markt ab als von Ihrer persönlichen Ausgangslage. Dieser Ratgeber macht sie greifbar.',
 'body':[
  ('Worauf es wirklich ankommt', p(
    'Die Marktlage ist nur die halbe Wahrheit. Ob sich ein Kauf lohnt, entscheiden drei persönliche Faktoren: Ihr <strong>Eigenkapital</strong>, Ihre <strong>Tragbarkeit</strong> und Ihr <strong>Zeithorizont</strong>. Wer mindestens fünf bis zehn Jahre am selben Ort bleiben will, übersteht auch Preisdellen – kurzfristige Käufer tragen ein höheres Risiko.')),
  ('Die drei Tragbarkeits-Faustregeln', p('In der Schweiz prüfen Banken den Kauf nach festen Regeln:')+ul([
    '<strong>20 % Eigenkapital</strong> des Kaufpreises, davon mindestens 10 % aus eigenen Mitteln (nicht aus der Pensionskasse).',
    '<strong>Kalkulatorischer Zins von rund 5 %</strong>: Die Bank rechnet bewusst mit einem höheren Zins als heute, um Reserven zu prüfen.',
    '<strong>Maximal ein Drittel des Bruttoeinkommens</strong> für Zins, Amortisation und Nebenkosten zusammen.',
  ])+p('Mehr dazu im Ratgeber '+a('/de/ratgeber-tragbarkeit-hypothek/','Reicht mein Einkommen für die Bank?')+'.')),
  ('Kaufen oder warten – wann was sinnvoll ist',
    '<table class="art-table"><thead><tr><th>Eher kaufen, wenn…</th><th>Eher warten, wenn…</th></tr></thead><tbody>'
    '<tr><td>Eigenkapital und Tragbarkeit stimmen</td><td>Eigenkapital noch unter 20 % liegt</td></tr>'
    '<tr><td>Sie 5–10+ Jahre bleiben wollen</td><td>Wohnsituation in 2–3 Jahren unklar ist</td></tr>'
    '<tr><td>Sie ein passendes Objekt gefunden haben</td><td>Sie unter Zeitdruck «irgendetwas» kaufen würden</td></tr>'
    '<tr><td>Budget auch bei 5 % Zins trägt</td><td>schon der heutige Zins das Budget sprengt</td></tr>'
    '</tbody></table>'),
  ('Warten hat auch Kosten', p(
    'Wer wartet, zahlt weiter Miete und spart vielleicht Eigenkapital an – verpasst aber möglichen Wertzuwachs und zahlt bei steigenden Preisen später mehr. «Warten auf den perfekten Zeitpunkt» führt selten zum Ziel. Sinnvoller ist, die eigenen Voraussetzungen gezielt zu verbessern: Eigenkapital aufbauen, Tragbarkeit erhöhen, Finanzierung vorbereiten.')),
 ],
 'faq':[
  ('Wie viel Eigenkapital brauche ich zum Kauf?','Mindestens 20 % des Kaufpreises, davon 10 % aus «harten» eigenen Mitteln ausserhalb der Pensionskasse. Bei 800 000 Franken Kaufpreis sind das 160 000 Franken, davon 80 000 aus eigenem Erspartem.'),
  ('Lohnt es sich, auf tiefere Preise zu warten?','Nur, wenn Ihre persönliche Lage unklar ist. Den perfekten Marktzeitpunkt trifft kaum jemand. Wer langfristig bleibt und die Tragbarkeit erfüllt, fährt mit einem Kauf meist besser als mit Spekulation auf fallende Preise.'),
  ('Was bedeutet der kalkulatorische Zins?','Banken rechnen die Tragbarkeit mit rund 5 % statt mit dem aktuellen Zins. So stellen sie sicher, dass Sie sich das Eigenheim auch bei steigenden Zinsen leisten können.'),
 ],
 'related':[('Wie viel Eigenkapital brauche ich wirklich?','/de/ratgeber-eigenkapital-eigenheim/'),
            ('Reicht mein Einkommen für die Bank?','/de/ratgeber-tragbarkeit-hypothek/'),
            ('SARON oder Festhypothek 2026?','/de/ratgeber-saron-oder-festhypothek/')],
},
{
 'slug':'ratgeber-rente-oder-kapitalbezug','img':'/de/artikel/ahv-2030-pensionierung-planungsfrage/','imgalt':'Rente oder Kapital aus der Pensionskasse beziehen','rubrik':'Vorsorge & Pensionierung','rubrik_href':'/de/smzhub-zukunft/',
 'title':'Rente oder Kapitalbezug? Pensionskasse 2026',
 'h1':'Rente oder Kapital: Wie Sie Ihre Pensionskasse 2026 beziehen',
 'h1_short':'Rente oder Kapital?',
 'dek':'Lebenslange Sicherheit oder maximale Flexibilität? Der Bezug der Pensionskasse ist eine der grössten Geldentscheidungen – mit Folgen für Steuern, Sicherheit und Erbschaft.',
 'desc':'Rente oder Kapitalbezug aus der Pensionskasse 2026? Vorteile, Steuern, Risiken und für wen sich Rente, Kapital oder die Mischform lohnt – Entscheidungshilfe von smzh.',
 'kw':'Rente oder Kapital','kw2':['Pensionskasse Kapitalbezug','Rente oder Kapital beziehen','Pensionierung 2026','Umwandlungssatz'],
 'cta':('/de/vorsorgeanalyse/','Vorsorge analysieren'),
 'cta_h':'Rente, Kapital oder beides – was ist für Sie richtig?','cta_p':'Eine Vorsorgeanalyse zeigt Ihre lebenslange Einkommenslücke und die steuerlich beste Bezugsform.',
 'lead':'Beim Übergang in die Pensionierung steht eine unumkehrbare Frage an: <strong>Rente oder Kapital</strong> aus der Pensionskasse? Die Entscheidung betrifft 2026 Ihr Einkommen, Ihre Steuern und Ihre Erben gleichzeitig – und lässt sich später nicht korrigieren.',
 'body':[
  ('Rente: Sicherheit ein Leben lang', p(
    'Die Rente zahlt Ihnen die Pensionskasse lebenslang aus – berechnet über den <strong>Umwandlungssatz</strong>. Sie ist planbar, endet nie und schützt vor dem Risiko, das Kapital zu überleben. Nachteil: Die Rente wird voll als Einkommen besteuert, ist kaum flexibel und beim Tod fällt oft nur eine reduzierte Hinterlassenenrente an.')),
  ('Kapital: Flexibilität und Kontrolle', p(
    'Beim Kapitalbezug erhalten Sie Ihr Guthaben einmalig. Vorteile: volle Flexibilität, Vererbbarkeit und eine einmalige, separat besteuerte Auszahlung zu einem reduzierten Satz. Der Preis dafür: Sie tragen das Anlage- und Langleberisiko selbst und müssen das Geld über Jahrzehnte einteilen.')),
  ('Rente oder Kapital – der direkte Vergleich',
    '<table class="art-table"><thead><tr><th>Kriterium</th><th>Rente</th><th>Kapital</th></tr></thead><tbody>'
    '<tr><td>Sicherheit</td><td>lebenslang garantiert</td><td>abhängig von Anlage/Disziplin</td></tr>'
    '<tr><td>Flexibilität</td><td>gering</td><td>hoch</td></tr>'
    '<tr><td>Steuern</td><td>volle Einkommenssteuer, jährlich</td><td>einmalige, reduzierte Kapitalsteuer</td></tr>'
    '<tr><td>Vererbbarkeit</td><td>eingeschränkt</td><td>ja</td></tr>'
    '<tr><td>Langleberisiko</td><td>trägt die Pensionskasse</td><td>tragen Sie selbst</td></tr>'
    '</tbody></table>'),
  ('Die Mischform – oft die beste Lösung', p(
    'Viele entscheiden sich nicht für entweder/oder, sondern beziehen einen Teil als Rente (für die fixen Lebenshaltungskosten) und einen Teil als Kapital (für Flexibilität und Vererbung). So sichern Sie das Existenzminimum und behalten Spielraum. Welche Aufteilung steuerlich und finanziell optimal ist, zeigt eine '+a('/de/vorsorgeanalyse/','Vorsorgeanalyse')+'.')),
  ('Worauf Sie früh achten sollten', p('Der Kapitalbezug muss meist Jahre im Voraus angemeldet werden. Klären Sie rechtzeitig:')+ul([
    'Höhe von Rente und Kapital gemäss Vorsorgeausweis',
    'Steuerfolgen am Wohnort (Kapitalbezugssteuer ist kantonal unterschiedlich)',
    'Einkommensbedarf und feste Ausgaben im Ruhestand',
  ])+p('Grundlagen zur 2. Säule erklärt das '+ax('https://www.bsv.admin.ch','Bundesamt für Sozialversicherungen')+'.')),
 ],
 'faq':[
  ('Wird die Rente oder das Kapital höher besteuert?','Die Rente wird jährlich voll als Einkommen besteuert. Der Kapitalbezug wird einmalig und zu einem reduzierten Satz getrennt vom übrigen Einkommen besteuert. Was günstiger ist, hängt von Ihrer Situation und Ihrem Kanton ab.'),
  ('Kann ich die Entscheidung später ändern?','Nein. Der Bezug ist endgültig. Der Kapitalbezug muss zudem oft Monate bis Jahre vorher angemeldet werden. Eine frühzeitige Planung ist deshalb entscheidend.'),
  ('Was ist die Mischform?','Sie beziehen einen Teil der Pensionskasse als lebenslange Rente und einen Teil als Kapital. So kombinieren Sie Sicherheit für die Fixkosten mit Flexibilität und Vererbbarkeit.'),
 ],
 'related':[('Früher pensionieren oder weiterarbeiten?','/de/ratgeber-frueher-pensionieren/'),
            ('Lohnt sich die Säule 3a für mich?','/de/ratgeber-lohnt-sich-saeule-3a/'),
            ('Wo verschenke ich jedes Jahr Steuern?','/de/ratgeber-steuern-sparen/')],
},
{
 'slug':'ratgeber-saeule-3a-konto-oder-wertschriften','img':'/de/artikel/neue-aera-fed/','imgalt':'Säule 3a als Konto oder Wertschriften anlegen','rubrik':'Vermögen & Anlegen','rubrik_href':'/de/smzhub-vermoegen/',
 'title':'Säule 3a: Konto oder Wertschriften? 2026',
 'h1':'Säule 3a 2026: Konto oder Wertschriften?',
 'h1_short':'3a Konto oder Wertschriften?',
 'dek':'Bei der Säule 3a entscheidet die Anlageform über Jahrzehnte mehr als die Einzahlung selbst. Wann sich ein Wertschriftendepot lohnt – und wann das Konto genügt.',
 'desc':'Säule 3a als Konto oder Wertschriften 2026? Wie Zinseszins, Anlagehorizont und Risiko zusammenspielen und für wen sich ein 3a-Wertschriftendepot lohnt – Ratgeber von smzh.',
 'kw':'Konto oder Wertschriften','kw2':['Säule 3a Wertschriften','3a Depot','Säule 3a 2026','3a anlegen'],
 'cta':('/de/risikoprofil-erstellen/','Anlagestrategie einordnen'),
 'cta_h':'Welche 3a-Anlagestrategie passt zu Ihnen?','cta_p':'Ermitteln Sie Ihr Risikoprofil und den passenden Aktienanteil für Ihre Säule 3a.',
 'lead':'Bei der <strong>Säule 3a</strong> machen die meisten denselben Fehler: Sie zahlen ein – und lassen das Geld auf dem Zinskonto liegen. Dabei entscheidet 2026 die <strong>Anlageform</strong> über Jahrzehnte mehr über Ihr Vermögen als die Einzahlung selbst. Konto oder Wertschriften? Das ist die eigentliche Frage.',
 'body':[
  ('Warum die Anlageform so viel ausmacht', p(
    'Auf einem 3a-Konto liegt Ihr Geld nahezu zinslos. In einem 3a-Wertschriftendepot ist es breit in Aktien und Anleihen investiert – und profitiert über die Jahre vom Zinseszins. Über 20 bis 30 Jahre kann der Unterschied mehrere Zehntausend Franken betragen, bei identischer Einzahlung.',
    'Der Grund liegt im Zinseszins: Erträge werfen selbst wieder Erträge ab, und dieser Effekt verstärkt sich mit jedem Jahr. Wer früh beginnt, lässt der Anlage am meisten Zeit zu wirken. Da Sie jedes Jahr ohnehin denselben Betrag einzahlen, entscheidet allein die gewählte Anlageform über das Endergebnis – und damit über spürbar mehr Vermögen im Alter.')),
  ('Wann sich Wertschriften lohnen', p(
    'Wertschriften eignen sich, wenn Sie einen langen Anlagehorizont haben – also nicht in wenigen Jahren auf das Geld angewiesen sind. Je länger die Zeit bis zum Bezug, desto stärker glätten sich Marktschwankungen und desto höher fällt der erwartete Mehrertrag aus.')+ul([
    '<strong>Über 10 Jahre Horizont:</strong> hoher Aktienanteil meist sinnvoll',
    '<strong>5–10 Jahre:</strong> moderater, ausgewogener Anteil',
    '<strong>Unter 5 Jahren bis Bezug:</strong> Konto oder defensive Strategie bevorzugen',
  ])),
  ('Konto oder Wertschriften – der direkte Vergleich',
    '<table class="art-table"><thead><tr><th>Kriterium</th><th>3a-Konto</th><th>3a-Wertschriften</th></tr></thead><tbody>'
    '<tr><td>Renditechance</td><td>sehr tief</td><td>höher (langfristig)</td></tr>'
    '<tr><td>Schwankung</td><td>keine</td><td>ja, kurzfristig</td></tr>'
    '<tr><td>Eignung</td><td>kurzer Horizont, Bezug nah</td><td>langer Horizont</td></tr>'
    '<tr><td>Kosten</td><td>kaum</td><td>auf tiefe Gebühren achten</td></tr>'
    '</tbody></table>'),
  ('Worauf Sie bei einem 3a-Depot achten', p('Nicht jedes Produkt ist gleich. Entscheidend sind:')+ul([
    'tiefe Gesamtkosten (TER) – Gebühren schmälern die Rendite direkt',
    'passender Aktienanteil zu Ihrem Risikoprofil',
    'gestaffelte 3a-Konten für einen späteren steuergünstigen Bezug',
  ])+p('Ob 3a für Sie überhaupt der beste Sparort ist, klärt der Ratgeber '+a('/de/ratgeber-lohnt-sich-saeule-3a/','Lohnt sich die Säule 3a für mich?')+'. Die gesetzlichen Grundlagen der gebundenen Vorsorge der dritten Säule erläutert das '+ax('https://www.bsv.admin.ch','Bundesamt für Sozialversicherungen')+'.')),
 ],
 'faq':[
  ('Ist die Säule 3a mit Wertschriften riskant?','Kurzfristig schwanken Wertschriften. Über einen langen Anlagehorizont – wie er bei der 3a üblich ist – gleichen sich Schwankungen aber meist aus, und die Renditechance liegt deutlich über dem Konto. Entscheidend ist ein zum Bezugszeitpunkt passender Aktienanteil.'),
  ('Kann ich von Konto auf Wertschriften wechseln?','Ja, ein Wechsel der Anlageform innerhalb der Säule 3a ist möglich. Je früher Sie auf eine zum Horizont passende Strategie wechseln, desto stärker wirkt der Zinseszins.'),
  ('Wie viele 3a-Konten sollte ich haben?','Mehrere gestaffelte 3a-Konten erlauben einen über mehrere Jahre verteilten Bezug – das senkt die Kapitalbezugssteuer spürbar. Eine Beratung zeigt die optimale Staffelung.'),
 ],
 'related':[('Lohnt sich die Säule 3a für mich?','/de/ratgeber-lohnt-sich-saeule-3a/'),
            ('Wo verschenke ich jedes Jahr Steuern?','/de/ratgeber-steuern-sparen/'),
            ('Hypothek amortisieren oder investieren?','/de/ratgeber-amortisieren-oder-investieren/')],
},
{
 'slug':'ratgeber-tragbarkeit-hypothek','img':'/de/artikel/snb-zinsentscheid-juni/','imgalt':'Tragbarkeit der Hypothek 2026 berechnen','rubrik':'Eigenheim & Hypothek','rubrik_href':'/de/smzhub-eigenheim/',
 'title':'Tragbarkeit Hypothek 2026: Reicht mein Einkommen?',
 'h1':'Reicht mein Einkommen für die Bank? Tragbarkeit 2026',
 'h1_short':'Tragbarkeit der Hypothek',
 'dek':'Banken rechnen die Tragbarkeit nach festen Regeln – nicht nach Ihrem Kontostand. So funktioniert die Rechnung 2026, und so verbessern Sie Ihre Ausgangslage.',
 'desc':'Tragbarkeit der Hypothek 2026 einfach erklärt: kalkulatorischer Zins, Ein-Drittel-Regel und Eigenkapital. So prüfen Banken Ihr Einkommen – mit Rechenbeispiel von smzh.',
 'kw':'Tragbarkeit','kw2':['Tragbarkeit berechnen','kalkulatorischer Zins','Hypothek Einkommen','Tragbarkeit 2026'],
 'cta':('/de/immobilienbewertung-rechner/','Tragbarkeit berechnen'),
 'cta_h':'Trägt Ihr Einkommen Ihr Wunschobjekt?','cta_p':'Rechnen Sie Tragbarkeit und Eigenkapital für ein konkretes Objekt durch – in wenigen Minuten.',
 'lead':'«<strong>Reicht mein Einkommen für die Bank?</strong>» – das ist die erste Hürde auf dem Weg zum Eigenheim. Banken prüfen die <strong>Tragbarkeit</strong> 2026 nach festen Regeln, die strenger sind, als viele erwarten. Wer sie kennt, kann seine Chancen gezielt verbessern.',
 'body':[
  ('Wie Banken die Tragbarkeit rechnen', p(
    'Massgebend ist nicht, was Sie heute zahlen könnten, sondern ob die Finanzierung auch bei höheren Zinsen tragbar bleibt. Die Bank addiert drei Posten und stellt sie Ihrem Bruttoeinkommen gegenüber:')+ul([
    '<strong>Kalkulatorischer Zins von rund 5 %</strong> auf die Hypothek (nicht der heutige Zins)',
    '<strong>Amortisation</strong>: Rückzahlung auf zwei Drittel des Werts, meist über 15 Jahre',
    '<strong>Nebenkosten/Unterhalt</strong> von rund 1 % des Immobilienwerts pro Jahr',
  ])+p('Liegt die Summe über einem Drittel Ihres Bruttoeinkommens, gilt die Finanzierung als nicht tragbar – auch wenn Sie die heutigen Kosten problemlos stemmen würden.')),
  ('Rechenbeispiel', p(
    'Bei einem Objekt von 800 000 Franken mit 640 000 Franken Hypothek rechnet die Bank grob: 5 % Zins (32 000) + Amortisation (rund 8 000) + 1 % Nebenkosten (8 000) = rund 48 000 Franken pro Jahr. Damit das tragbar ist, sollte das Bruttoeinkommen bei etwa 144 000 Franken liegen.')),
  ('Was Sie an der Tragbarkeit beeinflussen können', p('Sie sind der Faustregel nicht ausgeliefert. Diese Hebel helfen:')+ul([
    'Mehr Eigenkapital einbringen – das senkt die Hypothek und damit die kalkulatorischen Kosten',
    'Zweiteinkommen einbeziehen lassen (sofern die Bank es anrechnet)',
    'Konsumkredite und Leasing vor dem Antrag ablösen',
    'Objektpreis realistisch wählen statt am Limit kaufen',
  ])),
  ('Tragbarkeit, Eigenkapital, Zinswahl – alles hängt zusammen', p(
    'Die Tragbarkeit ist nur ein Teil des Puzzles. Wie viel Eigenkapital nötig ist, zeigt der Ratgeber '+a('/de/ratgeber-eigenkapital-eigenheim/','Wie viel Eigenkapital brauche ich wirklich?')+'. Und ob '+a('/de/ratgeber-saron-oder-festhypothek/','SARON oder Festhypothek')+' passt, beeinflusst Ihre laufenden Kosten zusätzlich. Die Rahmenbedingungen für selbstgenutztes Wohneigentum erläutert die '+ax('https://www.admin.ch','Bundesverwaltung')+'.')),
 ],
 'faq':[
  ('Warum rechnet die Bank mit 5 % Zins?','Der kalkulatorische Zins von rund 5 % ist ein Sicherheitspuffer. Er stellt sicher, dass Sie sich das Eigenheim auch dann leisten können, wenn die Hypothekarzinsen wieder steigen – unabhängig vom heute tiefen Niveau.'),
  ('Welches Einkommen zählt für die Tragbarkeit?','In der Regel das stabile Bruttoeinkommen. Boni oder variable Anteile werden vorsichtig oder gar nicht angerechnet. Ein Zweiteinkommen kann helfen, wenn die Bank es als gesichert betrachtet.'),
  ('Was, wenn die Tragbarkeit knapp nicht reicht?','Oft helfen mehr Eigenkapital, das Ablösen bestehender Kredite oder ein günstigeres Objekt. Eine Beratung zeigt, welcher Hebel in Ihrer Situation am meisten bringt.'),
 ],
 'related':[('Wie viel Eigenkapital brauche ich wirklich?','/de/ratgeber-eigenkapital-eigenheim/'),
            ('Eigenheim kaufen oder warten?','/de/ratgeber-eigenheim-kaufen-oder-warten/'),
            ('SARON oder Festhypothek 2026?','/de/ratgeber-saron-oder-festhypothek/')],
},
{
 'slug':'ratgeber-amortisieren-oder-investieren','img':'/de/artikel/neue-aera-fed/','imgalt':'Hypothek amortisieren oder investieren – Vermögen aufbauen','rubrik':'Vermögen & Anlegen','rubrik_href':'/de/smzhub-vermoegen/',
 'title':'Hypothek amortisieren oder investieren? 2026',
 'h1':'Hypothek amortisieren oder investieren – was lohnt 2026?',
 'h1_short':'Amortisieren oder investieren?',
 'dek':'Schulden tilgen fühlt sich sicher an – ist aber nicht immer die beste Wahl. Wann sich Amortisation lohnt und wann Ihr Kapital anderswo mehr bewirkt.',
 'desc':'Hypothek amortisieren oder investieren 2026? Wie Hypothekarzins, Rendite und Steuern zusammenspielen – mit klarer Entscheidungslogik und Beispiel von smzh.',
 'kw':'Hypothek amortisieren oder investieren','kw2':['Hypothek amortisieren','indirekte Amortisation','Schulden tilgen','investieren 2026'],
 'cta':('/de/finanzplan-erstellen/','Finanzplan erstellen'),
 'cta_h':'Tilgen oder anlegen – was bringt Ihnen mehr?','cta_p':'Ein Finanzplan rechnet Zins, Rendite und Steuern für Ihre Situation gegeneinander.',
 'lead':'<strong>Amortisieren oder investieren</strong>? Soll ich also die Hypothek tilgen oder das Geld anlegen? Diese Frage betrifft 2026 jeden Eigenheimbesitzer mit freiem Kapital. Schulden abbauen fühlt sich gut an – doch ob es sich rechnet, hängt von Zins, Rendite und Steuern ab.',
 'body':[
  ('Amortisieren oder investieren – die Kernlogik', p(
    'Bei der Frage amortisieren oder investieren gilt eine einfache Faustregel: Liegt die erwartete Rendite Ihrer Anlage nach Kosten und Risiko über dem Hypothekarzins, spricht vieles fürs Investieren. Liegt sie darunter – oder ist Ihnen Sicherheit wichtiger – lohnt die Amortisation. Bei den tiefen Zinsen von 2026 ist die Hürde fürs Investieren entsprechend niedrig.')),
  ('Direkte und indirekte Amortisation', p(
    'In der Schweiz unterscheidet man zwei Wege. Bei der <strong>direkten Amortisation</strong> zahlen Sie die Hypothek laufend zurück – die Schuld und die Zinskosten sinken, der steuerbare Eigenmietwert-Effekt aber auch. Bei der <strong>indirekten Amortisation</strong> zahlen Sie in die Säule 3a ein und tilgen erst später; Sie behalten den Schuldzinsabzug und profitieren vom 3a-Steuervorteil.')),
  ('Was für Amortisation spricht', ul([
    'Sie wollen das Risiko reduzieren und schuldenfrei in die Pensionierung',
    'Sie haben keine Disziplin oder keinen Horizont fürs Anlegen',
    'Die Bank verlangt ohnehin die Rückführung auf zwei Drittel des Werts',
  ])),
  ('Was fürs Investieren spricht', ul([
    'Tiefe Hypothekarzinsen 2026 senken die Renditehürde',
    'Schuldzinsen sind steuerlich abziehbar, Anlageerträge teils privilegiert',
    'Langer Anlagehorizont und ausreichend Risikofähigkeit',
  ])+p('Wie Sie 3a-Geld renditestark anlegen, zeigt der Ratgeber '+a('/de/ratgeber-saeule-3a-konto-oder-wertschriften/','Säule 3a: Konto oder Wertschriften?')+'.')),
  ('Steuern nicht vergessen', p(
    'Der Schuldzinsabzug und die Besteuerung des Eigenmietwerts verändern die Rechnung deutlich. Eine reine Zins-gegen-Rendite-Betrachtung greift zu kurz – die Steuerwirkung gehört in jede Entscheidung. Grundlagen liefert die '+ax('https://www.estv.admin.ch','Eidgenössische Steuerverwaltung')+'.')),
 ],
 'faq':[
  ('Ist es bei tiefen Zinsen besser zu investieren?','Tiefe Hypothekarzinsen senken die Renditehürde – Investieren wird attraktiver. Voraussetzung ist aber, dass Sie genug Risikofähigkeit und einen langen Horizont haben. Wer Sicherheit braucht, fährt mit Amortisation besser.'),
  ('Was ist indirekte Amortisation?','Sie tilgen die Hypothek nicht direkt, sondern zahlen in die Säule 3a ein und lösen die Schuld später ab. So behalten Sie den Schuldzinsabzug und nutzen gleichzeitig den Steuervorteil der 3a.'),
  ('Sollte ich vor der Pensionierung schuldenfrei sein?','Nicht zwingend. Eine Restschuld kann steuerlich und finanziell sinnvoll sein. Entscheidend ist, dass die Tragbarkeit auch nach der Pensionierung – mit dann tieferem Einkommen – erfüllt bleibt.'),
 ],
 'related':[('Säule 3a: Konto oder Wertschriften?','/de/ratgeber-saeule-3a-konto-oder-wertschriften/'),
            ('SARON oder Festhypothek 2026?','/de/ratgeber-saron-oder-festhypothek/'),
            ('Wo verschenke ich jedes Jahr Steuern?','/de/ratgeber-steuern-sparen/')],
},
{
 'slug':'ratgeber-frueher-pensionieren','img':'/de/artikel/ahv-2030-pensionierung-planungsfrage/','imgalt':'Früher pensionieren – Frühpensionierung in der Schweiz planen','rubrik':'Vorsorge & Pensionierung','rubrik_href':'/de/smzhub-zukunft/',
 'title':'Früher pensionieren 2026: Was kostet es?',
 'h1':'Früher pensionieren oder weiterarbeiten? Ratgeber 2026',
 'h1_short':'Früher pensionieren?',
 'dek':'Eine Frühpensionierung kostet mehr, als viele denken – ist aber planbar. Welche Stellhebel Sie früh klären sollten, damit der frühere Ausstieg finanzierbar bleibt.',
 'desc':'Früher pensionieren 2026: Was eine Frühpensionierung bei AHV und Pensionskasse kostet, welche Lücken entstehen und wie Sie sie schliessen – Ratgeber von smzh.',
 'kw':'früher pensionieren','kw2':['Frühpensionierung','vorzeitige Pensionierung','AHV Vorbezug','Pensionierung 2026'],
 'cta':('/de/pensionsplanung/','Pensionierung planen'),
 'cta_h':'Ist Ihre Frühpensionierung finanzierbar?','cta_p':'Eine Pensionsplanung zeigt Ihre Einkommenslücke und die Stellhebel, um sie rechtzeitig zu schliessen.',
 'lead':'<strong>Früher pensionieren oder weiterarbeiten?</strong> Der Wunsch nach mehr Freiheit hat 2026 einen konkreten Preis – bei AHV, Pensionskasse und Steuern. Die gute Nachricht: Eine Frühpensionierung ist planbar, wenn Sie die richtigen Hebel früh genug kennen.',
 'body':[
  ('Früher pensionieren – was es kostet', p(
    'Wer früher pensionieren will, spürt es dreifach: Die '+a('/de/ratgeber-rente-oder-kapitalbezug/','Pensionskassenrente')+' fällt tiefer aus, ein AHV-Vorbezug wird lebenslang gekürzt, und es entstehen Beitragslücken. Gleichzeitig müssen die Jahre bis zur ordentlichen Pensionierung überbrückt werden – komplett aus eigenen Mitteln.')),
  ('Die drei grossen Lücken', ul([
    '<strong>AHV:</strong> Ein Vorbezug kürzt die Rente lebenslang; zudem laufen die Beitragsjahre nicht weiter.',
    '<strong>Pensionskasse:</strong> Weniger Beitragsjahre und ein tieferer Umwandlungssatz senken die Rente spürbar.',
    '<strong>Überbrückung:</strong> Vom Ausstieg bis zur ordentlichen Pensionierung brauchen Sie ein eigenes Einkommen.',
  ])),
  ('Welche Stellhebel früh helfen', p('Je früher Sie planen, desto mehr Hebel haben Sie:')+ul([
    '<strong>Pensionskassen-Einkäufe:</strong> erhöhen die Rente und senken die Steuern – über mehrere Jahre gestaffelt',
    '<strong>Säule 3a:</strong> gezielt aufbauen und gestaffelt beziehen',
    '<strong>Teilpensionierung:</strong> schrittweise reduzieren statt abrupt aufhören',
    '<strong>Überbrückungskapital:</strong> frei verfügbares Vermögen für die Jahre bis zur AHV',
  ])),
  ('Teilpensionierung als Mittelweg', p(
    'Statt entweder/oder wählen viele eine Teilpensionierung: Sie reduzieren das Pensum, beziehen einen Teil der Vorsorge und bleiben teilweise erwerbstätig. Das glättet die Einkommenslücke, hält Beiträge am Laufen und kann steuerlich vorteilhaft sein. Grundlagen zur AHV liefert das '+ax('https://www.bsv.admin.ch','Bundesamt für Sozialversicherungen')+'.')),
 ],
 'faq':[
  ('Wie stark wird die AHV bei Vorbezug gekürzt?','Ein AHV-Vorbezug führt zu einer lebenslangen Kürzung der Rente pro vorbezogenem Jahr. Zusätzlich fehlen Beitragsjahre. Die genaue Höhe hängt vom Vorbezugszeitpunkt ab – eine Pensionsplanung rechnet es für Sie durch.'),
  ('Wie viel Kapital brauche ich für eine Frühpensionierung?','Das hängt von Ihren Ausgaben und der Anzahl Überbrückungsjahre ab. Faustregel: Sie müssen die jährliche Einkommenslücke mal die Jahre bis zur ordentlichen Pensionierung aus eigenem Vermögen decken – plus die dauerhaft tiefere Rente.'),
  ('Lohnen sich Pensionskassen-Einkäufe vor der Frühpensionierung?','Oft ja: Einkäufe erhöhen die Rente und sind steuerlich abziehbar. Über mehrere Jahre gestaffelt ist der Steuereffekt am grössten. Vor einem Kapitalbezug gelten allerdings Sperrfristen.'),
 ],
 'related':[('Rente oder Kapital aus der Pensionskasse?','/de/ratgeber-rente-oder-kapitalbezug/'),
            ('Lohnt sich die Säule 3a für mich?','/de/ratgeber-lohnt-sich-saeule-3a/'),
            ('Wo verschenke ich jedes Jahr Steuern?','/de/ratgeber-steuern-sparen/')],
},
{
 'slug':'ratgeber-steuern-sparen','img':'/de/artikel/snb-zinsentscheid-juni/','imgalt':'Steuern sparen in der Schweiz 2026 mit den richtigen Abzügen','rubrik':'Steuern & Finanzplanung','rubrik_href':'/de/smzhub-steuern/',
 'title':'Steuern sparen Schweiz 2026: Die wichtigsten Abzüge',
 'h1':'Steuern sparen 2026: Wo Sie jedes Jahr Geld verschenken',
 'h1_short':'Steuern sparen',
 'dek':'Viele zahlen Jahr für Jahr zu viel Steuern – aus reiner Unkenntnis. Welche Abzüge und Einzahlungen 2026 beim Steuern sparen wirklich einen Unterschied machen.',
 'desc':'Steuern sparen in der Schweiz 2026: Säule 3a, Pensionskassen-Einkauf, Liegenschaftsunterhalt und gestaffelte Bezüge. Die wirksamsten legalen Abzüge – Ratgeber von smzh.',
 'kw':'Steuern sparen','kw2':['Steuerabzüge 2026','Säule 3a Steuern','Pensionskasse Einkauf','Steuern sparen Schweiz'],
 'cta':('/de/budgetrechner/','Budget & Abzüge prüfen'),
 'cta_h':'Welche Abzüge lassen Sie liegen?','cta_p':'Eine Standortbestimmung deckt ungenutzte Abzüge und den optimalen Zeitpunkt für Einzahlungen auf.',
 'lead':'Beim <strong>Steuern sparen</strong> verschenken die meisten jedes Jahr Geld – nicht aus Nachlässigkeit, sondern weil sie die wirksamsten Hebel nicht kennen oder zu spät nutzen. Für das Steuerjahr 2026 lohnt es sich, jetzt zu handeln statt erst beim Ausfüllen der Erklärung.',
 'body':[
  ('Die Säule 3a – der einfachste Hebel', p(
    'Einzahlungen in die <strong>Säule 3a</strong> sind vollständig vom steuerbaren Einkommen abziehbar – bis zum jährlichen Maximalbetrag (für Erwerbstätige mit Pensionskasse rund 7 000 Franken, Stand 2026, jährlich angepasst). Wer früh im Jahr einzahlt, profitiert zusätzlich länger von der Anlage. Wie Sie 3a-Geld renditestark anlegen, zeigt der Ratgeber '+a('/de/ratgeber-saeule-3a-konto-oder-wertschriften/','Konto oder Wertschriften?')+'.')),
  ('Pensionskassen-Einkauf – der grösste Hebel', p(
    'Freiwillige Einkäufe in die Pensionskasse schliessen Beitragslücken, erhöhen die Rente und sind voll abziehbar. Gerade in einkommensstarken Jahren vor der Pensionierung ist der Effekt enorm. Über mehrere Jahre gestaffelt brechen Sie zudem die Steuerprogression. Vor einem Kapitalbezug gelten Sperrfristen.')),
  ('Weitere Abzüge, die oft vergessen gehen', ul([
    '<strong>Liegenschaftsunterhalt:</strong> werterhaltende Renovationen sind abziehbar – Pauschale oder effektive Kosten',
    '<strong>Berufskosten:</strong> Arbeitsweg, auswärtige Verpflegung, Weiterbildung',
    '<strong>Kinder- und Betreuungskosten:</strong> kantonal unterschiedlich, oft unterschätzt',
    '<strong>Krankheits- und Spendenabzüge</strong> ab gewissen Schwellen',
  ])),
  ('Steuern sparen ist auch eine Frage des Timings', p(
    'Steuern sparen heisst nicht nur, Abzüge zu kennen, sondern sie im richtigen Jahr zu nutzen. Wer grössere Renovationen oder Pensionskassen-Einkäufe auf mehrere Jahre verteilt, senkt die Progression stärker, als wenn alles in einem Jahr anfällt. Beim '+a('/de/ratgeber-rente-oder-kapitalbezug/','Kapitalbezug der Pensionskasse')+' lohnt sich aus demselben Grund eine gestaffelte Auszahlung. Kantonale Unterschiede sind gross – die '+ax('https://www.estv.admin.ch','Eidgenössische Steuerverwaltung')+' bietet eine Übersicht.')),
 ],
 'faq':[
  ('Wie viel Steuern spare ich mit der Säule 3a?','Die Ersparnis entspricht Ihrem Grenzsteuersatz auf den einbezahlten Betrag. Bei einem Grenzsteuersatz von 30 % und einer Maximaleinzahlung sparen Sie also rund ein Drittel davon an Steuern – Jahr für Jahr.'),
  ('Lohnt sich ein Pensionskassen-Einkauf steuerlich?','Meist ja, besonders in einkommensstarken Jahren. Der Einkauf ist voll abziehbar und erhöht die Rente. Über mehrere Jahre gestaffelt ist der Effekt am grössten. Beachten Sie die Sperrfrist vor einem Kapitalbezug.'),
  ('Was ist der wirksamste Steuerabzug?','Für die meisten ist es die Kombination aus Säule 3a und – vor der Pensionierung – gestaffelten Pensionskassen-Einkäufen. Welcher Hebel bei Ihnen am meisten bringt, hängt von Einkommen, Wohnkanton und Lebensphase ab.'),
 ],
 'related':[('Säule 3a: Konto oder Wertschriften?','/de/ratgeber-saeule-3a-konto-oder-wertschriften/'),
            ('Lohnt sich die Säule 3a für mich?','/de/ratgeber-lohnt-sich-saeule-3a/'),
            ('Rente oder Kapital aus der Pensionskasse?','/de/ratgeber-rente-oder-kapitalbezug/')],
},
{
 'slug':'ratgeber-eigenkapital-eigenheim','img':'/de/artikel/zuercher-wohnungsinitiativen/','imgalt':'Eigenkapital fürs Eigenheim 2026 – wie viel wirklich nötig ist','rubrik':'Eigenheim & Hypothek','rubrik_href':'/de/smzhub-eigenheim/',
 'title':'Eigenkapital fürs Eigenheim 2026: Wie viel wirklich?',
 'h1':'Eigenkapital fürs Eigenheim 2026: Wie viel brauchen Sie?',
 'h1_short':'Wie viel Eigenkapital?',
 'dek':'20 Prozent sind nur die halbe Wahrheit. Welche Mittel als Eigenkapital zählen, was «hartes» Eigenkapital bedeutet und worauf es 2026 zusätzlich ankommt.',
 'desc':'Wie viel Eigenkapital fürs Eigenheim 2026? Die 20-Prozent-Regel, hartes Eigenkapital, Pensionskasse und Säule 3a verständlich erklärt – mit Beispiel von smzh.',
 'kw':'Eigenkapital fürs Eigenheim','kw2':['Eigenkapital Hypothek','20 Prozent Eigenkapital','hartes Eigenkapital','Eigenheim 2026'],
 'cta':('/de/immobilienbewertung-rechner/','Eigenkapital & Tragbarkeit prüfen'),
 'cta_h':'Haben Sie genug Eigenkapital?','cta_p':'Prüfen Sie für ein konkretes Objekt, wie viel Eigenkapital nötig ist – und woher es kommen darf.',
 'lead':'Wie viel <strong>Eigenkapital fürs Eigenheim</strong> brauchen Sie 2026 wirklich? «20 Prozent» kennt jeder – doch das ist nur die halbe Wahrheit. Entscheidend ist, <strong>welche</strong> Mittel zählen und wie viel davon «hart» sein muss. Wer das versteht, plant den Kauf realistischer.',
 'body':[
  ('Die 20-Prozent-Regel richtig verstanden', p(
    'Banken finanzieren in der Regel maximal 80 % des Immobilienwerts. Die restlichen <strong>20 % Eigenkapital</strong> bringen Sie selbst ein. Bei einem Kaufpreis von 800 000 Franken sind das 160 000 Franken. Doch nicht jedes Eigenkapital ist gleichwertig.')),
  ('Hartes Eigenkapital – die entscheidende Hälfte', p(
    'Mindestens die Hälfte des Eigenkapitals – also 10 % des Kaufpreises – muss <strong>«hartes» Eigenkapital</strong> sein: Ersparnisse, Wertschriften, Schenkungen oder Erbvorbezüge. Diese 10 % dürfen <em>nicht</em> aus der Pensionskasse stammen. Die übrigen 10 % können Sie aus der 2. Säule oder der Säule 3a beziehen.')),
  ('Woher das Eigenkapital fürs Eigenheim kommen darf',
    '<table class="art-table"><thead><tr><th>Quelle</th><th>Zählt als</th><th>Hinweis</th></tr></thead><tbody>'
    '<tr><td>Erspartes, Wertschriften</td><td>hartes EK</td><td>jederzeit einsetzbar</td></tr>'
    '<tr><td>Schenkung / Erbvorbezug</td><td>hartes EK</td><td>oft unterschätzt</td></tr>'
    '<tr><td>Säule 3a</td><td>hartes EK möglich</td><td>Bezug oder Verpfändung</td></tr>'
    '<tr><td>Pensionskasse (2. Säule)</td><td>nur «weiche» 10 %</td><td>senkt spätere Rente</td></tr>'
    '</tbody></table>'),
  ('Vorsicht beim Pensionskassen-Bezug', p(
    'Geld aus der Pensionskasse fürs Eigenheim zu beziehen, klingt verlockend – schmälert aber Ihre spätere Rente und kann Vorsorgelücken reissen. Prüfen Sie Alternativen wie die Verpfändung. Wie sich Bezug und Rente langfristig auswirken, zeigt der Ratgeber '+a('/de/ratgeber-rente-oder-kapitalbezug/','Rente oder Kapital')+'.')),
  ('Mehr Eigenkapital senkt die Folgekosten', p(
    'Je mehr Eigenkapital Sie einbringen, desto tiefer ist die Hypothek – und damit die '+a('/de/ratgeber-tragbarkeit-hypothek/','Tragbarkeit')+'. Das verbessert Ihre Chancen bei der Bank und senkt die laufenden Kosten. Eigenkapital aufzubauen ist deshalb selten verschenkte Zeit.')),
 ],
 'faq':[
  ('Wie viel Eigenkapital brauche ich mindestens?','Mindestens 20 % des Kaufpreises. Davon müssen mindestens 10 % «hartes» Eigenkapital sein, das nicht aus der Pensionskasse stammt. Die übrigen 10 % dürfen Sie aus der 2. Säule oder der Säule 3a beziehen.'),
  ('Zählt Geld aus der Pensionskasse als Eigenkapital?','Ja, aber nur als «weicher» Teil – maximal 10 % des Kaufpreises. Ein Bezug senkt allerdings Ihre spätere Rente. Häufig ist die Verpfändung die bessere Alternative.'),
  ('Kann ich eine Schenkung als Eigenkapital nutzen?','Ja. Schenkungen und Erbvorbezüge zählen als hartes Eigenkapital und sind ein wichtiger, oft unterschätzter Baustein der Finanzierung.'),
 ],
 'related':[('Reicht mein Einkommen für die Bank?','/de/ratgeber-tragbarkeit-hypothek/'),
            ('Eigenheim kaufen oder warten?','/de/ratgeber-eigenheim-kaufen-oder-warten/'),
            ('SARON oder Festhypothek 2026?','/de/ratgeber-saron-oder-festhypothek/')],
},
{
 'slug':'ratgeber-lohnt-sich-saeule-3a','img':'/de/artikel/ahv-2030-pensionierung-planungsfrage/','imgalt':'Lohnt sich die Säule 3a 2026 für die Vorsorge','rubrik':'Vorsorge & Pensionierung','rubrik_href':'/de/smzhub-zukunft/',
 'title':'Lohnt sich die Säule 3a 2026? Der Ratgeber',
 'h1':'Lohnt sich die Säule 3a für mich? Ratgeber 2026',
 'h1_short':'Lohnt sich die Säule 3a?',
 'dek':'Die Säule 3a gilt als Pflicht – ist sie aber nicht für jeden gleich sinnvoll. Wann sich 3a 2026 wirklich lohnt und wann Ihr Geld anderswo besser aufgehoben ist.',
 'desc':'Lohnt sich die Säule 3a 2026? Steuervorteil, Renditechance, Bindung und für wen 3a wirklich sinnvoll ist – mit ehrlicher Entscheidungshilfe von smzh.',
 'kw':'lohnt sich die Säule 3a','kw2':['Säule 3a sinnvoll','Säule 3a Vorteile','Säule 3a Steuern','Säule 3a 2026'],
 'cta':('/de/vorsorgeanalyse/','Vorsorge analysieren'),
 'cta_h':'Ist die Säule 3a für Sie der beste Sparort?','cta_p':'Eine Vorsorgeanalyse zeigt, ob 3a, Pensionskassen-Einkauf oder freies Sparen für Sie mehr bringt.',
 'lead':'«Mach die <strong>Säule 3a</strong>, das lohnt sich immer» – diesen Rat hört man oft. Doch <strong>lohnt sich die Säule 3a</strong> 2026 wirklich für jeden? Sie hat starke Vorteile, aber auch eine entscheidende Einschränkung. Dieser Ratgeber hilft Ihnen, ehrlich zu entscheiden.',
 'body':[
  ('Die zwei grossen Vorteile', p(
    'Die Säule 3a punktet 2026 vor allem doppelt: Einzahlungen sind '+a('/de/ratgeber-steuern-sparen/','steuerlich abziehbar')+', und das Guthaben wächst – richtig angelegt – über Jahrzehnte mit dem Zinseszins. Der Steuervorteil entspricht Ihrem Grenzsteuersatz: Bei 30 % sparen Sie auf jeden einbezahlten Franken rund 30 Rappen.')),
  ('Der entscheidende Haken: die Bindung', p(
    'Das Geld in der Säule 3a ist <strong>gebunden</strong>. Sie kommen in der Regel erst frühestens fünf Jahre vor dem ordentlichen Rentenalter daran – Ausnahmen sind Eigenheim, Selbstständigkeit oder Wegzug. Wer kurzfristig Liquidität braucht, ist mit freiem Sparen flexibler.')),
  ('Lohnt sich die Säule 3a für Sie? Diese Punkte sprechen dafür', ul([
    'Erwerbstätige mit steuerbarem Einkommen – der Abzug wirkt sofort',
    'Langer Anlagehorizont bis zur Pensionierung',
    'Wer ohnehin fürs Alter spart und das Geld nicht kurzfristig braucht',
    'Wer den Bezug später '+a('/de/ratgeber-rente-oder-kapitalbezug/','gestaffelt')+' plant, um Steuern zu sparen',
  ])),
  ('Wann anderes sinnvoller sein kann', ul([
    'Sehr tiefes oder kein steuerbares Einkommen – der Steuervorteil verpufft',
    'Sie brauchen das Geld absehbar (Liquiditätsreserve fehlt)',
    'Hochverzinste Schulden oder Konsumkredite – diese zuerst tilgen',
  ])+p('Ob Sie Schulden zuerst abbauen oder anlegen sollten, klärt der Ratgeber '+a('/de/ratgeber-amortisieren-oder-investieren/','Amortisieren oder investieren?')+'.')),
  ('Wenn 3a, dann richtig', p(
    'Wer sich für die Säule 3a entscheidet, sollte zwei Dinge beachten: die '+a('/de/ratgeber-saeule-3a-konto-oder-wertschriften/','Anlageform')+' (Konto vs. Wertschriften) und mehrere gestaffelte Konten für einen steuergünstigen Bezug. Beides zusammen entscheidet über das Endresultat. Grundlagen zur 3. Säule liefert das '+ax('https://www.bsv.admin.ch','Bundesamt für Sozialversicherungen')+'.')),
 ],
 'faq':[
  ('Lohnt sich die Säule 3a ohne hohes Einkommen?','Der Hauptvorteil ist der Steuerabzug – er wirkt nur, wenn Sie steuerbares Einkommen haben. Bei sehr tiefem Einkommen ist der Effekt gering; dann kann flexibles Sparen sinnvoller sein. Die Renditechance bei langem Horizont bleibt aber bestehen.'),
  ('Wann komme ich an das Geld der Säule 3a?','In der Regel frühestens fünf Jahre vor dem ordentlichen Rentenalter. Vorzeitig nur für Wohneigentum, Selbstständigkeit, definitiven Wegzug aus der Schweiz oder den Einkauf in die Pensionskasse.'),
  ('Konto oder Wertschriften für die Säule 3a?','Bei langem Horizont bringt ein Wertschriftendepot meist deutlich mehr als das Zinskonto. Je näher der Bezug, desto defensiver sollte die Strategie sein. Mehr dazu im Ratgeber «Säule 3a: Konto oder Wertschriften?».'),
 ],
 'related':[('Säule 3a: Konto oder Wertschriften?','/de/ratgeber-saeule-3a-konto-oder-wertschriften/'),
            ('Wo verschenke ich jedes Jahr Steuern?','/de/ratgeber-steuern-sparen/'),
            ('Rente oder Kapital aus der Pensionskasse?','/de/ratgeber-rente-oder-kapitalbezug/')],
},
]

# ---------------------------------------------------------------------------
SLUG_RUBRIK = {a['slug']: a['rubrik'] for a in ARTICLES}
ASSET_DIR = os.path.join('site','smzh.ch','de','_assets','ratgeber')
SRC_LABEL = {'unsplash':'Unsplash','pexels':'Pexels'}
try:
    CREDITS = json.load(open(os.path.join(ASSET_DIR,'credits.json'),encoding='utf-8'))
except Exception:
    CREDITS = {}

def reading_time(html_text):
    words=len(re.findall(r"[A-Za-zÄÖÜäöü']+", re.sub(r'<[^>]+>',' ',html_text)))
    return max(3, round(words/200)), words

def cta_block(art, mid):
    href,label=art['cta']
    h = 'Wie sieht das in Ihrer Situation aus?' if mid else art['cta_h']
    txt = 'Eine unverbindliche Einschätzung zeigt, was für Sie konkret zählt – ohne Verpflichtung.' if mid else art['cta_p']
    eyebrow = 'Persönliche Einschätzung' if mid else 'Kostenlos & unverbindlich'
    return (f'<div class="art-cta"><p class="art-cta-eyebrow">{esc(eyebrow)}</p>'
            f'<h3>{esc(h)}</h3><p>{esc(txt)}</p>'
            f'<div class="art-cta-row">'
            f'<a class="art-cta-btn art-cta-btn1" href="{link(href)}">{esc(label)}<span class="ar">→</span></a>'
            f'<a class="art-cta-btn art-cta-btn2" href="{link(BOOK)}">Beratung vereinbaren<span class="ar">→</span></a></div>'
            f'<div class="art-cta-trust"><span>Unverbindlich</span><span>In wenigen Minuten</span><span>Persönlich beraten</span></div>'
            f'</div>')

def article_inner(art, mins):
    secs=[f'<h2>{esc(h2)}</h2>{body}' for h2,body in art['body']]
    # CTA nach dem 2. Abschnitt einschieben
    mid=cta_block(art,True)
    body_secs = secs[:2] + [mid] + secs[2:]
    faq=''.join(f'<p class="art-faq-q">{esc(q)}</p><p class="art-faq-a">{esc(ans)}</p>' for q,ans in art['faq'])
    rel_cards=''
    for t,pth in art['related']:
        rslug=pth.strip('/').split('/')[-1]
        kick=SLUG_RUBRIK.get(rslug,'Ratgeber')
        rel_cards+=(f'<a class="art-rel-card" href="{link(pth)}">'
                    f'<span class="art-rel-k">{esc(kick)}</span>'
                    f'<span class="art-rel-t">{esc(t)}</span>'
                    f'<span class="art-rel-go">Weiterlesen <span class="ar">→</span></span></a>')
    bc=(f'<div class="art-bc"><a href="{link("/de/smzhub/")}">smzhHub</a> › '
        f'<a href="{link(art["rubrik_href"])}">{esc(art["rubrik"])}</a> › {esc(art["h1_short"])}</div>')
    fig=''
    slug=art['slug']
    if os.path.exists(os.path.join(ASSET_DIR,slug+'.jpg')):
        cr=CREDITS.get(slug,{})
        cap=esc(art['imgalt'])
        ph=(cr.get('photographer') or '').strip()
        lbl=SRC_LABEL.get(cr.get('source'),'')
        if ph and 'contributor' not in ph.lower():
            cap+=' · Foto: '+esc(ph)+(f' / {lbl}' if lbl else '')
        elif lbl:
            cap+=' · Foto: '+lbl
        src=V.P_+'de/_assets/ratgeber/'+slug+'.jpg'
        fig=(f'<figure class="art-fig"><div class="art-figw">'
             f'<span class="art-fig-tag">{esc(art["rubrik"])}</span>'
             f'<img src="{src}" alt="{esc(art["imgalt"])}" width="1600" height="900" loading="lazy"></div>'
             f'<figcaption>{cap}</figcaption></figure>')
    return ('<div class="v5">'
            '<section class="v5-phead"><div class="v5-phead-in">'
            f'<p class="v5-eyebrow">{esc(art["rubrik"])} · Stand 2026 · {mins} Min</p>'
            f'<h1>{esc(art["h1"])}</h1><p>{esc(art["dek"])}</p></div></section>'
            '<div class="v5-wrap">'
            f'{bc}'
            '<article class="art-body">'
            f'<p class="art-lead">{art["lead"]}</p>'
            f'{fig}'
            f'{"".join(body_secs)}'
            f'<div class="art-faq"><h2>Häufige Fragen</h2>{faq}</div>'
            f'{cta_block(art,False)}'
            f'<div class="art-related"><p class="art-related-eyebrow">Weiterlesen</p>'
            f'<h2>Passend zu Ihrer Entscheidung</h2>'
            f'<div class="art-rel-grid">{rel_cards}</div></div>'
            f'<p style="margin-top:1.4rem"><a class="v5-back" href="{link("/de/smzhub/")}">← Zurück zum smzhHub</a></p>'
            '</article></div></div>')

def jsonld_for(art, url, mins, img_url=None):
    bc={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[
        {'@type':'ListItem','position':1,'name':'smzhHub','item':BASE+'/de/smzhub/'},
        {'@type':'ListItem','position':2,'name':art['rubrik'],'item':BASE+link(art['rubrik_href']).replace('../../','/').replace('/index.html','/')},
        {'@type':'ListItem','position':3,'name':art['h1_short'],'item':url},
    ]}
    article={'@context':'https://schema.org','@type':'Article','headline':art['h1'],
        'description':art['desc'],'inLanguage':'de-CH','author':ORG,'publisher':ORG,
        'mainEntityOfPage':url,'datePublished':'2026-01-15','dateModified':'2026-06-23',
        'keywords':', '.join([art['kw']]+art['kw2'])}
    if img_url: article['image']=img_url
    faq={'@context':'https://schema.org','@type':'FAQPage','mainEntity':[
        {'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a_}} for q,a_ in art['faq']]}
    return [bc,article,faq]

def build_all():
    for art in ARTICLES:
        inner_tmp=article_inner(art,6)
        mins,_=reading_time(inner_tmp)
        inner=article_inner(art,mins)
        url=BASE+'/de/'+art['slug']+'/'
        img_url=BASE+'/de/_assets/ratgeber/'+art['slug']+'.jpg' if os.path.exists(os.path.join(ASSET_DIR,art['slug']+'.jpg')) else None
        meta={'desc':art['desc'],'jsonld':jsonld_for(art,url,mins,img_url)}
        if img_url: meta['image']=img_url
        V.build_page(('de',art['slug']),inner,art['title'],meta)
    print(f'OK Ratgeber: {len(ARTICLES)} Lead-Gen-/SEO-Artikel geschrieben.')

if __name__=='__main__':
    build_all()
