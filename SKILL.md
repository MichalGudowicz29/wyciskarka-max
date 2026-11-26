---
name: wyciskarka-max
description: Wyszukuje okazje dla konkretnego projektu, zapisuje postęp i tworzy interaktywną mapę HTML z terminami, źródłami, finansowaniem i wymaganiami. Użyj również do wznowienia lub odświeżenia wcześniejszej kwerendy.
---

# Wyciskarka Max

## Zacznij od zapisanego stanu

Pracuj w katalogu wskazanego projektu. Stan lokalny to `.wyciskarka/`. Na początek sprawdź tylko `project.json` i krótki `progress.md`. Zapisuj zmiany po każdej sprawdzonej grupie źródeł, również przed przerwą. Nie wysyłaj prywatnego profilu do wyszukiwarek ani nie publikuj stanu.

- **Pierwszy raz:** przeczytaj README i tylko te przykłady, wyniki lub fragmenty implementacji, które rozstrzygają, co działa. W `project.json` zachowaj krótki profil, lokalizację, ograniczenia oraz ścieżki dowodów i rewizję Git lub daty plików. Domyślny horyzont to 12 miesięcy. Poprzedni PDF lub kalendarz może dostarczyć tropów do sprawdzenia.
- **Wznowienie:** zacznij od ostatniego punktu w `progress.md`. Trzymaj w nim zakres, sprawdzone kategorie i obszary geograficzne, luki, odrzucone lub zamknięte ścieżki z powodem, otwarte tropy oraz następny krok. Aktualizuj podsumowanie w miejscu. Porównaj stan plików dowodowych, także lokalne zmiany, i czytaj wyłącznie różnice ważne dla profilu.
- **Odświeżenie:** wydrukuj krótki indeks rekordów (komenda poniżej); ogranicz wynik do potrzebnych wierszy. Otwieraj pojedyncze rekordy. Najpierw sprawdź wygasające terminy, zmiany edycji, luki i niepotwierdzone statusy. Przy zachowanym rekordzie pozostaw rzeczywistą datę weryfikacji. Po terminie sprawdź przedłużenie albo przenieś rekord do `archive/` z powodem w postępie. Nie nadawaj dawnym wynikom statusu świeżo sprawdzonych.
- **Zmiana układu, filtrów albo sam eksport:** użyj istniejącego stanu bez kwerendy. Nie wczytuj gotowego HTML ani szablonu do kontekstu. Wyniki wyszukiwania przeglądaj krótkimi partiami; wyciągaj fragment regulaminu potrzebny dla konkretnej decyzji. Jedno źródło może obsłużyć kilka ścieżek. Wznawianie ma ograniczać powtórzenia, bez limitu liczby okazji.

## Co trafia na mapę

Szukaj lokalnie, krajowo i międzynarodowo, po polsku lub w języku regionu oraz po angielsku. Dla każdego udokumentowanego wyniku zmieniaj odbiorcę, zastosowanie i formę: konkurs, poster, demo, publikacja, hackathon, grant, stypendium, akcelerator, pilotaż miejski lub firmowy. Uwzględnij małe nabory, poboczne sesje i wsparcie wyjazdowe. Przy firmie wskaż publiczną drogę wejścia. Rejestruj luki w pokryciu. Nie ograniczaj wyników do rankingu.

Każda ścieżka potrzebuje konkretnego związku z projektem i źródła organizatora. Agregator służy do odkrycia źródła. Otwórz regulamin danej edycji; sprawdź rodzaj terminu, godzinę i strefę (jeśli opublikowane), status, uprawnionych, koszt, wymagany rezultat i formę zgłoszenia. Przy osobnych decyzjach (abstrakt, grant wyjazdowy) utwórz osobne rekordy. Oficjalne przedłużenie lub odwołanie ma pierwszeństwo. Przyszła konferencja nie otwiera zamkniętego CFP. Sprzeczne nierozstrzygnięte daty zapisz obie w szczegółach ze źródłami, bez daty sortowania. Ustaw status niepotwierdzony, gdy organizator nie określa dostępności.

