#!/usr/bin/env python3
"""Aufruf aus dem Repo-Root: python3 _build/build.py .
Erzeugt die statischen Seiten für ai-on-rails.com (Relaunch Säulen).
Einmaliger Generator; die Ausgabe ist plain HTML im Repo, kein Build-Schritt auf GitHub Pages."""
import json, sys
from pathlib import Path
from html import escape

REPO = Path(sys.argv[1])
BASE = "https://ai-on-rails.com"
CAL = "https://calendar.app.google/VdnLNLqjpSR4MS6G7"
MAIL = "hello@ai-on-rails.com"
OG = f"{BASE}/og-image.png?v=2026-11-19b"

ORG = {
    "@type": ["Organization", "ProfessionalService"],
    "@id": f"{BASE}/#organization",
    "name": "AI on Rails",
    "url": f"{BASE}/",
    "logo": OG,
    "email": MAIL,
    "address": {"@type": "PostalAddress", "streetAddress": "Lehmberg 7", "postalCode": "23795", "addressLocality": "Negernbötel", "addressRegion": "Schleswig-Holstein", "addressCountry": "DE"},
    "areaServed": [{"@type": "City", "name": "Hamburg"}, {"@type": "Country", "name": "Deutschland"}],
    "knowsAbout": ["Ruby on Rails", "Produktentwicklung", "UX-Design", "UI-Design", "Rails-Upgrade", "Softwaremodernisierung", "Wartung von Webanwendungen", "KI-gestützte Softwareentwicklung"],
    "founder": {"@id": f"{BASE}/#henning"},
    "sameAs": ["https://henning-thies.de", "https://www.linkedin.com/in/henningthies/"],
}
PERSON = {
    "@type": "Person",
    "@id": f"{BASE}/#henning",
    "name": "Henning Thies",
    "url": "https://henning-thies.de",
    "jobTitle": "Gründer",
    "worksFor": {"@id": f"{BASE}/#organization"},
    "address": {"@type": "PostalAddress", "streetAddress": "Lehmberg 7", "postalCode": "23795", "addressLocality": "Negernbötel", "addressRegion": "Schleswig-Holstein", "addressCountry": "DE"},
    "knowsAbout": ["Ruby on Rails", "Ruby", "Softwarearchitektur", "KI-gestützte Softwareentwicklung"],
    "sameAs": ["https://henning-thies.de", "https://www.linkedin.com/in/henningthies/"],
}

NAV = [("/product-bets", "Product Bets"), ("/rails-modernisierung", "Modernisierung"), ("/rails-weiterentwicklung", "Weiterentwicklung")]


def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", "", s)


def ld(page):
    url = BASE + page["path"]
    graph = [ORG]
    webpage = {
        "@type": "WebPage",
        "@id": f"{url}#webpage",
        "url": url,
        "name": page["title"],
        "description": page["desc"],
        "inLanguage": "de-DE",
        "isPartOf": {"@id": f"{BASE}/#website"},
        "about": {"@id": f"{BASE}/#organization"},
    }
    if page["path"] == "/":
        graph.append(PERSON)
        graph.append({"@type": "WebSite", "@id": f"{BASE}/#website", "url": f"{BASE}/", "name": "AI on Rails", "inLanguage": "de-DE", "publisher": {"@id": f"{BASE}/#organization"}})
    else:
        webpage["breadcrumb"] = {"@id": f"{url}#breadcrumb"}
        graph.append({
            "@type": "BreadcrumbList",
            "@id": f"{url}#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Start", "item": f"{BASE}/"},
                {"@type": "ListItem", "position": 2, "name": page["crumb"], "item": url},
            ],
        })
        svc = page["service"]
        graph.append({
            "@type": "Service",
            "@id": f"{url}#service",
            "name": svc["name"],
            "serviceType": svc["type"],
            "description": page["desc"],
            "provider": {"@id": f"{BASE}/#organization"},
            "areaServed": {"@type": "Country", "name": "DE"},
            "url": url,
            **({"offers": svc["offers"]} if svc.get("offers") else {}),
        })
        webpage["mainEntity"] = {"@id": f"{url}#service"}
    graph.insert(1, webpage)
    faq = [f for f in page.get("faq", []) if "class=\"ph\"" not in f[1]]
    if faq:
        graph.append({
            "@type": "FAQPage",
            "@id": f"{url}#faq",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faq],
        })
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)




# ------------------------------------------------------------------ Variante C: Handbuch mit Registern

def ph(s):
    return f'<span class="open">{s}</span>'


def ul(items):
    return '<ul class="list">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


TABS_PAGES = [("/", "t-start", "Start", "1.1"), ("/product-bets", "t-ship", "Ship Fast", "1.6"),
              ("/rails-modernisierung", "t-get", "Get Fast", "1.15"), ("/rails-weiterentwicklung", "t-stay", "Stay Fast", "1.15"),
              ("#kontakt", "t-kontakt", "Kontakt", ".8")]
TABS_START = [("#start", "t-start", "Start", "1.1"), ("#ship", "t-ship", "Ship Fast", "1.6"),
              ("#get", "t-get", "Get Fast", "1.15"), ("#stay", "t-stay", "Stay Fast", "1.15"),
              ("#kontakt", "t-kontakt", "Kontakt", ".8")]


def tabs(page):
    if page["path"] == "/":
        items = [f'  <a class="{c}" href="{h}" style="--ext:{e}" aria-current="false">{l}</a>' for h, c, l, e in TABS_START]
    else:
        items = []
        for h, c, l, e in TABS_PAGES:
            cur = ' aria-current="page"' if h == page["path"] else ""
            items.append(f'  <a class="{c}" href="{h}" style="--ext:{e}"{cur}>{l}</a>')
    return '<nav class="tabs" aria-label="Register">\n' + "\n".join(items) + "\n</nav>\n"


NAV = [("/product-bets", "Product Bets"), ("/rails-modernisierung", "Modernisierung"), ("/rails-weiterentwicklung", "Weiterentwicklung")]


def ld_block(page):
    if page.get("legal"):
        return ""
    return f"""  <script type="application/ld+json">
{ld(page)}
  </script>
"""


