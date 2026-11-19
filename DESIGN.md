---
name: ai-on-rails
description: Handbuch mit Registern. Papiergrund, ein Register pro Leistung in voller Farbe, Inhalt auf hellen Blättern.
colors:
  paper: "#f3efe4"
  leaf: "rgba(255, 255, 253, .95)"
  ink: "#1b1b1d"
  ink-2: "#4b4a47"
  rule: "#d8d2c3"
  start: "#6e685c"
  ship: "#c4471a"
  ship-ink: "#a83a12"
  get: "#1d6f55"
  stay: "#2a3d9a"
  dark: "#1b1b1d"
  errata: "#9a3412"
  selection: "#f6d7c6"
  dark-leaf: "#26262a"
  dark-line: "#3a3a40"
  dark-text: "#f1efe9"
  dark-lead: "#c9c6bd"
  dark-ghost-line: "#6b6b72"
  white: "#ffffff"
typography:
  display:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "clamp(2rem, 4vw, 3rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.015em"
  headline:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "clamp(1.9rem, 3.8vw, 2.8rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.015em"
  title:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "clamp(1.4rem, 2.6vw, 1.9rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.015em"
  register-name:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "1.6rem"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.015em"
  subtitle:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "1.12rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.015em"
  body:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.62
  lead:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "1.08rem"
    fontWeight: 400
    lineHeight: 1.62
  lead-start:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "1.15rem"
    fontWeight: 400
    lineHeight: 1.62
  label:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "0.8rem"
    fontWeight: 600
    letterSpacing: "0.04em"
  ui:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 600
  wordmark:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 700
    letterSpacing: "0.08em"
  measure:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: "0.8rem"
    fontWeight: 500
  measure-amount:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: "1.1rem"
    fontWeight: 500
rounded:
  none: "0px"
spacing:
  row-gap: "10px"
  cell: "14px"
  leaf-stack: "18px"
  grid-gap: "28px"
  start-gap: "40px"
  register-y: "56px"
  plain-y: "64px"
  rail: "64px"
  leaf-pad: "clamp(22px, 3.5vw, 40px)"
  gutter: "clamp(16px, 4vw, 48px)"
  container: "1120px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
    typography: "{typography.ui}"
    rounded: "{rounded.none}"
    padding: "12px 20px"
  button-primary-hover:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
  button-ship:
    backgroundColor: "{colors.ship}"
    textColor: "{colors.white}"
    typography: "{typography.ui}"
    rounded: "{rounded.none}"
    padding: "12px 20px"
  button-ship-hover:
    backgroundColor: "transparent"
    textColor: "{colors.ship-ink}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.ui}"
    rounded: "{rounded.none}"
    padding: "12px 20px"
  button-ghost-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
  button-sm:
    padding: "7px 14px"
  button-on-dark:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "12px 20px"
  tab-ship:
    backgroundColor: "{colors.ship}"
    textColor: "{colors.white}"
    typography: "{typography.label}"
    width: "{spacing.rail}"
  tab-get:
    backgroundColor: "{colors.get}"
    textColor: "{colors.white}"
    width: "{spacing.rail}"
  tab-stay:
    backgroundColor: "{colors.stay}"
    textColor: "{colors.white}"
    width: "{spacing.rail}"
  tab-start:
    backgroundColor: "{colors.start}"
    textColor: "{colors.white}"
    width: "{spacing.rail}"
  tab-kontakt:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.white}"
    width: "{spacing.rail}"
  register-ship:
    backgroundColor: "{colors.ship}"
    textColor: "{colors.white}"
    padding: "56px 0"
  register-get:
    backgroundColor: "{colors.get}"
    textColor: "{colors.white}"
    padding: "56px 0"
  register-stay:
    backgroundColor: "{colors.stay}"
    textColor: "{colors.white}"
    padding: "56px 0"
  register-dark:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.dark-text}"
    padding: "56px 0"
  leaf:
    backgroundColor: "{colors.leaf}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.leaf-pad}"
  leaf-dark:
    backgroundColor: "{colors.dark-leaf}"
    textColor: "{colors.dark-text}"
    rounded: "{rounded.none}"
    padding: "{spacing.leaf-pad}"
  errata-open:
    textColor: "{colors.errata}"
    typography: "{typography.measure}"
    rounded: "{rounded.none}"
    padding: "0 5px"
