# Lekcja 001 — pierwszy program

## Czego się nauczysz

- czym jest program i jak uruchomić plik Pythona;
- jak funkcja `print()` wyświetla tekst;
- jak zapisać tekst w cudzysłowie.

## Uruchomienie

Z katalogu głównego repozytorium:

```powershell
python 01_PYTHON\001_PIERWSZY_PROGRAM\lekcja_001.py
```

Program wypisuje trzy komunikaty w terminalu. Każde wywołanie `print()` tworzy osobny wiersz.

## Ćwiczenia

1. Uruchom program i porównaj wynik z kodem.
2. Zmień pierwszy komunikat na własne powitanie.
3. Dodaj kolejne wywołanie `print()` opisujące swój cel nauki.
4. Uruchom test. Jeśli zmienisz tekst w programie, zaktualizuj też oczekiwany wynik w teście.

## Sprawdzenie

```powershell
python -m unittest discover -s 01_PYTHON\001_PIERWSZY_PROGRAM -p "test_*.py" -v
```

## Słowniczek

- **Program** — instrukcje, które komputer wykonuje.
- **Funkcja** — nazwany element programu wykonujący określone działanie.
- **Terminal** — tekstowy interfejs do uruchamiania poleceń i programów.