def head(page):
    url = BASE + page["path"]
    t, d = escape(page["title"]), escape(page["desc"])
    nav = "\n".join(f'        <a href="{h}"{" aria-current=\"page\"" if h == page["path"] else ""}>{l}</a>' for h, l in NAV)
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t}</title>
  <meta name="description" content="{d}">
  <link rel="canonical" href="{url}">

  <meta property="og:title" content="{t}">
  <meta property="og:description" content="{d}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{OG}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="AI on Rails">
  <meta property="og:locale" content="de_DE">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t}">
  <meta name="twitter:description" content="{d}">
  <meta name="twitter:image" content="{OG}">

  <meta name="robots" content="{page.get("robots", "index, follow")}">
  <meta name="theme-color" content="#eff4f6">
  <meta name="author" content="Henning Thies">
  <link rel="sitemap" type="application/xml" href="/sitemap.xml">

  <script defer src="https://cloud.umami.is/script.js" data-website-id="5dde56bc-9822-4d4c-a606-0bd521350c76"></script>

  <link rel="preload" href="/assets/fonts/hanken-grotesk-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/source-serif-4-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/site.css">

{ld_block(page)}</head>
<body>
<a class="skip-link" href="#main">Zum Inhalt springen</a>
<div class="page">
<header class="top">
  <div class="in">
    <a class="brand" href="/" aria-label="AI on Rails, Startseite"><span>AI</span> ON RAILS</a>
    <nav aria-label="Hauptnavigation">
{nav}
      <a class="btn sm" href="{"/#kontakt" if page.get("legal") else "#kontakt"}">Gespräch vereinbaren</a>
    </nav>
  </div>
</header>
<main id="main">
"""


FOOT = """</main>
<footer><div class="in"><span>AI on Rails · Ruby on Rails Agentur · Region Hamburg</span><ul><li><a href="/product-bets">Product Bets</a></li><li><a href="/rails-modernisierung">Modernisierung</a></li><li><a href="/rails-weiterentwicklung">Weiterentwicklung</a></li><li><a href="/impressum">Impressum</a></li><li><a href="/datenschutz">Datenschutz</a></li></ul></div></footer>
</div>
"""

SCRIPT_START = """<script>
// Startseite: Reiter des Registers ausziehen, das gerade im Blick ist
(function () {
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.tabs a'));
  if (!('IntersectionObserver' in window)) return;
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return;
      tabs.forEach(function (t) { t.setAttribute('aria-current', String(t.getAttribute('href') === '#' + e.target.id)); });
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  document.querySelectorAll('[data-reg]').forEach(function (s) { io.observe(s); });
})();
</script>
"""


def brief(laufzeit, einstieg, kosten, ergebnis):
    return f"""<dl class="brief">
        <div><dt>Laufzeit</dt><dd>{laufzeit}</dd></div>
        <div><dt>Einstieg</dt><dd>{einstieg}</dd></div>
        <div><dt>Preis</dt><dd>{kosten}</dd></div>
        <div><dt>Ergebnis</dt><dd>{ergebnis}</dd></div>
      </dl>"""


BRIEF_SHIP = brief("12 Wochen", "Workshop-Tag", "Festpreis, festgelegt nach dem Workshop-Tag", "UX-Konzept, Design, Anwendung im Test mit euren Nutzern, Entscheidungs&shy;vorlage")
BRIEF_GET = brief("Audit 2 Wochen, dann je Meilen&shy;stein", "Technisches Audit", "Festpreis je Meilen&shy;stein, festgelegt nach dem Audit", "Audit-Bericht mit Risiken und Plan, Meilen&shy;steine, die einzeln live gehen")
BRIEF_STAY = brief("Monatlich, mindestens 3 Monate", "Einrichtung von Zugängen und Abläufen", "Monatlicher Festbetrag je nach Umfang", "Updates, Fehler&shy;behebung, neue Funktionen, Monats&shy;bericht")


def contact(title, text, sub="30 Minuten"):
    return f"""
<section class="reg dark" id="kontakt" aria-labelledby="k-h">
  <div class="in grid">
    <div class="margin"><span class="name">Kontakt</span><span class="sub">{sub}</span></div>
    <div class="leaf">
      <h2 id="k-h">{title}</h2>
      <p class="lead">{text}</p>
      <div class="row"><a class="btn" href="{CAL}" target="_blank" rel="noopener">Termin wählen</a><a class="btn ghost" href="mailto:{MAIL}">{MAIL}</a></div>
    </div>
  </div>
</section>
"""


def faq(items):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


def section(cls, name, sub, body, hid=None, sid=None):
    attrs = f' id="{sid}"' if sid else ""
    lab = f' aria-labelledby="{hid}"' if hid else ""
    subh = f'<span class="sub">{sub}</span>' if sub else ""
    return f"""
<section class="reg {cls}"{attrs}{lab}>
  <div class="in grid">
    <div class="margin"><span class="name">{name}</span>{subh}</div>
    <div>{body}</div>
  </div>
</section>
"""


def leaf(inner):
    return f'<div class="leaf">{inner}</div>'


# ---------------------------------------------------------------- Startseite
start = dict(path="/", file="index.html",
             title="Produktentwicklung und Ruby on Rails Agentur Hamburg | ai-on-rails",
             desc="In 12 Wochen wissen, ob eine Produktidee trägt: laufende Anwendung auf euren Daten, Test mit euren Nutzern, Entscheidungsvorlage. Agentur, Region Hamburg.")

start_body = f"""
<section class="start" id="start" aria-labelledby="start-h">
  <div class="in startgrid">
    <div>
      <h1 id="start-h">In 12 Wochen wisst ihr, ob eure Produktidee trägt.</h1>
      <p class="lead">Wir bauen sie als laufende Anwendung auf euren Daten. Ab Woche 4 testen eure Nutzer, in Woche 12 liegt die Entscheidungsvorlage: weiterbauen, umbauen oder stoppen. Zum Festpreis, bevor ihr ein Team einstellt.</p>
      <div class="row"><a class="btn" href="#kontakt">Idee in 30 Minuten prüfen lassen</a><a class="btn ghost" href="/product-bets#ablauf">Ablauf ansehen</a></div>
      <p class="proof">Der Workshop-Tag zum Einstieg wird bei Beauftragung angerechnet.<br>Aktuell: <a href="#projekte">KI-Produkt für Modemarken, SaaS-Plattform für Versicherer</a></p>
    </div>
    <ol class="index" aria-label="Leistungen">
      <li><a href="#ship"><i style="background:var(--ship)"></i>Product Bets</a><span>12 Wochen</span></li>
      <li><a href="#get"><i style="background:var(--get)"></i>Modernisierung</a><span>in Meilensteinen</span></li>
      <li><a href="#stay"><i style="background:var(--stay)"></i>Weiterentwicklung</a><span>monatlich</span></li>
    </ol>
  </div>