---

# Design System: ai-on-rails

## Overview

**Creative North Star: "Das Handbuch mit Registern"**

Die Website ist ein gebundenes Handbuch. Jede Leistung ist ein Register aus Karton in voller Farbe (Ship Fast Oxidorange, Get Fast Grün, Stay Fast Ultramarin, Kontakt Tinte), und der Inhalt liegt auf fast weißen Blättern, die auf diesem Karton aufliegen. Rechts sitzt über die volle Höhe eine feste Registerleiste; der Reiter des Registers, das gerade im Blick ist, ist ausgezogen. Die Welt stammt aus dem Katalog-Challenger rw-manual-acetate-tab-board und wurde vom Nutzer auf Platz 1 gesetzt.

Die Haltung ist die eines technischen Handbuchs, nicht einer Agenturseite: dieselben Felder in jedem Register, Maße und Dauern in Monospace, Linien wie in einer Tabelle, offene Angaben als sichtbarer Errata-Zettel statt als geglätteter Platzhalter. Dichte ist mittel: lesbare Blätter mit begrenzter Zeilenlänge, aber keine Luftflächen ohne Inhalt. Die Seite verweigert die Agentur-Vorlage aus Hero-Bild, drei gleichen Karten und Logoleiste.

Bewegung hat genau eine Grammatik: zwei harte Stufen in 90 ms (`steps(2)`), ohne Easing. Der Reiter springt heraus, der Button kippt um, das Plus der FAQ klappt. Nichts gleitet, nichts federt.

**Key Characteristics:**
- Papiergrund, Register in voller Farbe, Inhalt immer auf einem hellen Blatt
- Feste Registerleiste rechts (64px), Reiterhöhe nach Umfang der Leistung
- Drei Schriftstimmen: Serif zum Lesen, Grotesk zum Navigieren, Mono zum Messen
- Steckbrief mit denselben vier Feldern in jedem Register
- Offene Angaben als gestrichelter Errata-Zettel in Rostrot
- Rechte Winkel überall, Schatten nur unter Blättern
- Bewegung in zwei Stufen, 90 ms, kein Easing

## Colors

Warmer Papiergrund und Tinte als Basis, drei kräftige, gedeckte Registerfarben als Leistungs-Codes, ein Rostrot nur für offene Angaben.

### Primary
- **Ship Oxidorange** (`ship`): Register Ship Fast / Product Bets, ihr Reiter, ihre Farbmarke im Inhaltsverzeichnis und der einzige farbige Button (`button-ship`). Weil die Product Bet führt, ist Orange auch die Farbe des Haupt-Aufrufs "Gespräch vereinbaren" im Startblock und auf der Bet-Seite.
- **Ship-Tinte** (`ship-ink`): dunklere Stufe für orangefarbenen Text auf hellem Grund (Wochenangaben im Ablauf, Listenmarker, Hover-Text des Ship-Buttons, "AI" in der Wortmarke). Text in Registerfarbe auf Papier oder Blatt nimmt immer die `-ink`-Stufe.

### Secondary
- **Register-Grün** (`get`): Register Get Fast / Modernisierung. Im CSS existiert `--get-ink` mit identischem Wert; Grün ist dunkel genug, um als Text auf dem Blatt zu stehen.

### Tertiary
- **Ultramarin** (`stay`): Register Stay Fast / Weiterentwicklung. `--stay-ink` ist identisch.

### Signal
- **Errata-Rost** (`errata`): ausschließlich für offene Angaben (`.open`): Preise, Fristen, Freigaben, die noch fehlen.

