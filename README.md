# KI-lesbare Satzungen der Gemeinde Linsengericht

**Pipeline zur Umwandlung kommunaler Satzungen in maschinenlesbare Texte**

Dieses Repository dokumentiert eine vollständige technische Pipeline zur Umwandlung kommunaler Satzungen der Gemeinde Linsengericht sowie relevanter hessischer Rechtstexte (z. B. HGO) in strukturierte, maschinenlesbare Textdaten.

Neben den erzeugten Texten enthält dieses Projekt auch die **komplette Verarbeitungspipeline**, sodass der gesamte Prozess nachvollzogen und auf andere Dokumente übertragen werden kann.

Die Dokumente wurden aus teilweise gescannten oder bildbasierten PDFs mithilfe von OCR in Text überführt, bereinigt und zu einem konsistenten Datensatz zusammengeführt.

---

# Ziel des Projekts

Viele kommunale Satzungen werden online nur als PDF bereitgestellt. Diese PDFs haben häufig folgende Eigenschaften:

* gescannte Dokumente ohne Textlayer
* Bild-PDFs ohne maschinenlesbaren Text
* schlechte Durchsuchbarkeit
* komplexe Layouts

Für Menschen sind diese Dokumente gut lesbar, für Maschinen jedoch schwer nutzbar.

Ziel dieses Projekts ist daher:

* die Inhalte maschinenlesbar zu machen
* eine reproduzierbare Pipeline bereitzustellen
* kommunale Rechtstexte für KI-Anwendungen nutzbar zu machen

Die erzeugten Daten können beispielsweise genutzt werden für:

* semantische Suche über Satzungen
* KI-gestützte juristische Recherche
* Retrieval-Augmented Generation (RAG)
* Analyse kommunaler Regelwerke
* Aufbau kommunaler Wissensdatenbanken

---

# Überblick über die Verarbeitungspipeline

Die Dokumente werden in mehreren klar getrennten Schritten verarbeitet.

```text
PDF Dokumente
↓
OCR (Texterkennung)
↓
Extraktion von Rohtext
↓
Textbereinigung
↓
Strukturierung mit Metadaten
↓
Zusammenführung zu einem Datensatz
```

---

# Projektstruktur

```text
original/
    Originale PDF-Dokumente

results/

    ocr/
        durch OCR verarbeitete PDFs

    txt/
        Rohtexte aus der OCR-Erkennung

    clean/
        bereinigte Texte

    dataset.txt
        zusammengeführter Gesamtdatensatz

scripts/

    clean_txt.py
    add_header.py
    merge_all.py
```

---

# Voraussetzungen

Die Pipeline wurde unter macOS und Linux entwickelt und nutzt einfache Terminal-Werkzeuge.

Benötigte Software:

* Homebrew (macOS Paketmanager)
* Tesseract OCR
* OCRmyPDF
* Python 3

---

# Installation der benötigten Software

## 1 Homebrew installieren (nur macOS)

Homebrew ist ein Paketmanager, mit dem Software über das Terminal installiert werden kann.

Im Terminal ausführen:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Installation prüfen:

```bash
brew --version
```

---

## 2 Tesseract OCR installieren

Tesseract ist die eigentliche OCR-Engine zur Texterkennung.

Installation:

```bash
brew install tesseract
```

Installation prüfen:

```bash
tesseract --version
```

---

## 3 Sprachmodelle installieren

Für deutsche Dokumente wird das deutsche Sprachmodell benötigt.

```bash
brew install tesseract-lang
```

Verfügbare Sprachen prüfen:

```bash
tesseract --list-langs
```

Die Ausgabe sollte unter anderem enthalten:

```text
deu
eng
```

---

## 4 OCRmyPDF installieren

OCRmyPDF automatisiert die Texterkennung in PDF-Dateien.

Installation:

```bash
brew install ocrmypdf
```

Installation prüfen:

```bash
ocrmypdf --version
```

---

## 5 Python installieren

Python wird für die Verarbeitungsskripte benötigt.

Version prüfen:

```bash
python3 --version
```

Falls Python fehlt:

```bash
brew install python
```

---