</section>

<section class="reg ship" id="ship" aria-labelledby="ship-h">
  <div class="in grid">
    <div class="margin"><span class="name">Ship Fast</span><span class="sub">12 Wochen · Festpreis</span></div>
    <div class="leaf">
      <h2 id="ship-h">Product Bets: eine Produktidee in 12 Wochen testen</h2>
      <p class="lead">Anforderungen mit eurem Fachbereich, UX-Konzept, Design und Entwicklung in einem Team. Ihr stellt die Idee, den Zugang zu euren Daten und die Testnutzer.</p>
      {BRIEF_SHIP}
      <div class="row"><a class="btn" href="/product-bets">Product Bets im Detail</a></div>
    </div>
  </div>
</section>

<section class="reg get" id="get" aria-labelledby="get-h">
  <div class="in grid">
    <div class="margin"><span class="name">Get Fast</span><span class="sub">Audit · 2 Wochen</span></div>
    <div class="leaf">
      <h2 id="get-h">Bestehende Anwendungen modernisieren</h2>
      <p class="lead">Rails- und Ruby-Upgrades, Performance und Codequalität. Ältere Anwendungen in anderen Technologien bauen wir schrittweise in Rails neu. Jeder Meilenstein geht einzeln live, die Anwendung läuft weiter.</p>
      {BRIEF_GET}
      <div class="row"><a class="btn" href="/rails-modernisierung">Modernisierung im Detail</a></div>
    </div>
  </div>
</section>

<section class="reg stay" id="stay" aria-labelledby="stay-h">
  <div class="in grid">
    <div class="margin"><span class="name">Stay Fast</span><span class="sub">monatlich</span></div>
    <div class="leaf">
      <h2 id="stay-h">Webanwendungen weiterentwickeln und betreuen</h2>
      <p class="lead">Laufende Weiterentwicklung eurer Anwendung zu einem festen Monatsbetrag: Sicherheits-Updates, Fehlerbehebung und neue Funktionen. In Rails und in anderen Technologien. Ihr priorisiert, wir liefern.</p>
      {BRIEF_STAY}
      <div class="row"><a class="btn" href="/rails-weiterentwicklung">Weiterentwicklung im Detail</a></div>
    </div>
  </div>
</section>