### Neutral
- **Papier** (`paper`): Seitengrund, Startblock, Kopf, Fuß, Abschnitt "Für alle Register". Auch `theme-color`.
- **Blatt** (`leaf`): fast weißes, leicht transparentes Blatt, auf dem jeder Inhalt eines Registers liegt.
- **Tinte** (`ink`): Text, Primär-Button, 1.5px-Kopflinien von Tabellen, Fokusring. `dark` hat denselben Wert und färbt das Kontakt-Register und seinen Reiter.
- **Tinte 2** (`ink-2`): Leads, Fließtext in Listen und Antworten, Labels, Meta-Zeilen, inaktive Kopfnavigation.
- **Linie** (`rule`): 1px-Trennlinien innerhalb von Steckbrief, Ablauf, Preisen, Inhaltsverzeichnis und FAQ.
- **Startgrau** (`start`): nur der Reiter "Start".
- **Kontakt-Blatt / -Linie / -Text / -Lead / Ghost-Linie** (`dark-leaf`, `dark-line`, `dark-text`, `dark-lead`, `dark-ghost-line`): die invertierte Ausführung im Kontakt-Register.
- **Markierung** (`selection`): Textauswahl, ein helles Orange.

### Named Rules
**The One Register, One Color Rule.** Jede Leistung besitzt genau eine Farbe, und diese Farbe erscheint nur als ihr Registerband, ihr Reiter, ihre Farbmarke im Inhaltsverzeichnis und als Akzent auf ihren Blättern (Wochenangaben, Listenmarker, FAQ-Plus über `--hue-ink`). Eine Registerfarbe taucht nie in einem fremden Register auf.

**The Leaf Carries Content Rule.** Auf Registerfarbe stehen nur Registername und Unterzeile in der linken Marginalie (weiß). Überschriften, Fließtext, Steckbrief und Buttons liegen immer auf einem Blatt.

**The Errata Rule.** Rostrot ist für offene Angaben reserviert. Eine fehlende Zahl wird als Errata-Zettel gezeigt, nie weggelassen, nie durch eine erfundene ersetzt und nie unauffällig gestaltet.

## Typography

**Display Font:** Hanken Grotesk (mit system-ui, sans-serif), Gewichte 500/600/700
**Body Font:** Source Serif 4 (mit Georgia, serif), optische Größe 8..60, Gewichte 400/600
**Label/Mono Font:** JetBrains Mono (mit ui-monospace, monospace), Gewicht 500

**Character:** Eine ruhige Buchserif trägt den Text, eine sachliche Grotesk beschriftet und gliedert wie in einem Handbuch, Mono misst. Die Kombination liest sich wie technische Dokumentation mit Satzspiegel, nicht wie Werbung.

### Hierarchy
- **Display** (700, `clamp(2rem, 4vw, 3rem)`, 1.15, max. 24ch): nur die H1 im Startblock der Startseite.
- **Headline** (700, `clamp(1.9rem, 3.8vw, 2.8rem)`, 1.15, max. 22ch): H1 auf dem ersten Blatt einer Leistungsseite.
- **Title** (700, `clamp(1.4rem, 2.6vw, 1.9rem)`, 1.15): H2 auf Blättern. Auf Papier ohne Blatt feste 1.6rem.
- **Register-Name** (700, 1.6rem, 1.1): Name des Registers in der Marginalie.
- **Subtitle** (700, 1.08–1.15rem): H3 in Preisen, Projekten, Zweispaltern.
- **Body** (400, 1.0625rem, 1.62, max. 64ch auf Blättern): aller Fließtext, auch Steckbrief-Werte und Ablauf-Texte.
- **Lead** (400, 1.08rem auf Blättern, 1.15rem im Startblock, max. 56ch, Tinte 2): der Einleitungsabsatz unter einer Überschrift.
- **Label** (600, 0.8rem, +0.04em): Feldnamen im Steckbrief. Reiter nutzen 0.8rem/600/+0.06em, vertikal gesetzt.
- **UI** (600, 1rem): Buttons; Kopfnavigation 500/0.95rem.
- **Wortmarke** (700, 1.05rem, +0.08em, Versalien im Text): "AI ON RAILS", "AI" in Ship-Tinte.
- **Measure** (Mono 500, 0.8–0.82rem): Wochen, Dauern, Unterzeilen in der Marginalie, Laufzeiten im Inhaltsverzeichnis, Errata-Zettel (0.8em). Beträge in Preisen 1.1rem.

