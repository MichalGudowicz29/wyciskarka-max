# Wyciskarka Max

Skill dla Codexa, Claude Code i Antigravity. Analizuje projekt i przygotowuje PDF z kalendarzem konkursów, konferencji, grantów i pilotaży. Przy każdej okazji podaje źródło, termin i ocenę gotowości projektu.

## Instalacja globalna

```sh
npx skills add MichalGudowicz29/wyciskarka-max -g -a codex claude-code antigravity
```

Do przygotowania kalendarza agent potrzebuje dostępu do źródeł w internecie i narzędzia do zapisu PDF.

## Instalacja z pobranego repozytorium

W katalogu zawierającym ten plik uruchom:

```sh
npx skills add . -g -a codex claude-code antigravity
```

Otwórz rozmowę w katalogu wybranego projektu i wpisz `$wyciskarka-max` w Codexie lub `/wyciskarka-max` w Claude Code. W Antigravity poproś: „Użyj skilla wyciskarka-max dla tego projektu”.