<section class="reg plain" id="zusammenhang" aria-labelledby="zus-h">
  <div class="in">
    <div class="blk">
      <h2 id="zus-h">Wie die Leistungen zusammenhängen</h2>
      <ol class="cols3">
        <li><h3>Workshop-Tag oder Audit</h3><span class="m">Einstieg</span><p>Am Workshop-Tag schärfen wir mit eurem Fachbereich Idee, Erfolgskriterium und Datenlage. Im Audit prüfen wir zwei Wochen lang Zustand und Risiken einer bestehenden Anwendung. Danach steht der Festpreis für das Projekt.</p></li>
        <li><h3>Product Bet oder Modernisierung</h3><span class="m">Projekt · Festpreis</span><p>Eine Product Bet dauert 12 Wochen: Anforderungen, Design und eine laufende Anwendung, die eure Nutzer testen, am Ende eine Entscheidungsvorlage. Eine Modernisierung läuft in Meilensteinen, die einzeln live gehen.</p></li>
        <li><h3>Weiterentwicklung oder Übergabe</h3><span class="m">Danach · auf Wunsch</span><p>Wir entwickeln zu einem festen Monatsbetrag weiter, oder euer Team übernimmt. Dann übergeben wir mit Dokumentation und Einarbeitung und helfen bei der Auswahl eurer Entwickler.</p></li>
      </ol>
    </div>

    <div class="blk">
      <h2 id="ki-h">Wie wir arbeiten</h2>
      <div class="cols3">
        <div><h3>Unsere Arbeitsweise</h3>{ul(["Wir entwickeln mit KI. Werkzeuge und Abläufe wählen wir selbst.", "Projekte rechnen wir zum Festpreis ab, nicht nach Aufwand.", "Ein Mensch prüft jede Änderung, bevor sie live geht.", "Ihr seht jede Woche den aktuellen Stand."])}</div>
        <div><h3>Was bei euch bleibt</h3>{ul(["Quellcode, Designs und Zugänge gehören euch.", "Wir entwickeln auf euren Daten und in euren Systemen.", "Alles ist so dokumentiert, dass euer Team übernehmen kann."])}</div>
        <div><h3>Warum Ruby on Rails</h3><p>Neue Anwendungen bauen wir mit Ruby on Rails. Rails gibt jeder Anwendung dieselbe Struktur und feste Regeln, wo was hingehört. In diesem Rahmen arbeitet KI verlässlich, und jede Änderung lässt sich schnell prüfen. Daher der Name: KI auf festen Schienen.</p><p>Bestehende Anwendungen in anderen Technologien entwickeln wir weiter oder bauen sie schrittweise neu.</p></div>
      </div>
    </div>

    <div class="blk">
      <h2 id="projekte">Projekte</h2>
      <div class="cols3">
        <article><h3>KI-Produkt für Modemarken</h3><span class="m">Stay Fast · E-Commerce · seit März 2026</span>
          <dl class="facts">
            <div><dt>Ausgangslage</dt><dd>Ein KI-Produkt, das Produktbilder für die Onlineshops von Modemarken erzeugt. Es war in einem internen Test entstanden und sollte zum Produkt für zahlende Marken werden.</dd></div>
            <div><dt>Unsere Rolle</dt><dd>Wir unterstützen das Team des Kunden bei der Weiterentwicklung: neue Funktionen und ein KI-gestützter Entwicklungsablauf, in dem ein Mensch jede Änderung prüft. Gebaut mit Ruby on Rails.</dd></div>
            <div><dt>Stand</dt><dd>Das Produkt ist bei Modemarken und Onlinehändlern im Einsatz, laut Kunde sind damit bisher über 140.000 Outfits entstanden. Der Kunde baut jetzt ein eigenes Team auf, wir unterstützen bei der Auswahl der Entwickler.</dd></div>
          </dl>
        </article>
        <article><h3>Code-Audit einer KI-Plattform</h3><span class="m">Get Fast · Agentur · Juni 2026</span>
          <dl class="facts">
            <div><dt>Ausgangslage</dt><dd>Eine Agentur nutzt eine eigene KI-Plattform mit rund 300.000 Zeilen Code, überwiegend von einer Person mit KI-Unterstützung geschrieben. Die Geschäftsführung wollte wissen, ob sie die Plattform sicher intern nutzen kann und wie es weitergehen soll.</dd></div>
            <div><dt>Unsere Rolle</dt><dd>Wir haben die Plattform in fünf Bereichen geprüft: Sicherheit, Datenschutz, Wartbarkeit, Kern und Ballast, Tragfähigkeit für Wachstum. Jeder Befund ist am Code belegt, der Bericht ist für die Geschäftsführung ohne Programmierkenntnisse lesbar.</dd></div>
            <div><dt>Ergebnis</dt><dd>Drei kritische Sicherheitsbefunde, darunter eine Prompt-Injection, über die eine hochgeladene Datei eine Aktion nach außen auslösen konnte. Dazu eine Empfehlung mit Umsetzungspfad: erst sieben Pflichtkorrekturen und eine automatische Prüfung vor jedem Merge, dann die Richtung für die Weiterentwicklung. Nach der Übergabe hat der Kunde Beratungsstunden beauftragt.</dd></div>
          </dl>
        </article>
        <article><h3>SaaS-Plattform für Versicherer</h3><span class="m">Stay Fast · Versicherung · seit 2023</span>
          <dl class="facts">
            <div><dt>Ausgangslage</dt><dd>Eine mandantenfähige Plattform, über die mehrere Versicherer ihre Produkte, Schäden und Abrechnung verwalten. Ruby on Rails mit GraphQL-API und Vue.js, entwickelt im Team eines Softwarekonzerns.</dd></div>
            <div><dt>Unsere Rolle</dt><dd>Wir unterstützen das Entwicklungsteam des Kunden bei der Weiterentwicklung: Produkt-Engine für die Verteilung von Risiken auf mehrere Versicherer, Lead-Entwicklung im Schadenmodul, Funktionen für Buchhaltung und Abrechnung.</dd></div>
            <div><dt>Stand</dt><dd>Läuft seit September 2023. Seit 2026 mit den KI-Werkzeugen, die der Konzern freigegeben hat.</dd></div>
          </dl>
        </article>
      </div>
    </div>

    <div class="blk">
      <h2 id="team-h">Team</h2>
      <div class="cols3 team">
        <article>
          <img src="/henning-thies.webp" alt="Henning Thies" width="120" height="150" loading="lazy">
          <h3>Henning Thies</h3><span class="m">Gründer · Product Engineering · Dipl.-Ing.</span>
          {ul(["Anforderungen", "Systemdesign und Architektur", "Entwicklung", "Ansprechpartner vom ersten Gespräch bis zur Übergabe"])}
          <p class="links"><a href="https://henning-thies.de" target="_blank" rel="noopener">henning-thies.de</a> · <a href="https://www.linkedin.com/in/henningthies/" target="_blank" rel="noopener">LinkedIn</a></p>
        </article>
        <article>
          <img src="/karin-krech.webp" alt="Karin Krech" width="120" height="150" loading="lazy">
          <h3>Karin Krech</h3><span class="m">UX, Produkt und Management</span>
          {ul(["Nutzerflüsse und Wireframes", "Gestaltung der Oberflächen", "Produktmanagement", "Projektorganisation"])}
          <p class="links"><a href="https://www.linkedin.com/in/karin-krech-63ab86291/" target="_blank" rel="noopener">LinkedIn</a></p>
        </article>
        <article class="net">
          <div class="net-tile" aria-hidden="true"></div>
          <h3>Netzwerk</h3><span class="m">Je nach Projekt</span>
          <p><a href="https://normkit.digital" target="_blank" rel="noopener">normkit.digital</a>, ein Studio für Produktentwicklung und UX/UI-Design aus Freiburg und Hamburg, bei größeren Design-Vorhaben.</p>
          <p>Dazu Freelancer aus unserem Netzwerk, je nach Bedarf.</p>
        </article>
      </div>
    </div>
  </div>