Alle Überschriften: Grotesk 700, Zeilenhöhe 1.15, −0.015em, `text-wrap: balance`.

### Named Rules
**The Three Voices Rule.** Serif ist, was man liest. Grotesk ist, was man navigiert und überfliegt (Überschriften, Labels, Buttons, Reiter, Meta-Zeilen). Mono ist, was man misst (Dauer, Woche, Betrag, offene Angabe). Ein Wert, der eine Dauer oder ein Betrag ist, steht in Mono.

**The One Body Size Rule.** Fließtext hat eine Größe (1.0625rem), auch in Steckbrief-Werten und Ablauf-Texten. Größer werden nur Leads und Überschriften.

## Layout

**Seitenmodell.** Die Registerleiste ist fest rechts, 64px breit (`--rail`), über die volle Höhe. Die Seite (`.page`) reserviert rechts genau diese Breite. Der Inhalt sitzt in einem Container von max. 1120px mit Seitenrand `clamp(16px, 4vw, 48px)`.

**Register-Raster.** Jedes Register ist ein Band über die volle Breite (56px oben/unten, Abschnitt auf Papier 64px) mit einem Zweispalter 1fr : 3fr und 28px Abstand: links die Marginalie mit Registername (22px nach unten versetzt, auf Höhe der ersten Blattzeile), rechts ein Stapel Blätter mit 18px Abstand. Blätter haben Innenabstand `clamp(22px, 3.5vw, 40px)`.

**Startblock.** Auf Papier, 48px oben / 64px unten, Zweispalter 2fr : 1fr, 40px Abstand, unten bündig: links H1, Lead, Button-Reihe; rechts das Inhaltsverzeichnis. Unter dem Startblock beginnt sofort das orange Ship-Register.

**Tabellen-Raster.** Steckbrief (0.8fr / 1fr / 1fr / 1.5fr), Ablauf (Bet: `minmax(200px, 2fr) minmax(0, 4fr) minmax(190px, 2fr)`, sonst drei gleiche Spalten), Preise (zwei Spalten) und Zweispalter (1fr 1fr, 28px) teilen ihre Zellen mit senkrechten 1px-Linien statt mit Abständen allein.

**Button-Reihe.** 10px Abstand, 26px über der Reihe, umbrechend.

**Responsive (≤ 860px).**
- Die Registerleiste wird zu einer horizontalen Leiste, sticky oben, 40px hoch; Reiter waagrecht, 0.72rem; Reiter liegen bündig an der Unterkante der Leiste (zur Seite hin); inaktive Reiter sind 34px hoch, der aktive füllt die 40px und ragt nach oben heraus. `--rail` wird 0.
- Alle Zweispalter (Start, Register, Zweispalter, Preise) werden einspaltig; die Marginalie verliert ihren Versatz, auf Papier-Abschnitten wird sie ausgeblendet.
- Steckbrief wird 2×2, die zweite Zeile mit 1px-Linie oben und ohne linke Linie in der ersten Spalte.
- Ablauf wird einspaltig, Schritte durch 1px-Linie oben getrennt.
- Die Textlinks der Kopfnavigation verschwinden, nur Wortmarke und kleiner Button bleiben; die Registerleiste übernimmt die Navigation.
- Porträt 90 × 112px statt 120 × 150px.

### Named Rules
**The Margin Rule.** Der Name eines Registers steht in der linken Marginalie, nicht als Zeile über der Überschrift. Was ein Abschnitt ist, sagt der Rand; was er enthält, sagt die Überschrift.

