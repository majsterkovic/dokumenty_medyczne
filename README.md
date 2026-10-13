# Plan sprawy pacjentki — nawrót torbieli po kontroli CBCT

Repozytorium zawiera poradnik dotyczący konkretnej sprawy nawrotu torbieli po wcześniejszym leczeniu, listę zadań, historię pacjentki, wzory pism, materiały prawne oraz wersje do druku i edycji (**PDF** i **DOCX**). Główne zagadnienie do wyjaśnienia to to, czy nawrót torbieli był widoczny na CBCT z 04.08.2026 i czy opóźnienie rozpoznania spowodowało dalszą szkodę. Materiały nie przesądzają, że doszło do błędu.

Ogólne szablony są zanonimizowane i zawierają wykropkowane pola (`............`). Historia oraz wersja robocza opisują przypadek pacjentki, choć nie podają jej bezpośrednich danych identyfikacyjnych.

**Prywatność:** informacje o zdrowiu są danymi wrażliwymi. Przed publikacją lub wysłaniem repozytorium do publicznego serwisu (w tym GitHub) sprawdź, czy chcesz udostępnić historię i robocze materiały tej sprawy.

---

## 📂 Zawartość repozytorium

### Zacznij tutaj

- [Poradnik sprawy — strona HTML](poradnik-sprawy.html): chronologia, stan dowodów, kolejność działań i podstawy prawne.
- [Plan postępowania — lista zadań](PLAN-POSTEPOWANIA.md): checklista do odhaczania i rejestr korespondencji.
- [Historia pacjentki](notatki-przypadek.md): relacja źródłowa i uporządkowana chronologia.

| Dokument | Markdown | Do druku (PDF) | Do edycji (DOCX) | Opis |
| :--- | :---: | :---: | :---: | :--- |
| **Wniosek o dokumentację medyczną i wskazanie polisy OC** | [`wniosek-dokumentacja-papierowa.md`](wniosek-dokumentacja-papierowa.md) | [Pobierz PDF](dist/wniosek-dokumentacja-papierowa.pdf) | [Pobierz DOCX](dist/wniosek-dokumentacja-papierowa.docx) | Oficjalny wniosek do gabinetu na podstawie art. 26–28 ustawy o prawach pacjenta (bezpłatna pierwsza kopia, RTG DICOM) oraz art. 14 ust. 2 pkt 2 ustawy o działalności leczniczej (dane ubezpieczyciela OC). |
| **Zgłoszenie szkody i roszczeń** | [`wniosek-odszkodowanie-OC-dentysty.md`](wniosek-odszkodowanie-OC-dentysty.md) | [Pobierz PDF](dist/wniosek-odszkodowanie-OC-dentysty.pdf) | [Pobierz DOCX](dist/wniosek-odszkodowanie-OC-dentysty.docx) | Ogólny szablon do uzupełnienia. Bezpośrednie roszczenie z art. 822 § 4 KC jest kierowane do ubezpieczyciela; wariant do placówki wymaga wskazania podstawy jej odpowiedzialności. |
| **Robocze zgłoszenie tej sprawy** | [`wniosek-odszkodowanie-OC-dentysty-ROBOCZY.md`](wniosek-odszkodowanie-OC-dentysty-ROBOCZY.md) | — | — | Chronologia i neutralne sformułowanie podejrzenia. Nie wysyłać bez uzupełnienia dokumentacji i danych. |
| **Poradnik prawny** | [`research-OC-dentysty.md`](research-OC-dentysty.md) | [Pobierz PDF](dist/research-OC-dentysty.pdf) | [Pobierz DOCX](dist/research-OC-dentysty.docx) | Prawo do dokumentacji, dowody, OC, terminy i ograniczenia w ocenie odpowiedzialności. |

### 📚 Akty prawne (pełne teksty jednolite)

Katalog [`ustawy/`](ustawy/) zawiera pełne teksty jednolite 5 ustaw cytowanych we wnioskach (PDF + TXT do wyszukiwania). Pobrane z oficjalnego API Sejmu (`api.sejm.gov.pl`). Lista z cytowaniami artykułów: [`ustawy/README.md`](ustawy/README.md).

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
Materiały mają charakter informacyjny i organizacyjny. Nie stanowią indywidualnej porady prawnej ani medycznej. Fakty w historii pochodzą z relacji pacjentki; istotne elementy wymagają potwierdzenia dokumentacją.