</section>
""" + contact("Idee prüfen lassen", "30 Minuten, unverbindlich. Ihr beschreibt eure Idee oder eure Anwendung, wir sagen, ob sie in 12 Wochen testbar ist oder was der erste Schritt wäre.")

# ---------------------------------------------------------------- Product Bets
bets_faq = [
    ("Was ist der Unterschied zu einem Klickdummy?", "Nach 12 Wochen läuft die Anwendung auf euren Daten und wird von Testnutzern benutzt. Gemessen wird echtes Verhalten."),
    ("Wie setzt ihr KI ein?", "In der Entwicklung, mit unseren eigenen Werkzeugen und Abläufen. Für euch zählt das Ergebnis: Ein Mensch prüft jede Änderung, bevor sie live geht, und Code und Designs gehören euch."),
    ("Warum baut ihr mit Ruby on Rails?", "Rails gibt jeder Anwendung dieselbe Struktur und feste Regeln. Darin arbeitet KI verlässlich, und jede Änderung lässt sich schnell prüfen. Anbindungen an eure bestehenden Systeme, egal in welcher Technologie, laufen über APIs und sind Teil der Arbeit."),
    ("Brauchen wir eigene Designer?", "Nein. Anforderungen, UX-Konzept und UI-Design sind Teil der Bet. UX und UI-Design übernimmt eine eigene Rolle im Team, nicht die Entwicklung nebenbei. Habt ihr einen Styleguide oder ein Designsystem, arbeiten wir damit."),
    ("Wem gehören Code und Designs?", "Euch, ab dem ersten Commit bzw. der ersten Datei."),
]
bets = dict(path="/product-bets", file="product-bets.html", crumb="Product Bets",
            title="Product Bets: Produktidee in 12 Wochen testen | ai-on-rails",
            desc="Anforderungen, UX-Konzept, Design und eine laufende Anwendung auf euren Daten in 12 Wochen, mit Entscheidungsvorlage. Zum Festpreis.",
            service={"name": "Product Bets", "type": "Produktentwicklung: Anforderungen, UX- und UI-Design und Softwareentwicklung (Proof of Concept)"}, faq=bets_faq)
bets_body = f"""
<section class="reg ship" aria-labelledby="h1">
  <div class="in grid">
    <div class="margin"><span class="name">Ship Fast</span><span class="sub">12 Wochen · Festpreis</span></div>
    <div>
      <div class="leaf">
        <h1 id="h1">Product Bets: eine Produktidee in 12 Wochen testen</h1>
        <p class="lead">Wir klären mit eurem Fachbereich die Anforderungen, entwerfen das UX-Konzept, gestalten die Oberfläche und bauen die Produktidee als laufende Anwendung auf euren Daten. In Woche 12 liegt eine Entscheidungsvorlage: weiterbauen, umbauen oder stoppen. Zum Festpreis. Für Unternehmen, die eine Idee testen wollen, bevor sie dafür ein Team aufbauen.</p>
        {BRIEF_SHIP}
        <div class="row"><a class="btn" href="#kontakt">Gespräch vereinbaren</a></div>
      </div>
      <div class="leaf">
        <h2 id="ablauf">Ablauf</h2>
        <ol class="track w-bet">
          <li><span class="w">Woche 1–2</span><b>Anforderungen und Ziel</b><span class="t">Anforderungen mit eurem Fachbereich, Erfolgs&shy;kriterium, UX-Konzept mit Nutzer&shy;flüssen und Wireframes. Ihr gebt das Kriterium frei.</span></li>
          <li><span class="w">Woche 3–10</span><b>Gestalten und entwickeln</b><span class="t">Design und Entwicklung der Anwendung auf euren Daten. Jede Woche eine Demo, ab Woche 4 eine testbare Version für Testnutzer, die ihr stellt.</span></li>
          <li><span class="w">Woche 11–12</span><b>Auswerten</b><span class="t">Messung gegen das Kriterium aus Woche 2 und Entscheidungs&shy;vorlage.</span></li>
        </ol>
      </div>
      <div class="leaf">
        <h2>Was ihr stellt und was ihr bekommt</h2>
        <div class="two">
          <div><h3>Ihr stellt</h3>{ul(["Idee und geschäftlichen Hintergrund", "Eine Person, die in Woche 12 entscheidet", "Zugang zu Daten und Systemen ab Woche 1", "Testnutzer oder Pilotkunden ab Woche 4"])}</div>
          <div><h3>Ihr bekommt</h3>{ul(["Dokumentierte Anforderungen und messbares Erfolgskriterium", "UX-Konzept mit Nutzerflüssen und Wireframes", "Design der Oberfläche", "Laufende Anwendung, getestet mit euren Testnutzern", "Wöchentliche Demos", "Messergebnis und Entscheidungsvorlage"])}</div>
        </div>
        <p class="note">Nicht enthalten: Marktforschung, Businessplan, Marketing.</p>
      </div>
      <div class="leaf">
        <h2>Nach Woche 12</h2>
        <ol class="track w-3">
          <li><span class="w">Go</span><b>Weiterbauen mit uns</b><span class="t">Weiterentwicklung über <a href="/rails-weiterentwicklung">Stay Fast</a> zu einem festen Monatsbetrag.</span></li>
          <li><span class="w">Go</span><b>Selbst übernehmen</b><span class="t">Übergabe an euer Team mit Dokumentation und Einarbeitung. Auf Wunsch helfen wir bei der Auswahl eurer Entwickler.</span></li>
          <li><span class="w">No-Go</span><b>Stoppen</b><span class="t">Ihr behaltet Code, Designs und Messergebnis. Die Entscheidungs&shy;vorlage dokumentiert, warum.</span></li>
        </ol>
      </div>
      <div class="leaf">
        <h2>Wie der Preis entsteht</h2>
        <div class="prices">
          <div><h3>Workshop-Tag</h3><span class="k">Einstieg</span><p>Wir schärfen Idee, Erfolgskriterium und Datenlage. Danach steht der Festpreis für die 12 Wochen. Bei Beauftragung der Bet wird der Workshop-Tag angerechnet.</p></div>
          <div><h3>Product Bet</h3><span class="k">12 Wochen · Festpreis</span><p>Der Preis hängt von Umfang und Datenlage ab und steht nach dem Workshop-Tag fest. Bei einem Go: Weiterentwicklung über <a href="/rails-weiterentwicklung">Stay Fast</a> oder Übergabe an euer Team.</p></div>
        </div>
        <p class="note">Einen Preisrahmen für eure Idee nennen wir im ersten Gespräch.</p>
      </div>
      <div class="leaf">
        <h2>Häufige Fragen</h2>
        {faq(bets_faq)}
      </div>
    </div>
  </div>