**The Rail Rule.** Die Registerleiste ist immer da, rechts auf dem Desktop, oben auf dem Telefon. Die Reiterhöhe folgt dem Umfang der Leistung (`--ext`: Start 1.1, Ship 1.6, Get 1.15, Stay 1.15, Kontakt 0.8); Ship ist der größte Reiter, weil die Product Bet führt.

## Elevation & Depth

Hybrid aus flacher Fläche und genau einem physischen Schatten. Papier, Registerbänder, Tabellen und Buttons sind flach. Tiefe entsteht durch das Bild "Blatt liegt auf Karton": Blätter tragen einen kurzen, weichen Schatten. Der aktive Reiter bleibt flach und geht auf Unterseiten nahtlos in sein Registerband über.

### Shadow Vocabulary
- **Blattschatten** (`box-shadow: 0 1px 1px rgba(0, 0, 0, .08), 0 10px 24px -12px rgba(0, 0, 0, .35)`): jedes Blatt auf einem Register oder auf Papier.
- Im Kontakt-Register haben Blätter keinen Schatten, sondern eine 1px-Kante in Kontakt-Linie.

### Named Rules
**The Leaf On Board Rule.** Nur Blätter haben Schatten. Buttons, Tabellen, Bilder und Register bleiben flach; ein Schatten heißt immer "das liegt obenauf".

## Shapes

Rechte Winkel überall: Blätter, Buttons, Reiter, Farbmarken, Errata-Zettel, Porträt (0px Radius). Form entsteht aus Linien: Jede Tabelle (Inhaltsverzeichnis, Steckbrief, Ablauf, Preise, Projekt) beginnt mit einer 1.5px-Linie in Tinte und wird innen mit 1px-Linien in `rule` geteilt. Buttons tragen eine 1.5px-Kontur. Der Errata-Zettel ist die einzige gestrichelte Form. Das FAQ-Plus ist aus zwei 1.5px-Balken gezeichnet, kein Glyph.

**The Square Cut Rule.** Kein Radius. Ecken sind geschnitten wie Papier und Karton.

**The Ledger Rule.** Eine Liste mit Struktur öffnet mit 1.5px Tinte und teilt innen mit 1px `rule`. Keine Karten-Rahmen, keine Hintergrund-Kacheln für Zellen.

## Components

**The Two Step Rule.** Jede Transition läuft über `--step` (`90ms steps(2)`): Reiter, Buttons, FAQ-Plus. Kein Easing, keine andere Dauer, kein Gleiten. Bei `prefers-reduced-motion` entfallen alle Transitions und das weiche Scrollen.

### Buttons
Klar und satt; beim Hover kippt der Button in zwei Stufen in seine Kontur.
- **Shape:** rechteckig (0px), 1.5px Kontur in der Füllfarbe, Grotesk 600 1rem, 12px 20px.
- **Primary (Tinte):** Tinte gefüllt, weißer Text. Standard für Leistungsseiten Get/Stay und Detail-Links.
- **Ship:** Oxidorange gefüllt. Haupt-Aufruf im Startblock, auf der Bet-Seite und für den Link zur Bet.
- **Ghost:** transparent mit Tintenkontur; Hover füllt in Tinte.
- **Hover:** gefüllte Buttons werden transparent, Text nimmt die Konturfarbe an (Ship: Ship-Tinte). Übergang `--step`.
- **Klein:** 7px 14px, 0.9rem, im Seitenkopf.
- **Auf Kontakt-Register:** weiß gefüllt mit Tintentext; Ghost mit Kontur in Ghost-Linie, Hover weiß.
- **Focus:** 2px Tintenring, 3px Abstand (global).

