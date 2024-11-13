Zadanie Rekrutacyjne - Junior AI Developer

Opis
Projekt realizuje zadanie polegające na utworzeniu prostej aplikacji w Pythonie, która pobiera artykuł, generuje jego wersję HTML przy użyciu API OpenAI i zapisuje wynik do pliku 'podglad.html'.

Struktura projektu

- main.py - główny skrypt aplikacji
- config_template.py - szablon pliku konfiguracyjnego (skopiuj go jako config.py i dodaj swój klucz API)
- szablon.html - szablon HTML
- Generowane automatycznie:
  - zadanie.txt - plik z artykułem bazowym (pobrany z adresu: https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt)
  - artykul.html - wygenerowany artykuł HTML (generowany automatycznie)
  - podglad.html - ostateczna wersja artykułu HTML w szablonie (generowana automatycznie)

Instrukcja uruchomienia

1. Sklonuj repozytorium:
   git clone https://github.com/Pablossimus/Pawel_Ratkiewicz_zadanie_rekrutacyjne_OXIDO.git
   cd Pawel_Ratkiewicz_zadanie_rekrutacyjne_OXIDO

2. Utwórz i aktywuj wirtualne środowisko:
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows

3. Zainstaluj wymagane pakiety:
   pip install requests openai

4. Skopiuj config_template.py jako config.py i dodaj swój klucz API:
   openai_api_key = "twoj_klucz_api"

5. Uruchom skrypt:
   python main.py

6. Otwórz plik podglad.html w przeglądarce, aby zobaczyć wygenerowany artykuł.

Autor:
Paweł Ratkiewicz
Kontakt: pawel.ratkiewicz@gmail.com