</section>
""" + contact("Gespräch vereinbaren", "30 Minuten. Ihr beschreibt die Idee, wir sagen, ob sie in 12 Wochen testbar ist.")

# ---------------------------------------------------------------- Modernisierung
mod_faq = [
    ("Upgrade oder Neubau?", "Das hängt vom Zustand der Anwendung ab. Das Audit beantwortet genau diese Frage, mit Aufwand für beide Wege."),
    ("Modernisiert ihr auch Anwendungen, die nicht in Rails gebaut sind?", "Ja. Das Audit zeigt, ob sich die bestehende Anwendung weiterführen lässt oder ob ein schrittweiser Neubau günstiger ist. Neu bauen wir mit Ruby on Rails."),
    ("Müssen wir den Betrieb unterbrechen?", "Nein. Wir arbeiten in Meilensteinen, die einzeln live gehen."),
    ("Wie setzt ihr KI ein?", "In der Entwicklung, mit unseren eigenen Werkzeugen und Abläufen. Für euch zählt das Ergebnis: Ein Mensch prüft jede Änderung, bevor sie live geht, und Code und Designs gehören euch."),
    ("Arbeitet ihr mit unserem Team zusammen?", "Ja. Wir arbeiten in eurem Repository. Jede Änderung kommt als Pull Request, euer Team kann sie jederzeit einsehen."),
]
mod = dict(path="/rails-modernisierung", file="rails-modernisierung.html", crumb="Modernisierung",
           title="Rails Upgrade und Modernisierung von Webanwendungen | ai-on-rails",
           desc="Technisches Audit, Rails- und Ruby-Upgrade, Performance und schrittweiser Neubau älterer Anwendungen, in Meilensteinen zum Festpreis.",
           service={"name": "Rails Upgrade und Modernisierung", "type": "Ruby on Rails Upgrade und Modernisierung von Webanwendungen"}, faq=mod_faq)
mod_body = f"""
<section class="reg get" aria-labelledby="h1">
  <div class="in grid">
    <div class="margin"><span class="name">Get Fast</span><span class="sub">Audit · 2 Wochen</span></div>
    <div>
      <div class="leaf">
        <h1 id="h1">Bestehende Anwendungen modernisieren</h1>
        <p class="lead">Wir modernisieren gewachsene Webanwendungen: Upgrade auf aktuelle Rails- und Ruby-Versionen, Performance und Codequalität. Ältere Anwendungen in anderen Technologien bauen wir schrittweise in Rails neu. Am Anfang steht ein technisches Audit.</p>
        {BRIEF_GET}
        <div class="row"><a class="btn" href="#kontakt">Audit anfragen</a></div>
      </div>
      <div class="leaf">
        <h2>Ablauf</h2>
        <ol class="track w-3">
          <li><span class="w">Schritt 1 · 2 Wochen</span><b>Technisches Audit</b><span class="t">Architektur, Sicherheit, Abhängigkeiten und Versionen, Testabdeckung, Performance-Engpässe und die Stellen, die oft geändert werden und schwer zu ändern sind.</span></li>
          <li><span class="w">Schritt 2</span><b>Bericht und Plan</b><span class="t">Bewertete Risiken, Empfehlung für Upgrade, Teilneubau oder Neubau und ein Plan in Meilensteinen mit Festpreis. Ihr entscheidet.</span></li>
          <li><span class="w">Schritt 3</span><b>Umsetzung in Meilensteinen</b><span class="t">Jeder Meilenstein geht einzeln live. Die Anwendung läuft während der ganzen Zeit weiter.</span></li>
        </ol>
      </div>
      <div class="leaf">
        <h2>Typische Aufgaben</h2>
        <div class="two">
          <div>{ul(["Upgrade von Rails 5, 6 oder 7 auf die aktuelle Version", "Ruby-Upgrade und Austausch veralteter Gems", "Testabdeckung dort aufbauen, wo Änderungen riskant sind"])}</div>
          <div>{ul(["Langsame Seiten und Abfragen finden und beheben", "Ältere Anwendungen, etwa in PHP oder Java, schrittweise in Rails neu bauen", "Wissen dokumentieren, das nur noch bei wenigen Personen liegt"])}</div>
        </div>
      </div>
      <div class="leaf">
        <h2>Wie der Preis entsteht</h2>
        <div class="prices">
          <div><h3>Technisches Audit</h3><span class="k">Einstieg · 2 Wochen · Festpreis</span><p>Der Preis richtet sich nach Größe und Zustand der Anwendung. Ergebnis ist ein schriftlicher Bericht mit bewerteten Risiken, Empfehlung und Plan.</p></div>
          <div><h3>Je Meilenstein</h3><span class="k">Umsetzung · Festpreis</span><p>Jeder Meilenstein hat einen eigenen Festpreis auf Basis des Audits. Danach kann die Weiterentwicklung über <a href="/rails-weiterentwicklung">Stay Fast</a> laufen.</p></div>
        </div>
        <p class="note">Einen Preisrahmen für das Audit nennen wir im ersten Gespräch.</p>
      </div>
      <div class="leaf">
        <h2>Häufige Fragen</h2>
        {faq(mod_faq)}
      </div>
    </div>
  </div>
</section>
""" + contact("Audit anfragen", "Im ersten Gespräch klären wir Umfang, Zugänge und Zeitplan.")

# ---------------------------------------------------------------- Weiterentwicklung
stay_faq = [
    ("Wie viel wird pro Monat erledigt?", "Das hängt von der Größe der Aufgaben ab. Im Bericht seht ihr jeden Monat, was erledigt wurde."),
    ("Was passiert bei einem Ausfall in Produktion?", "Bei Fehlern mit Ausfall reagieren wir am selben Arbeitstag (Montag bis Freitag, 9 bis 17 Uhr). Eine Bereitschaft rund um die Uhr bieten wir nicht an."),
    ("Können wir das später selbst übernehmen?", "Ja. Board und Deployment-Pipeline bleiben bei euch und sind dokumentiert."),
    ("Betreut ihr auch Anwendungen, die nicht in Rails gebaut sind?", "Ja. Mit KI-gestützter Entwicklung hängt weniger an der einzelnen Technologie als früher. Ob wir eure Anwendung übernehmen, klären wir vorab anhand von Code, Tests und Deployment. Neue Anwendungen bauen wir mit Ruby on Rails."),
]
stay = dict(path="/rails-weiterentwicklung", file="rails-weiterentwicklung.html", crumb="Weiterentwicklung",
            title="Wartung und Weiterentwicklung von Rails- und Webanwendungen | ai-on-rails",
            desc="Laufende Weiterentwicklung eurer Webanwendung zu einem festen Monatsbetrag: Updates, Fehlerbehebung, neue Funktionen. Rails und andere Technologien.",
            service={"name": "Wartung und Weiterentwicklung", "type": "Wartung, Support und Weiterentwicklung von Ruby-on-Rails- und Webanwendungen"}, faq=stay_faq)
stay_body = f"""
<section class="reg stay" aria-labelledby="h1">
  <div class="in grid">
    <div class="margin"><span class="name">Stay Fast</span><span class="sub">monatlich</span></div>
    <div>
      <div class="leaf">
        <h1 id="h1">Webanwendungen weiterentwickeln und betreuen</h1>
        <p class="lead">Wir übernehmen die laufende Weiterentwicklung eurer Anwendung zu einem festen Monatsbetrag: Updates, Fehlerbehebung und neue Funktionen. Ruby on Rails ist unser Schwerpunkt, andere Technologien übernehmen wir nach einer Prüfung. Ihr priorisiert, wir liefern.</p>
        {BRIEF_STAY}
        <div class="row"><a class="btn" href="#kontakt">Gespräch vereinbaren</a></div>
      </div>
      <div class="leaf">
        <h2>Was enthalten ist</h2>
        <div class="two">
          <div><h3>Jeden Monat</h3>{ul(["Sicherheits-Updates für Framework und Abhängigkeiten", "Fehlerbehebung nach eurer Priorität", "Neue Funktionen im Rahmen der vereinbarten Kapazität"])}</div>
          <div><h3>So läuft es</h3>{ul(["Ihr legt Aufgaben in einem gemeinsamen Board an.", "Wir sichten das Board jeden Arbeitstag.", "Jede Änderung prüft ein Mensch, bevor sie live geht.", "Monatlicher Bericht: erledigt, offen, Auffälligkeiten."])}</div>
        </div>
      </div>
      <div class="leaf">
        <h2>Wie der Preis entsteht</h2>
        <div class="prices">
          <div><h3>Einrichtung</h3><span class="k">Einmalig</span><p>Zugänge, Board und Deployment-Pipeline für eure Anwendung. Dabei prüfen wir Code, Tests und Deployment.</p></div>
          <div><h3>Weiterentwicklung</h3><span class="k">Monatlich · fester Betrag</span><p>Feste monatliche Kapazität, der Betrag richtet sich nach dem Umfang. Mindestlaufzeit 3 Monate, danach monatlich kündbar.</p></div>
        </div>
        <p class="note">Einen Preisrahmen nennen wir im ersten Gespräch.</p>
      </div>
      <div class="leaf">
        <h2>Häufige Fragen</h2>
        {faq(stay_faq)}
      </div>
    </div>
  </div>