### Registerleiste (Signatur)
- Feste Spalte rechts, 64px, volle Höhe; fünf Reiter Start / Ship Fast / Get Fast / Stay Fast / Kontakt in ihren Farben, Text weiß, vertikal (`writing-mode: vertical-rl`), 0.8rem/600/+0.06em.
- Alle Reiter liegen bündig an der linken Kante der Leiste, also direkt an der Seite; es gibt nie eine Papierfuge zwischen Inhalt und Reiter. In Ruhe sind Reiter 52px breit (64px − 12px); aktiver Reiter (`aria-current`) und Hover ziehen nach außen auf die volle Breite aus, in zwei Stufen (`width`, `steps(2)`). Auf Unterseiten geht der aktive Reiter damit nahtlos in das Registerband gleicher Farbe über.
- Startseite: der Reiter folgt per IntersectionObserver dem Register in der Bildschirmmitte. Unterseiten: `aria-current="page"` am eigenen Reiter.
- Focus: weißer Ring, 4px nach innen versetzt.
- Mobil: siehe Layout.

### Registerband
- Band über die volle Breite in der Registerfarbe, 56px vertikal; Variante `plain` auf Papier (64px), `dark` für Kontakt.
- Setzt `--hue` / `--hue-ink`, die alle Akzente auf den Blättern färben.
- Marginalie: Registername (Grotesk 700 1.6rem, weiß) und Unterzeile in Mono 0.82rem (z.B. "12 Wochen · Festpreis").

### Blatt
- Fast weiß, 0px Radius, Innenabstand `clamp(22px, 3.5vw, 40px)`, Blattschatten, 18px zwischen gestapelten Blättern.
- Absätze max. 64ch; Lead in Tinte 2; Notiz in Tinte 2 mit 18px Abstand.
- Kontakt-Variante: dunkles Blatt, 1px Kante, kein Schatten.

### Steckbrief
- Definitionsliste mit genau vier Feldern in fester Reihenfolge: **Laufzeit, Einstieg, Kosten, Ergebnis**. Spalten 0.8 / 1 / 1 / 1.5, 1.5px Tintenlinie oben, 1px-Linien zwischen den Feldern, 24px unter dem Lead.
- Feldname als Label (Grotesk 600 0.8rem, Tinte 2), Wert in Body-Größe, mit Silbentrennung.
- Mobil 2×2.

**The Same Four Fields Rule.** Jedes Register und jede Leistungsseite führt den Steckbrief mit denselben vier Feldern in derselben Reihenfolge. Fehlt ein Wert, steht dort ein Errata-Zettel, das Feld bleibt.

### Ablauf
- Geordnete Liste als Spaltenreihe, 1.5px Tintenlinie oben, 1px-Linien zwischen den Schritten.
- Pro Schritt: Zeitraum in Mono 0.8rem in `--hue-ink`, Schrittname in Grotesk fett, Beschreibung in Body/Tinte 2.
- Bet: drei Spalten nach Dauer gewichtet (2 : 5 : 2); Modernisierung: drei gleiche Spalten. Mobil einspaltig.

### Preise
- Zwei Spalten mit 1.5px Tintenlinie oben und 1px-Trennlinie. Pro Spalte: Name (H3), Art in Grotesk 500 0.9rem Tinte 2, Betrag in Mono 1.1rem, Erläuterung in Tinte 2.
- Offene Beträge stehen als Errata-Zettel im Betragsfeld.

### Häufige Fragen
- Native `details`/`summary`, 1px-Linien oben und unter dem letzten Eintrag, 14px vertikal.
- Frage in Grotesk 600 1.02rem; rechts ein 14px-Plus aus zwei 1.5px-Balken in `--hue-ink`, offen klappt der senkrechte Balken in zwei Stufen weg (Minus).
- Antwort in Tinte 2, 8px Abstand.

### Errata-Zettel (offene Angabe)
- Inline-Marke: Mono 500 0.8em, Rostrot, 1px gestrichelte Kontur in Textfarbe, 0 5px Innenabstand, kein Umbruch.
- Steht genau dort, wo die fehlende Angabe hingehört (Preis, Frist, Nutzerzahl, Freigabe), mit einem knappen Wort ("offen", "Preis", "5.900 €/Monat?").

