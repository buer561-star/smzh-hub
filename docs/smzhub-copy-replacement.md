# smzhHub Landing Page – Copy-Replacement-Tabelle

Konsumentenorientierte Überarbeitung aller sichtbaren Texte der smzhHub-Landingpage.
Schweizer Rechtschreibung (ss statt ß). Kein Redesign, keine Strukturänderung –
nur Wording. Quelle: `build/build_hub_v5.py` (generiert
`site/smzh.ch/de/smzhub/index.html`); die Schluss-CTA liegt im Seiten-Chrome und
wird beim Build seitenscharf ersetzt.

Hinweis: `research()` und `flag_card()` sind im Generator definiert, werden aber
in `home_inner()` **nicht** gerendert – ihre Texte sind nicht sichtbar und daher
nicht Teil dieser Tabelle.

---

## 1 Hero

| Ort | Bisher | Problem | Neu | Grund |
|---|---|---|---|---|
| Hero H1 | „Klarheit für Ihre nächste Finanzentscheidung." | – | unverändert | Sagt direkt, was der Hub leistet; entspricht der empfohlenen Richtung. Bewusst beibehalten. |
| Hero Subline | „Einordnungen, Research und Ratgeber zu Eigenheim, Vermögen, Vorsorge und Steuern – kuratiert nach Ihren Fragen." | „kuratiert nach Ihren Fragen" ist abstrakt und portalhaft; sagt nicht, was der Nutzen ist. | „smzhHub ordnet Märkte, Eigenheim, Vorsorge und Steuern so ein, dass Sie Ihre nächste Entscheidung sicherer treffen." | Benennt den konkreten Nutzen (bessere Entscheidung) statt nur die Inhaltsgattung. |

## 2 Entscheidungs-Karussell

| Ort | Bisher | Problem | Neu | Grund |
|---|---|---|---|---|
| Sektion H2 | „Entscheiden statt nur informieren" | – | unverändert | Klar, advisory, auf den Punkt. |
| Sektion Subline | „Wichtige Finanzfragen sollten nicht unter Unsicherheit entschieden werden." | „unter Unsicherheit" ist vage und leicht dramatisierend. | „Wichtige Finanzfragen sollten nicht ohne Einordnung entschieden werden." | Verschiebt von Angst (Unsicherheit) zu Leistungsversprechen (Einordnung) – passt zur Thought-Leadership-Rolle. |
| Karte 2 Teaser | „Wie Preisentwicklung, Eigenkapital und Lebensplanung zusammenhängen." | „Lebensplanung" ist weich/abstrakt. | „Wie Preisentwicklung, Eigenkapital und Tragbarkeit zusammenspielen." | „Tragbarkeit" ist die konkrete, entscheidungsrelevante Grösse. |
| Karte 3 Teaser | „Die Pensionierungsentscheidung, die selten sauber vorbereitet wird." | Beschreibt das Problem, nicht den Inhalt; leicht belehrend. | „Eine Entscheidung, die Steuern, Sicherheit und Flexibilität gleichzeitig betrifft." | Benennt die drei realen Dimensionen – nützlicher und neutraler. |
| Karte 4 Teaser | „Warum Sparen allein über lange Zeiträume oft nicht genügt." | Etwas generisch/mahnend. | „Warum die Wahl der Anlageform über Jahrzehnte mehr bewirkt als die Einzahlung allein." | Konkrete These mit Zeithorizont – Thought Leadership statt Mahnung. |
| Karte 6 Teaser | „Hypothek tilgen oder das Geld anlegen – was sich für Sie langfristig mehr lohnt." | Wiederholt nur die Frage. | „Wann Schuldenabbau sinnvoll ist – und wann Ihr Kapital mehr bewirkt." | Liefert das Entscheidungskriterium statt die Frage zu spiegeln. |
| Karte 8 Teaser | „Welche Abzüge und Vorsorgebezüge wirklich einen Unterschied machen." | „Vorsorgebezüge" (Bezug = Auszahlung) ist sachlich falsch im Abzugskontext. | „Welche Abzüge und Einzahlungen wirklich einen Unterschied machen." | Fachlich korrekt: abzugsfähig sind Einzahlungen, nicht Bezüge. |

(Karten 1, 5, 7, 9, 10 sind bereits konkret und konsumentennah – bewusst unverändert.)

## 3 Saisonaler Fokus