</section>
""" + contact("Gespräch vereinbaren", "Wir sehen uns eure Anwendung an und sagen, welche Kapazität passt.")

# ---------------------------------------------------------------- Impressum, Datenschutz (Inhalt rechtlich, nur Layout neu)
IMPRESSUM = r"""<section>
 <h2>Angaben gemäß § 5 DDG</h2>
 <p>
 <strong>ai-on-rails</strong><br>
 Inhaber: Henning Thies<br>
 Lehmberg 7<br>
 23795 Negernbötel<br>
 Deutschland
 </p>
 </section>
 <section>
 <h2>Kontakt</h2>
 <p>
 E-Mail: <a href="mailto:hello@ai-on-rails.com">hello@ai-on-rails.com</a>
 </p>
 </section>
 <section>
 <h2>Umsatzsteuer-ID</h2>
 <p>
 Umsatzsteuer-Identifikationsnummer gemäß § 27 a Umsatzsteuergesetz:<br>
 DE351589906
 </p>
 </section>
 <section>
 <h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
 <p>
 <strong>Henning Thies</strong><br>
 Lehmberg 7<br>
 23795 Negernbötel<br>
 Deutschland
 </p>
 </section>
 <section>
 <h2>Verbraucherstreitbeilegung</h2>
 <p>
 Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer
 Verbraucherschlichtungsstelle teilzunehmen.
 </p>
 </section>
 <section>
 <h2>Haftung für Inhalte</h2>
 <p>
 Als Diensteanbieter sind wir gemäß § 7 Abs. 1 DDG für eigene Inhalte auf diesen Seiten
 nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 DDG sind wir als
 Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde
 Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige
 Tätigkeit hinweisen.
 </p>
 <p>
 Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den
 allgemeinen Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist jedoch
 erst ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei
 Bekanntwerden von entsprechenden Rechtsverletzungen werden wir diese Inhalte
 umgehend entfernen.
 </p>
 </section>
 <section>
 <h2>Haftung für Links</h2>
 <p>
 Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen
 Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen.
 Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber
 der Seiten verantwortlich.
 </p>
 <p>
 Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße
 überprüft. Rechtswidrige Inhalte waren zum Zeitpunkt der Verlinkung nicht erkennbar.
 Eine permanente inhaltliche Kontrolle der verlinkten Seiten ist jedoch ohne konkrete
 Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei Bekanntwerden von
 Rechtsverletzungen werden wir derartige Links umgehend entfernen.
 </p>
 </section>
 <section>
 <h2>Urheberrecht</h2>
 <p>
 Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen
 dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art
 der Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der schriftlichen
 Zustimmung des jeweiligen Autors bzw. Erstellers.
 </p>
 <p>
 Downloads und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen Gebrauch
 gestattet. Soweit die Inhalte auf dieser Seite nicht vom Betreiber erstellt wurden, werden
 die Urheberrechte Dritter beachtet. Sollten Sie trotzdem auf eine Urheberrechtsverletzung
 aufmerksam werden, bitten wir um einen entsprechenden Hinweis. Bei Bekanntwerden von
 Rechtsverletzungen werden wir derartige Inhalte umgehend entfernen.
 </p>
 </section>