### Inhaltsverzeichnis
- Geordnete Liste im Startblock, Grotesk 500 0.92rem, 1.5px Tintenlinie oben, 1px `rule` unter jeder Zeile, 9px vertikal.
- Links eine 12px-Farbmarke in Registerfarbe und der Leistungsname, rechts die Dauer in Mono 0.8rem Tinte 2.

### Navigation (Kopf)
- Wortmarke links, rechts Textlinks in Grotesk 500 0.95rem (Tinte 2, aktiv/Hover Tinte, aktiv unterstrichen) und ein kleiner Primär-Button "Gespräch vereinbaren". Mobil nur Wortmarke und Button.

### Projekt und Person
- Projekt: 1.5px Tintenlinie oben, H3, Meta-Zeile in Grotesk 500 0.88rem Tinte 2 ("Ship Fast · E-Commerce · seit 2026"), Text in Tinte 2.
- Person: Porträt 120 × 150px, rechteckig, `object-fit: cover`, daneben Name, Rolle (Grotesk 500 0.9rem Tinte 2), Text.
- Team (`.team`): drei gleichrangige Rollen nebeneinander (mobil untereinander), je 1.5px-Kopflinie in Tinte, Rollenname als h3, Meta-Zeile (Grotesk 500 0.88rem) mit Person bzw. Herkunft, Text in Serif. Nur die Rolle mit benannter Person trägt ein Porträt, 64 × 80px rechts eingerückt, damit die Rollenüberschriften auf einer Linie bleiben. Keine Rolle wird durch ein großes Foto hervorgehoben.

## Do's and Don'ts

### Do:
- **Do** lege jeden Inhalt eines Registers auf ein Blatt (`leaf`) und lass nur Registername und Mono-Unterzeile direkt auf der Registerfarbe stehen.
- **Do** führe in jedem Register den Steckbrief mit Laufzeit, Einstieg, Kosten, Ergebnis in dieser Reihenfolge.
- **Do** setze jede Dauer, Woche und jeden Betrag in JetBrains Mono 500.
- **Do** markiere jede fehlende Angabe mit dem Errata-Zettel in Rostrot (gestrichelt, Mono) an der Stelle, wo sie fehlt.
- **Do** nutze für jede Transition `--step` (90ms steps(2)) und schalte sie bei `prefers-reduced-motion` ab.
- **Do** öffne strukturierte Listen mit einer 1.5px-Tintenlinie und teile innen mit 1px `rule`.
- **Do** färbe Text in Registerfarbe auf hellem Grund mit der `-ink`-Stufe (Ship-Tinte statt Ship-Orange).
- **Do** gib eine neue Leistungsseite ihr eigenes Register: Seite öffnet im Band ihrer Farbe, H1 auf dem ersten Blatt, Steckbrief, Button, Reiter mit `aria-current="page"`.

### Don't:
- **Don't** setze Überschriften, Fließtext, Steckbrief oder Buttons direkt auf ein Registerband.
- **Don't** runde Ecken; der Radius ist 0px.
- **Don't** verwende Easing-Kurven, weiche Übergänge oder andere Dauern als 90ms steps(2).
- **Don't** gib Elementen außer Blättern einen Schatten.
- **Don't** verschiebe Reiter zur Seite hin (z.B. per `translateX`); zwischen Inhalt und Leiste darf keine Fuge entstehen.
- **Don't** nutze Rostrot für etwas anderes als offene Angaben, und verstecke offene Angaben nicht.
- **Don't** trage eine Registerfarbe in ein fremdes Register oder führe eine vierte Akzentfarbe ein.
- **Don't** baue Hero-Bild, drei gleiche Karten oder eine Logoleiste; Leistungen sind Register, keine Kacheln.
- **Don't** setze Labels oder Kicker über Überschriften; der Abschnittsname gehört in die Marginalie.
- **Don't** verwende Icon-Sets oder Glyph-Icons; Marken sind Farbquadrate, Linien und gezeichnete Balken.
