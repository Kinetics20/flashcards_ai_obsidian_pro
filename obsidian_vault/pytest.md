Created: 2025-02-05 15:29

---
Note:

`pytest` to popularne narzędzie do testowania w pythonie , które umożliwia łatwe pisanie, organizowanie i uruchamianie testów jednostkowych oraz funkcjonalnych. Obsługuje automatyczne wykrywanie testów, parametryzację, asercje oraz pluginy rozszerzające jego funkcjonalność.

[[pytest-cov]]

---
Metadata:

Status: #pending
Tags: #python #test #pytest #unit_tests

| Polecenie                         | Opis                                                  |
|------------------------------------|------------------------------------------------------|
| `pytest`                           | Uruchomienie wszystkich testów w katalogu.          |
| `pytest test_example.py`           | Uruchomienie testów w określonym pliku.             |
| `pytest -k "test_name"`            | Uruchomienie testów pasujących do wzorca.           |
| `pytest -m "marker"`               | Uruchomienie testów oznaczonych danym markerem.     |
| `pytest -q`                        | Cichy tryb (minimalny output).                      |
| `pytest -v`                        | Szczegółowy tryb (więcej informacji o testach).     |
| `pytest -vv`                       | Jeszcze bardziej szczegółowy tryb (`-v` + więcej logów). |
| `pytest -s`                        | Wyświetlenie `print()` i `stdout` w konsoli.        |
| `pytest --maxfail=2`               | Przerwanie testów po dwóch błędach.                 |
| `pytest --tb=short`                | Skrócony traceback dla błędów.                      |
| `pytest --disable-warnings`        | Wyłączenie ostrzeżeń w wynikach testów.             |
| `pytest --cov=my_module`           | Uruchomienie testów z pokryciem kodu (`pytest-cov`). |
| `pytest --junitxml=report.xml`     | Zapis wyników w formacie JUnit XML.                 |
| `pytest --last-failed`             | Uruchomienie tylko ostatnich nieudanych testów.     |
| `pytest --lf`                      | Skrócona wersja `--last-failed`.                    |
| `pytest --durations=5`             | Wyświetlenie 5 najwolniejszych testów.              |
| `pytest --pdb`                     | Debugowanie testów po błędzie (włącza `pdb`).       |
tak komenda wywoluje pytest dla nazwy danego testu lub seri testow ktore maja dana nazwe :

~~~bash
pytest -k test_name
~~~


pytest -k construct - wystarczy podac nazwe testu z pliku i tylko dla tej nazwy sprawdzi testy



**📝 1. Pytest i Testy Jednostkowe**

  

**🔹 Podstawy pytest**

• pytest to popularna biblioteka do testowania w Pythonie.

• Obsługuje **testy jednostkowe** (unit tests), **testy integracyjne** i **test-driven development (TDD)**.

**🔹 Instalacja**

```sh

pip install pytest

```

**🔹 Pisanie testów jednostkowych**

```python

def add(x, y):
    return x + y

def test_add():
    assert add(2, 3) == 5
    
```

**🔹 Uruchamianie testów**

```sh

pytest test_file.py  # Uruchomienie konkretnego pliku
pytest               # Uruchomienie wszystkich testów
pytest -v            # Szczegółowy output