"""
DATENSCHUTZ = r"""<p class="update-date">Stand: November 2026</p>
 <section>
 <h2>1. Verantwortlicher</h2>
 <p>
 <strong>ai-on-rails</strong><br>
 Inhaber: Henning Thies<br>
 Lehmberg 7<br>
 23795 Negernbötel<br>
 Deutschland<br>
 E-Mail: <a href="mailto:hello@ai-on-rails.com">hello@ai-on-rails.com</a>
 </p>
 </section>
 <section>
 <h2>2. Übersicht der Datenverarbeitung</h2>
 <p>
 Diese Website verarbeitet so wenige personenbezogene Daten wie möglich.
 Wir verwenden <strong>keine Cookies</strong> und <strong>keine Tracking-Dienste</strong>.
 </p>
 <p>
 Die folgenden Daten werden im Rahmen des normalen Websitebetriebs verarbeitet:
 </p>
 <ul>
 <li>Server-Logfiles (technisch notwendig)</li>
 <li>Webanalyse mit Umami (datenschutzfreundlich, ohne Cookies)</li>
 <li>E-Mail-Kommunikation (bei Kontaktaufnahme)</li>
 </ul>
 </section>
 <section>
 <h2>3. Hosting und Server-Logfiles</h2>
 <p>
 Diese Website wird bei Github Pages gehostet. Beim Besuch der
 Website werden automatisch technische Informationen in Server-Logfiles gespeichert:
 </p>
 <ul>
 <li>IP-Adresse (anonymisiert)</li>
 <li>Datum und Uhrzeit der Anfrage</li>
 <li>Aufgerufene Seite</li>
 <li>Browser-Typ und -Version</li>
 <li>Betriebssystem</li>
 </ul>
 <p>
 <strong>Rechtsgrundlage:</strong> Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse
 an der Sicherheit und Stabilität der Website).
 </p>
 <p>
 <strong>Speicherdauer:</strong> Die Logfiles werden nach 7 Tagen automatisch gelöscht.
 </p>
 </section>
 <section>
 <h2>4. Webanalyse (Umami)</h2>
 <p>
 Wir nutzen Umami, einen datenschutzfreundlichen Webanalysedienst. Umami wurde
 speziell entwickelt, um ohne Cookies und ohne Erfassung personenbezogener Daten
 zu funktionieren.
 </p>
 <p>
 Folgende anonymisierte Daten werden erhoben:
 </p>
 <ul>
 <li>Seitenaufrufe</li>
 <li>Referrer (woher Sie kamen)</li>
 <li>Gerätetype (Desktop/Mobil)</li>
 <li>Browser und Betriebssystem</li>
 <li>Land (basierend auf anonymisierter IP)</li>
 </ul>
 <p>
 <strong>Wichtig:</strong> Es werden keine Cookies gesetzt, keine IP-Adressen
 gespeichert und kein Tracking über mehrere Websites hinweg durchgeführt.
 Eine Einwilligung ist daher nicht erforderlich.
 </p>
 <p>
 <strong>Anbieter:</strong> Umami Software, Inc.
 </p>
 <p>
 <strong>Rechtsgrundlage:</strong> Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse
 an der Analyse der Websitenutzung zur Verbesserung des Angebots).
 </p>
 <p>
 <strong>Datenschutzerklärung von Umami:</strong>
 <a href="https://umami.is/privacy" target="_blank" rel="noopener">
 https://umami.is/privacy
 </a>
 </p>
 </section>
 <section>
 <h2>5. Schriftarten</h2>
 <p>
 Die Schriftarten dieser Website liegen auf demselben Server wie die Website und werden von dort geladen.
 Beim Aufruf der Seite wird keine Verbindung zu Google oder anderen Schriftanbietern aufgebaut.
 </p>
 </section>
 <section>
 <h2>6. Externe Links</h2>
 <p>
 Diese Website enthält Links zu externen Diensten:
 </p>
 <h3>Google Calendar (Terminbuchung)</h3>
 <p>
 Für die Terminbuchung nutzen wir Google Calendar. Wenn Sie auf den Link zur
 Terminbuchung klicken, werden Sie zu Google weitergeleitet. Die Datenverarbeitung
 erfolgt dann nach den Datenschutzbestimmungen von Google.
 </p>
 <p>
 <strong>Datenschutzerklärung von Google:</strong>
 <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">
 https://policies.google.com/privacy
 </a>
 </p>
 </section>
 <section>
 <h2>7. E-Mail-Kontakt</h2>
 <p>
 Wenn Sie uns per E-Mail kontaktieren, werden Ihre Angaben (E-Mail-Adresse,
 Name, Inhalt der Nachricht) zur Bearbeitung Ihrer Anfrage gespeichert.
 </p>
 <p>
 <strong>Rechtsgrundlage:</strong> Art. 6 Abs. 1 lit. b DSGVO (Vertragsanbahnung)
 bzw. Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an der Beantwortung von Anfragen).
 </p>
 <p>
 <strong>Speicherdauer:</strong> Ihre Daten werden gelöscht, sobald sie für die
 Erreichung des Zweckes ihrer Erhebung nicht mehr erforderlich sind, spätestens
 jedoch nach Ablauf gesetzlicher Aufbewahrungsfristen.
 </p>
 </section>
 <section>
 <h2>8. Ihre Rechte</h2>
 <p>
 Sie haben folgende Rechte bezüglich Ihrer personenbezogenen Daten:
 </p>
 <ul>
 <li><strong>Auskunftsrecht</strong> (Art. 15 DSGVO)</li>
 <li><strong>Recht auf Berichtigung</strong> (Art. 16 DSGVO)</li>
 <li><strong>Recht auf Löschung</strong> (Art. 17 DSGVO)</li>
 <li><strong>Recht auf Einschränkung der Verarbeitung</strong> (Art. 18 DSGVO)</li>
 <li><strong>Recht auf Datenübertragbarkeit</strong> (Art. 20 DSGVO)</li>
 <li><strong>Widerspruchsrecht</strong> (Art. 21 DSGVO)</li>
 </ul>
 <p>
 Zur Ausübung Ihrer Rechte wenden Sie sich bitte an:
 <a href="mailto:hello@ai-on-rails.com">hello@ai-on-rails.com</a>
 </p>
 </section>
 <section>
 <h2>9. Beschwerderecht</h2>
 <p>
 Sie haben das Recht, sich bei einer Datenschutz-Aufsichtsbehörde über die
 Verarbeitung Ihrer personenbezogenen Daten zu beschweren.
 </p>
 <p>
 <strong>Zuständige Aufsichtsbehörde:</strong><br>
 Unabhängiges Landeszentrum für Datenschutz Schleswig-Holstein (ULD)<br>
 Holstenstraße 98, 24103 Kiel<br>
 <a href="https://www.datenschutzzentrum.de" target="_blank" rel="noopener">www.datenschutzzentrum.de</a>
 </p>
 </section>
 <section>
 <h2>10. Änderung dieser Datenschutzerklärung</h2>
 <p>
 Wir behalten uns vor, diese Datenschutzerklärung anzupassen, um sie an geänderte
 Rechtslagen oder bei Änderungen des Dienstes anzupassen. Die aktuelle Version
 finden Sie stets auf dieser Seite.
 </p>
 </section>
"""


def legal_body(title, content):
    return f"""
<section class="reg plain legal" aria-labelledby="h1">
  <div class="in">
    <h1 id="h1">{title}</h1>
    {content}
  </div>
</section>
"""


imp_page = dict(path="/impressum", file="impressum.html", legal=True, robots="noindex, follow", title="Impressum | ai-on-rails", desc="Impressum von ai-on-rails, Henning Thies, Negernbötel.")
ds_page = dict(path="/datenschutz", file="datenschutz.html", legal=True, robots="noindex, follow", title="Datenschutzerklärung | ai-on-rails", desc="Datenschutzerklärung von ai-on-rails.")

for page, body in [(start, start_body), (bets, bets_body), (mod, mod_body), (stay, stay_body), (imp_page, legal_body("Impressum", IMPRESSUM)), (ds_page, legal_body("Datenschutzerklärung", DATENSCHUTZ))]:
    html = head(page) + body + FOOT + "" + "</body>\n</html>\n"
    (REPO / page["file"]).write_text(html, encoding="utf-8")
    print("wrote", page["file"])
