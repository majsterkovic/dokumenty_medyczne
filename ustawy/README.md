# Akty prawne — teksty jednolite (źródła)

Pełne teksty jednolite ustaw cytowanych we wnioskach i researchu, pobrane z oficjalnego API Sejmu (`api.sejm.gov.pl`). Pliki `.txt` to konwersja `pdftotext` z PDF-ów Kancelarii Sejmu — nadają się do odczytu przez agenty AI i wyszukiwania frazami (np. „Art. 822 § 4").

## Spis plików

| # | Akt prawny | Dz.U. (t.j.) | Stan prawny | Pliki |
|---|-----------|-------------|-------------|-------|
| 01 | Ustawa z 6.11.2008 r. o prawach pacjenta i Rzeczniku Praw Pacjenta | Dz.U. 2024 poz. 581 | 27.03.2024 | `.txt` (125 KB), `.pdf` (791 KB) |
| 02 | Ustawa z 15.04.2011 r. o działalności leczniczej | Dz.U. 2026 poz. 156 | 05.02.2026 | `.txt` (253 KB), `.pdf` (1,3 MB) |
| 03 | Ustawa z 22.05.2003 r. o ubezpieczeniach obowiązkowych, UFG i PBUK | Dz.U. 2026 poz. 783 | 27.05.2026 | `.txt` (256 KB), `.pdf` (1,2 MB) |
| 04 | Ustawa z 23.04.1964 r. – Kodeks cywilny | Dz.U. 2026 poz. 795 | 19.05.2026 | `.txt` (535 KB), `.pdf` (1,2 MB) |
| 05 | Ustawa z 5.12.1996 r. o zawodach lekarza i lekarza dentysty | Dz.U. 2026 poz. 37 | 03.12.2025 | `.txt` (528 KB), `.pdf` (2,3 MB) |

## Kluczowe artykuły dla sprawy (błąd dentysty / OC)

### 01 — Prawa pacjenta
- **Art. 26** — prawo do dokumentacji medycznej
- **Art. 27** — formy udostępnienia dokumentacji
- **Art. 28** — zasady opłat; pierwsze udostępnienie w żądanym zakresie i ustawowo wskazanych formach jest bezpłatne. Dokumentację udostępnia się bez zbędnej zwłoki; ustawa nie ustanawia ogólnego terminu 14 dni roboczych.

### 02 — Działalność lecznicza
- **Art. 14 ust. 2 pkt 2** — obowiązek podania danych ubezpieczyciela OC i nr polisy
- **Art. 25** — obowiązek i podstawowy zakres OC; minimalna suma gwarancyjna wynika z rozporządzenia wykonawczego i zależy od rodzaju podmiotu

### 03 — Ubezpieczenia obowiązkowe
- **Art. 14 ust. 1** — 30 dni na wypłatę odszkodowania przez ubezpieczyciela

### 04 — Kodeks cywilny
- **Art. 822 § 4** — direct action poszkodowanego wobec ubezpieczyciela OC
- **Art. 444 § 1** — koszty leczenia (zdanie 1) / wyłożenie z góry sumy (zdanie 2)
- **Art. 445 § 1** — zadośćuczynienie za ból i cierpienia
- **Art. 819 § 4 KC** — przerwanie przedawnienia roszczenia o świadczenie wobec ubezpieczyciela po zgłoszeniu roszczenia lub zdarzenia
- **Art. 442¹** — 3-letni termin przedawnienia

### 05 — Zawody lekarza i lekarza dentysty
- **Art. 8** — granice wykonywania zawodu

## Źródła pobrania

Pobrano 13.10.2026 z API Kancelarii Sejmu:

```
https://api.sejm.gov.pl/eli/acts/DU/2024/581/text.pdf  # prawa pacjenta
https://api.sejm.gov.pl/eli/acts/DU/2026/156/text.pdf  # działalność lecznicza
https://api.sejm.gov.pl/eli/acts/DU/2026/783/text.pdf  # ubezpieczenia obowiązkowe
https://api.sejm.gov.pl/eli/acts/DU/2026/795/text.pdf  # Kodeks cywilny
https://api.sejm.gov.pl/eli/acts/DU/2026/37/text.pdf   # zawody lekarza/dentysty
```

Wyszukiwarka aktów: [ISAP](https://isap.sejm.gov.pl) · [ELI](https://eli.gov.pl)

## Uwagi

- Teksty są **pełne** (nie wyciągi) — zawierają wszystkie artykuły i załączniki.
- Pliki `.txt` zawierają znaki diakrytyczne polskie (UTF-8).
- Przy cytowaniu w pismach urzędowych odwołuj się do **Dz.U.** (np. „Dz.U. 2026 poz. 783"), nie do plików w tym repozytorium.
- Teksty jednolite mogą być nieaktualne po kolejnych nowelizacjach — przed wysłaniem pisma zweryfikuj aktualność na [eli.gov.pl](https://eli.gov.pl).
