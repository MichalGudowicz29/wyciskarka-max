# Wyciskarka Max

Skill dla Codexa i Claude Code. Analizuje projekt i przygotowuje PDF z kalendarzem konkursów, konferencji, grantów i pilotaży. Przy każdej okazji podaje źródło, termin i ocenę gotowości projektu.

## Instalacja globalna

```sh
npx skills add MichalGudowicz29/wyciskarka-max -g -a codex claude-code
```

Do przygotowania kalendarza agent potrzebuje dostępu do źródeł w internecie i narzędzia do zapisu PDF.

## Instalacja z pobranego repozytorium

W katalogu zawierającym ten plik uruchom:

```sh
npx skills add . -g -a codex claude-code
```

Otwórz rozmowę w katalogu wybranego projektu i wpisz `$wyciskarka-max` w Codexie albo `/wyciskarka-max` w Claude Code.