| Ort | Bisher | Problem | Neu | Grund |
|---|---|---|---|---|
| Eyebrow/Tag | „Saisonthema" | Wirkt redaktionell-intern und etwas beliebig. | „Aktuell relevant" | Signalisiert Relevanz statt Kalenderlogik. |
| Saison H | „Krankenkasse 2027: jetzt vergleichen statt automatisch zahlen" | „jetzt … statt automatisch zahlen" klingt salesy. | „Krankenkasse 2027: prüfen, bevor die Police automatisch weiterläuft" | Behält die Dringlichkeit, aber ruhig/advisory statt werblich. |
| Saison Teaser | „Prämien steigen erneut – wer Grundversicherung, Franchise und Modell prüft, spart oft mehrere Hundert Franken pro Jahr." | „spart oft mehrere Hundert Franken" ist ein vages Sparversprechen. | „Prämie, Franchise und Modellwahl wirken jedes Jahr direkt auf Ihr Budget. Der richtige Moment zu prüfen ist, bevor die neue Police automatisch weiterläuft." | Benennt die konkreten Stellhebel und den richtigen Zeitpunkt statt eine Sparzahl zu versprechen. |
| Sub 3 | „Budgetrechner nutzen" | Tool-zentriert, kein Nutzen. | „Budget für 2027 durchrechnen" | Konkreter Anlass und Ergebnis. |

## 4 Rubriken

| Ort | Bisher | Problem | Neu | Grund |
|---|---|---|---|---|
| Rubrik 1 Titel | „Eigenheim & Hypothek" | – | unverändert | Passt ins Layout, konsumentenklar. |
| Rubrik 1 Beschreibung | (keine) | Rubrik hatte keine Einordnung. | „Für alle, die kaufen, verlängern oder ihre Finanzierung neu ausrichten wollen." | Adressiert konkrete Nutzersituationen statt Themenetikett. |
| Rubrik 2 Titel | „Vermögen & Anlegen" | – | unverändert | Passt. |
| Rubrik 2 Beschreibung | (keine) | – | „Märkte, Zinsen und Portfolios verständlich eingeordnet – ohne tägliches Börsenrauschen." | Grenzt vom Newsfeed-Rauschen ab (Thought Leadership). |
| Rubrik 3 Titel | „Vorsorge & Pensionierung" | – | unverändert | Passt. |
| Rubrik 3 Beschreibung | (keine) | – | „AHV, BVG, 3a und Pensionierung als Lebensplanung – nicht als Produktliste." | Positioniert beratend statt produktverkäuferisch. |

### Tool-/Rechner-CTAs in den Rubriken

| Ort | Bisher | Problem | Neu | Grund |
|---|---|---|---|---|
| Eigenheim-Tool Button | „Jetzt prüfen" | Generisch. | „Tragbarkeit berechnen" | Kontextbezogen und ergebnisklar. |
| Vermögen-Tool Button | „Check starten" | Generisch. | „Anlagestrategie einordnen" | Beschreibt das konkrete Ergebnis. |
| Vorsorge-Tool Button | „Analyse starten" | Generisch. | „Vorsorge analysieren" | Konkreter Gegenstand der Analyse. |

## 5 Schluss-CTA (360°-Band im Chrome – seitenscharf ersetzt)

| Ort | Bisher | Problem | Neu | Grund |
|---|---|---|---|---|
| CTA H3 | „Nutzen Sie unseren 360° Check-Up" | Produkt-/Toolname statt Nutzen; portalhaft. | „Wissen ist der Einstieg. Entscheidend ist, was es für Ihre Situation bedeutet." | Übersetzt Inhalt in Handlung – ruhig, advisory, lead-relevant. |
| CTA Subline | „Unser 360° Check-Up ist eine Analyse Ihrer aktuellen Ausgangslage. Mit ihr finden wir heraus, wie Ihre individuelle Situation optimiert werden könnte." | „individuelle Situation optimiert" ist Marketingfloskel. | „smzh hilft, Marktinformationen, Vorsorge, Eigenheim, Steuern und Vermögen in eine konkrete Finanzentscheidung zu übersetzen." | Konkretes Leistungsversprechen statt Floskel. |
| CTA Button | „Unverbindlichen Termin vereinbaren" | Generischer Termin-Call. | „Nächsten Schritt klären" | Niederschwellig, beratend, nicht salesy (Link/Routing unverändert). |

---

## Bewusst nicht geändert

- **Hero-H1, Sektions-H2 des Karussells, Saison-CTA „Prämien vergleichen"**:
  bereits klar, konkret und konsumentennah.
- **Karten 1, 5, 7, 9, 10** des Entscheidungs-Karussells: Titel und Teaser sind
  bereits konkrete Nutzerfragen mit Implikation.
- **Navigation, Footer-Links, Filialhinweis, rechtliche Texte**: gehören zum
  globalen smzh-Chrome und sind nicht Teil der Hub-Redaktion.
- **`research()` / `flag_card()`**: im Generator vorhanden, aber nicht gerendert –
  nicht sichtbar.
- **Routing/Links aller CTAs**: unverändert (nur Beschriftung).