# Schritt 1 – OCR durchführen und Textdateien erzeugen

Zuerst wird eine Texterkennung auf alle PDF-Dokumente angewendet.

Dabei werden gleichzeitig erzeugt:

* durchsuchbare OCR-PDFs
* Textdateien mit dem erkannten Inhalt

---

## Ordnerstruktur vorbereiten

Im Projektordner folgende Ordner anlegen:

```bash
mkdir -p results/ocr
mkdir -p results/txt
```

Danach existiert:

```text
results/
    ocr/
    txt/
```

---

## OCR für alle PDFs durchführen

Wenn sich die PDFs im aktuellen Ordner befinden, kann die OCR für alle Dateien gleichzeitig ausgeführt werden.

```bash
for f in *.pdf; do
  base="${f%.pdf}"

  ocrmypdf \
    -l deu \
    --rotate-pages \
    --deskew \
    --force-ocr \
    --sidecar "results/txt/${base}.txt" \
    "$f" "results/ocr/$f"

done
```

---

## Erklärung der wichtigsten Optionen

`-l deu`
verwendet das deutsche Sprachmodell.

`--rotate-pages`
erkennt automatisch gedrehte Seiten.

`--deskew`
richtet schiefe Scans aus.

`--force-ocr`
erzwingt OCR auch bei PDFs mit vorhandenem Textlayer.

`--sidecar`
erstellt gleichzeitig eine `.txt`-Datei mit dem erkannten Text.

---

## Ergebnis

Nach Abschluss enthält der Projektordner:

```text
results/

    ocr/
        Feuerwehrsatzung.pdf
        Gebuehrensatzung.pdf

    txt/
        Feuerwehrsatzung.txt
        Gebuehrensatzung.txt
```

---

# Schritt 2 – OCR-Text bereinigen

Die Rohtexte enthalten häufig Layout-Artefakte aus der OCR-Erkennung.

Das Script

```
scripts/clean_txt.py
```

bereinigt diese automatisch.

Es führt u. a. folgende Schritte aus:

* Normalisierung von Zeilenumbrüchen
* Zusammenführen von Worttrennungen
* Reduktion mehrfacher Leerzeichen
* Vereinheitlichung von Absätzen

Ausführen:

```bash
python3 scripts/clean_txt.py
```

Ergebnis:

```text
results/clean/
```

---

# Schritt 3 – Metadaten ergänzen

Um Dokumente leichter identifizieren zu können, werden Metadaten ergänzt.

Script:

```
scripts/add_header.py
```

Ausführen:

```bash
python3 scripts/add_header.py
```

Beispielstruktur eines Dokuments:

```text
DOCUMENT: Feuerwehrsatzung
SOURCE: Feuerwehrsatzung.pdf
LANGUAGE: de

CONTENT

...
```

---

# Schritt 4 – Datensatz erstellen

Alle bereinigten Texte werden anschließend zu einem Gesamtdatensatz zusammengeführt.

Script:

```
scripts/merge_all.py
```

Ausführen:

```bash
python3 scripts/merge_all.py
```

Ergebnis:

```text
results/dataset.txt
```

Diese Datei enthält alle Dokumente in sequenzieller Form.

---

# Verwendung der erzeugten Daten

Der erzeugte Datensatz kann verwendet werden für:

* semantische Suche über Satzungen
* juristische Textanalyse
* KI-gestützte Recherche
* Aufbau kommunaler Wissensdatenbanken
* RAG-basierte Chatbots

---

# Transparenzhinweis

Die Inhalte basieren auf öffentlich zugänglichen Dokumenten.

Dieses Repository stellt **keine amtliche Veröffentlichung** dar.
Für rechtsverbindliche Fassungen sind die offiziellen Veröffentlichungen der Gemeinde bzw. des Landes Hessen maßgeblich.

---

# Hintergrund

Viele öffentliche Dokumente sind zwar frei zugänglich, aber technisch nur eingeschränkt nutzbar.

Dieses Projekt zeigt exemplarisch, wie solche Dokumente mit einfachen Werkzeugen in strukturierte Textdaten überführt werden können, die für moderne Analyse- und KI-Anwendungen geeignet sind.