Ścieżki bez daty, ciągłe i warunkowe również trafiają na mapę. Dla nieogłoszonej edycji wymagaj udokumentowanego cyklu, wpisz „cykliczne · kolejna edycja niepotwierdzona” i przytocz dowód. Nie przenoś dat, kwot ani zasad z poprzedniej edycji. Gdy źródła są niedostępne, odnotuj lukę; nie wnioskuj z tego o braku okazji.

Bariera formalna nigdy nie usuwa tematycznie pasującej ścieżki. W polu barier podaj kto może aplikować, warunek (np. spółka na określonym etapie albo uczelnia) i czy oficjalnie przewidziano rolę autora. Odróżnij nieznaną kwalifikację od potwierdzonego wykluczenia w tej edycji. Nie zakładaj, że afiliacja wystarczy.

Oceń dopracowanie niezależnie od formalności: **Nie wymaga** przy dowodach dla wszystkich obowiązkowych kryteriów merytorycznych, **Trochę** przy ograniczonym uzupełnieniu, **Bardzo** przy nowym istotnym wyniku, **Brak danych** przy niewystarczających dowodach. Formularz i abstrakt to praca nad zgłoszeniem. W szczegółach nazwij istniejący dowód oraz brakujący aspekt i pytanie, na które projekt musi odpowiedzieć. Zostaw wybór rozwiązania autorowi. Pomiń rekomendacje i szacunki roboczogodzin.

**Pieniądze** dotyczą konkretnej ścieżki. „Tak” wymaga źródła potwierdzającego świadczenie; podaj rodzaj, walutę, limit lub pulę oraz beneficjenta, albo „kwota niepodana”. Przy inwestycji podaj warunki. „Nie” i „–” tylko dla potwierdzonego braku wypłaty lub wyłącznie rzeczowej korzyści. Milczenie organizatora to „Brak danych”. Koszt uczestnictwa opisz osobno.

## Zapis i eksport

`project.json` zawiera publiczne pola `project`, `period` i opcjonalne `coverage` (data raportu, luki lub zakres aktualizacji). Pozostałe pola profilu są prywatne. W `records/` trzymaj jeden JSON na ścieżkę, z trwałą nazwą pliku według organizatora, edycji i ścieżki. Aktualizuj tylko zmienione rekordy. Zapisuj kompletne pliki, przy aktualizacji zastępuj je atomowo. Przykład formatu (dane ilustracyjne):

```json
{"name":"Grant pilotażowy","type":"Grant","date":"2027-02-01","dateKind":"wniosek","status":"otwarty","fit":"Trochę","money":"Tak","amount":"do 20 000 PLN dla instytucji","facts":"Prototyp działa. Wymagany jest dowód użycia w terenie. Jakie wyniki wykazuje pilotaż?","barrier":"Tylko uczelnie. Rola autora nieokreślona.","links":["https://example.org/call"],"checked":"2026-11-26"}
```

`date` to oficjalna data ISO albo null, `dateKind` określa rodzaj terminu. Godzinę i strefę dodaj w `dateKind`. Zachowaj spójne nazwy kategorii. `facts` to najwyżej kilka rzeczowych zdań ze statusem projektu, wymaganiami i kosztami. Podaj klikalne źródła do poszczególnych twierdzeń.

Uruchom dołączony skrypt z katalogu projektu. Zastąp SKILL_DIR rzeczywistym katalogiem tego SKILL.md. Python 3, bez instalowania bibliotek. Pierwsza komenda wyświetla indeks; druga generuje samodzielny raport offline. Przy kolejnym eksporcie użyj tej samej ścieżki dedykowanego raportu.

```sh
python3 "SKILL_DIR/scripts/map.py" .wyciskarka
python3 "SKILL_DIR/scripts/map.py" .wyciskarka mapa-okazji.html
```

Oddaj link do HTML i wskaż zapisany stan do wznowienia. Na końcu odpowiedzi dodaj gotową do wklejenia komendę z rzeczywistą bezwzględną ścieżką pliku. Użyj `open` na macOS, `xdg-open` na Linuksie lub `Start-Process -FilePath` w PowerShell na Windows. Zacytuj ścieżkę zgodnie z używaną powłoką. Raport można przesłać jako jeden plik. Nie wysyłaj zgłoszeń i nie ustawiaj monitoringu bez osobnej prośby.
