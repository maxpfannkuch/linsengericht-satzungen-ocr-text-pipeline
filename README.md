# Linsengericht Satzungen – KI-lesbare kommunale Rechtstexte

Dieses Repository enthält maschinenlesbare Versionen kommunaler Satzungen der Gemeinde Linsengericht sowie ausgewählter hessischer Rechtstexte (z. B. HGO).

Die Dokumente wurden aus bildbasierten PDFs mittels OCR verarbeitet und anschließend bereinigt, strukturiert und zu einem KI-freundlichen Datensatz zusammengeführt.

Ziel ist es, kommunale Rechtsdokumente leichter zugänglich und für moderne Technologien wie semantische Suche, Retrieval-Augmented Generation (RAG) und KI-gestützte Analyse nutzbar zu machen.

---

# Motivation

Viele kommunale Satzungen werden online ausschließlich als PDF bereitgestellt.

Diese PDFs sind häufig:

* gescannte Dokumente
* Bild-PDFs ohne Textlayer
* nur begrenzt durchsuchbar
* für KI-Systeme schwer interpretierbar

Dadurch entstehen mehrere Probleme:

* Inhalte sind nicht zuverlässig maschinenlesbar
* automatische Analyse ist kaum möglich
* KI-gestützte Recherche funktioniert schlecht

Durch eine OCR-Pipeline wurden diese Dokumente daher in sauberen Text überführt.

---

# Inhalt des Repositorys

```
original/
    Original PDFs der Satzungen und Rechtstexte

results/
    clean/
        bereinigte KI-optimierte Einzeltexte

    txt/
        Roh-OCR-Texte

    ocr/
        OCR-PDF Versionen

    dataset.txt
        Gesamtdatensatz aller Dokumente

scripts/
    clean_txt.py
    add_header.py
    merge_all.py

README.md
```

---

# Verarbeitungspipeline

Die Dokumente wurden mit folgender Pipeline verarbeitet.

## 1 OCR der PDF-Dokumente

Werkzeuge:

* Tesseract
* OCRmyPDF

Ziel:

* Bild-PDF → durchsuchbares OCR-PDF
* Textlayer erzeugen

---

## 2 Extraktion des Textes

Aus den OCR-PDFs wurden Textdateien erzeugt.

Ergebnis:

```
txt/
```

Diese Dateien enthalten den Roh-OCR-Text.

---

## 3 Textbereinigung

Das Script

```
scripts/clean_txt.py
```

führt folgende Schritte aus:

* Zeilenumbrüche normalisieren
* OCR-Trennungen zusammenführen
* Mehrfach-Leerzeichen reduzieren
* Absätze strukturieren

Ergebnis:

```
results/clean/
```

---

## 4 Dokumentstruktur hinzufügen

Script:

```
scripts/add_header.py
```

Ergänzt pro Datei Metadaten:

```
DOCUMENT:
SOURCE:
LANGUAGE:
```

---

## 5 Zusammenführung zu einem Gesamtdatensatz

Script:

```
scripts/merge_all.py
```

Erzeugt:

```
results/dataset.txt
```

Diese Datei enthält alle Dokumente als zusammenhängenden KI-Datensatz.

---

# Nutzung

Die Daten können verwendet werden für:

* KI-Recherche zu kommunalen Satzungen
* semantische Suche
* RAG-Systeme
* juristische Analyse
* kommunale Wissensdatenbanken

---

# Transparenz

Die Inhalte stammen aus öffentlich zugänglichen Quellen.

Dieses Repository stellt **keine amtliche Fassung** dar, sondern eine maschinenlesbare Aufbereitung.

Für rechtsverbindliche Fassungen sind die offiziellen Veröffentlichungen maßgeblich.

---

# Ziel des Projekts

Dieses Projekt zeigt exemplarisch, wie kommunale Rechtsdokumente technisch aufbereitet werden können, um:

* demokratische Transparenz zu erhöhen
* öffentliche Dokumente besser zugänglich zu machen
* moderne KI-Werkzeuge für kommunale Informationen nutzbar zu machen
