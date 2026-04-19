# KI-lesbare Satzungen der Gemeinde Linsengericht

**Pipeline zur Umwandlung kommunaler PDF-Satzungen in maschinenlesbare Texte**

Dieses Repository enthält eine technisch aufbereitete Version kommunaler Satzungen der Gemeinde Linsengericht sowie ausgewählter hessischer Rechtstexte (z. B. HGO).

Die Dokumente wurden aus PDF-Dateien – teilweise gescannt oder bildbasiert – in strukturierte Textdateien überführt. Ziel ist es, diese Dokumente **für moderne Such- und KI-Systeme zugänglich zu machen**.

Das Repository enthält sowohl:

* die **verarbeiteten Texte**
* als auch die **Pipeline**, mit der diese erzeugt wurden.

Damit kann der gesamte Prozess nachvollzogen und auf andere Dokumente angewendet werden.

---

# Ziel des Projekts

Viele kommunale Satzungen werden öffentlich nur als PDF bereitgestellt.

Diese PDFs sind häufig:

* gescannte Dokumente
* Bild-PDFs ohne Textlayer
* schwer durchsuchbar
* für Computer schwer auswertbar

Für Menschen sind sie lesbar – für Maschinen jedoch oft nicht.

Dieses Projekt zeigt, wie solche Dokumente in **maschinenlesbare Textdaten** überführt werden können.

Die erzeugten Texte können beispielsweise genutzt werden für:

* KI-gestützte Recherche über Satzungen
* semantische Suche
* Retrieval-Augmented-Generation (RAG)
* Analyse kommunaler Regelwerke
* Aufbau kommunaler Wissensdatenbanken

---

# Überblick über die Verarbeitungspipeline

Die Dokumente werden in mehreren Schritten verarbeitet:

```
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

```
original/
    Originale PDF-Dokumente

results/
    ocr/
        durch OCR verarbeitete PDFs

    txt/
        Rohtexte aus der OCR-Erkennung

    clean/
        bereinigte und strukturierte Texte

    dataset.txt
        zusammengeführter Gesamtdatensatz aller Dokumente

scripts/
    clean_txt.py
    add_header.py
    merge_all.py

README.md
```

---

# Voraussetzungen

Für die Verarbeitung werden einige Programme benötigt.

Dieses Projekt wurde unter **macOS / Linux** mit einem Terminal verwendet.

Benötigte Software:

* Homebrew (Paketmanager)
* Tesseract OCR
* OCRmyPDF
* Python 3

---

# Installation der benötigten Software

## 1 Homebrew installieren (macOS)

Homebrew ist ein Paketmanager für macOS.

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

Tesseract ist die eigentliche OCR-Engine.

Installation:

```bash
brew install tesseract
```

Prüfen:

```bash
tesseract --version
```

---

## 3 Sprachpakete installieren

Für deutsche Dokumente:

```bash
brew install tesseract-lang
```

Danach prüfen:

```bash
tesseract --list-langs
```

Die Ausgabe sollte unter anderem enthalten:

```
deu
eng
```

---

## 4 OCRmyPDF installieren

OCRmyPDF automatisiert die OCR-Verarbeitung von PDFs.

Installation:

```bash
brew install ocrmypdf
```

Prüfen:

```bash
ocrmypdf --version
```

---

## 5 Python installieren (falls nötig)

Prüfen:

```bash
python3 --version
```

Falls Python fehlt:

```bash
brew install python
```

---

# Schritt 1 – OCR der PDF-Dokumente

Zunächst wird auf die PDFs eine Texterkennung angewendet.

Beispiel für eine Datei:

```bash
ocrmypdf -l deu input.pdf output.pdf
```

Parameter:

```
-l deu
```

bedeutet:

```
Sprache: Deutsch
```

---

## OCR für einen ganzen Ordner

Wenn viele PDFs vorhanden sind:

```bash
for f in *.pdf; do
  ocrmypdf -l deu "$f" "ocr_$f"
done
```

Dadurch entstehen OCR-Versionen der PDFs.

Diese liegen im Ordner:

```
results/ocr/
```

---

# Schritt 2 – Text aus PDFs extrahieren

Aus den OCR-PDFs wird anschließend der Text extrahiert.

Ergebnis:

```
results/txt/
```

Diese Dateien enthalten den **Rohtext der OCR-Erkennung**.

Typische Eigenschaften:

* Layoutbedingte Zeilenumbrüche
* OCR-bedingte Worttrennungen
* ungleichmäßige Leerzeichen

---

# Schritt 3 – Textbereinigung

Der Rohtext wird mit einem Python-Script bereinigt.

Script:

```
scripts/clean_txt.py
```

Dieses Script:

* normalisiert Zeilenumbrüche
* entfernt OCR-bedingte Worttrennungen
* reduziert Leerzeichen
* erzeugt konsistente Absätze

Ausführen:

```bash
python3 scripts/clean_txt.py
```

Ergebnis:

```
results/clean/
```

---

# Schritt 4 – Metadaten ergänzen

Um Dokumente später leichter identifizieren zu können, werden Metadaten ergänzt.

Script:

```
scripts/add_header.py
```

Ausführen:

```bash
python3 scripts/add_header.py
```

Beispielstruktur eines Dokuments:

```
DOCUMENT: Feuerwehrsatzung
SOURCE: Feuerwehrsatzung.pdf
LANGUAGE: de

CONTENT

...
```

---

# Schritt 5 – Datensatz erzeugen

Alle Texte werden anschließend zu einem Gesamtdatensatz zusammengeführt.

Script:

```
scripts/merge_all.py
```

Ausführen:

```bash
python3 scripts/merge_all.py
```

Ergebnis:

```
results/dataset.txt
```

Diese Datei enthält alle Dokumente in sequenzieller Form.

---

# Verwendung der erzeugten Texte

Die erzeugten Texte können beispielsweise verwendet werden für:

* KI-gestützte Recherche über Satzungen
* semantische Dokumentensuche
* juristische Textanalyse
* RAG-Systeme
* kommunale Wissensdatenbanken

---

# Transparenzhinweis

Die Inhalte basieren auf öffentlich zugänglichen Dokumenten.

Dieses Repository stellt **keine amtliche Veröffentlichung** dar.
Für rechtsverbindliche Fassungen sind die offiziellen Veröffentlichungen der Gemeinde bzw. des Landes Hessen maßgeblich.

---

# Hintergrund

Viele öffentliche Dokumente sind zwar zugänglich, aber technisch schwer nutzbar.

Dieses Projekt zeigt, wie solche Dokumente mit einfachen Werkzeugen in strukturierte Textdaten überführt werden können, die für moderne Analyse- und KI-Anwendungen geeignet sind.
