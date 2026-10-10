# Dokumenty Medyczne — Procedura i Wzory Pism (Błąd Dentysty / OC)

Repozytorium zawiera gotowe wzory pism, poradnik prawny oraz automatycznie generowane wersje do druku i edycji (**PDF** oraz **DOCX**) w sprawach dotyczących błędu diagnostycznego dentysty (np. zaniechanie na zdjęciu RTG), uzyskania dokumentacji medycznej oraz dochodzenia odszkodowania i zadośćuczynienia z obowiązkowego ubezpieczenia OC podmiotu leczniczego.

Wszystkie szablony są **zanonimizowane** — zawierają estetyczne, wykropkowane pola (`............`) gotowe do wypełnienia ręcznie lub w edytorze tekstu.

---

## 📂 Zawartość repozytorium

| Dokument | Markdown | Do druku (PDF) | Do edycji (DOCX) | Opis |
| :--- | :---: | :---: | :---: | :--- |
| **Wniosek o dokumentację medyczną i wskazanie polisy OC** | [`wniosek-dokumentacja-papierowa.md`](wniosek-dokumentacja-papierowa.md) | [Pobierz PDF](dist/wniosek-dokumentacja-papierowa.pdf) | [Pobierz DOCX](dist/wniosek-dokumentacja-papierowa.docx) | Oficjalny wniosek do gabinetu na podstawie art. 26–28 ustawy o prawach pacjenta (bezpłatna pierwsza kopia, RTG DICOM) oraz art. 14 ust. 2 pkt 2 ustawy o działalności leczniczej (dane ubezpieczyciela OC). |
| **Zgłoszenie szkody i wezwanie do zapłaty (OC)** | [`wniosek-odszkodowanie-OC-dentysty.md`](wniosek-odszkodowanie-OC-dentysty.md) | [Pobierz PDF](dist/wniosek-odszkodowanie-OC-dentysty.pdf) | [Pobierz DOCX](dist/wniosek-odszkodowanie-OC-dentysty.docx) | Kompletne zgłoszenie szkody w trybie *actio directa* (art. 822 § 4 KC) do ubezpieczyciela OC lub wezwanie do gabinetu (odszkodowanie z art. 444 § 1 zd. 2 KC + zadośćuczynienie z art. 445 § 1 KC). |
| **Poradnik prawno-praktyczny (Research)** | [`research-OC-dentysty.md`](research-OC-dentysty.md) | [Pobierz PDF](dist/research-OC-dentysty.pdf) | [Pobierz DOCX](dist/research-OC-dentysty.docx) | Omówienie zasad działania OC, sum gwarancyjnych (min. 75 000 EUR), terminów (30 dni), 3-letniego przedawnienia, ścieżek RPP, OROZ oraz kroków dowodowych. |

---

## ⚡ Jak używać?

1. **Pobierz plik DOCX** jeśli chcesz wypełnić pismo na komputerze (w programie Microsoft Word, LibreOffice Writer lub Dokumenty Google).
2. **Pobierz plik PDF** jeśli wolisz wydrukować czysty formularz i uzupełnić go odręcznie lub dołączyć jako wzór do korespondencji.
3. Wypełnij wykropkowane pola własnymi danymi, datami i kwotami popartymi rachunkami.

---

## 🤖 Automatyczna konwersja (CI/CD)

Repozytorium posiada skonfigurowany proces **GitHub Actions** (`.github/workflows/build-docs.yml`), który przy każdym commicie lub zmianie w plikach `.md`:
1. Automatycznie parsuje pliki Markdown.
2. Generuje sformatowane wersje **PDF** i **DOCX** za pomocą silnika LibreOffice / Python.
3. Publikuje wygenerowane pliki w katalogu `dist/` oraz w zakładce **GitHub Releases**.

Aby uruchomić konwersję lokalnie:
```bash
python3 convert.py
```
Pliki wyjściowe znajdą się w folderze `dist/`.

---

## ⚖️ Zastrzeżenie prawne
Materiały udostępnione w niniejszym repozytorium mają charakter wyłącznie informacyjny i edukacyjny. Nie stanowią one świadczenia pomocy prawnej ani indywidualnej porady prawnej.
