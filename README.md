# Wyciskarka Max

Skill dla Codexa, Claude Code i Antigravity. Analizuje projekt i przygotowuje interaktywną mapę HTML z terminami konkursów, konferencji, grantów i pilotaży. Przy każdej okazji podaje źródło, termin i ocenę gotowości projektu.

## Instalacja globalna

```sh
npx skills add MichalGudowicz29/wyciskarka-max -g -a codex claude-code antigravity
```

Agent zapisuje profil, postęp i pojedyncze rekordy w lokalnym katalogu `.wyciskarka/`. Przy kolejnym uruchomieniu może wznowić poszukiwania albo wygenerować mapę z zapisanych danych. Kolumny przedstawiają miesiące, karty grupują się według zakresu dopracowania, a panel filtruje typ okazji i finansowanie. Kliknij kartę, aby zobaczyć wymagania, datę sprawdzenia i źródła.

Do wyszukiwania potrzebny jest internet, do eksportu Python 3. Gotowy `mapa-okazji.html` otwiera się w przeglądarce offline. Szablon jest dołączony do skilla.

## Instalacja z pobranego repozytorium

W katalogu zawierającym ten plik uruchom:

```sh
npx skills add . -g -a codex claude-code antigravity
```

Otwórz rozmowę w katalogu wybranego projektu i wpisz `$wyciskarka-max` w Codexie lub `/wyciskarka-max` w Claude Code. W Antigravity poproś: „Użyj skilla wyciskarka-max dla tego projektu”.
