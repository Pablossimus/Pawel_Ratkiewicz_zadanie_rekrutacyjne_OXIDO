import requests  # Importowanie modułu requests do wykonywania zapytań HTTP
import openai  # Importowanie modułu openai do komunikacji z API OpenAI
from config import openai_api_key  # Importowanie klucza API OpenAI z pliku config

print("Pobieranie pliku z zadaniem...")  # Informacja o pobieraniu pliku z zadaniem
url = "https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt"  # URL pliku z zadaniem
response = requests.get(url)  # Wykonywanie zapytania HTTP GET w celu pobrania pliku

if response.status_code == 200:  # Sprawdzanie, czy pobranie się powiodło
    with open("zadanie.txt", "wb") as file:  # Otwieranie pliku do zapisu w trybie binarnym
        file.write(response.content)  # Zapisanie pobranej zawartości do pliku
    print("Plik został pobrany i zapisany jako zadanie.txt")  # Informacja o sukcesie
else:
    print(f"Nie udało się pobrać pliku, status code: {response.status_code}")  # Informacja o błędzie

print("Odczytywanie zawartości pobranego pliku...")  # Informacja o odczycie pliku
with open("zadanie.txt", "r", encoding="utf-8") as file:  # Otwieranie pliku do odczytu w trybie tekstowym
    content = file.read()  # Odczytanie zawartości pliku do zmiennej content
    print("Zawartość pliku zadanie.txt:")  # Wyświetlenie zawartości pliku
    print(content)

openai.api_key = openai_api_key  # Ustawienie klucza API OpenAI

print("Generowanie artykułu przy użyciu OpenAI...")  # Informacja o generowaniu artykułu
def generate_article(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Użycie modelu GPT-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},  # Wiadomość systemowa
            {"role": "user", "content": prompt}  # Wiadomość użytkownika z promptem
        ]
    )
    return response.choices[0].message["content"].strip()  # Zwracanie wygenerowanej treści artykułu

# Definiowanie promptu do wygenerowania artykułu
prompt = f'''
Napisz artykuł na podstawie poniższego tekstu, zawierający szczegółowe wprowadzenie, rozwinięcie i podsumowanie.
W miejscach, gdzie warto wstawić grafiki, oznacz je z użyciem tagu <img> z atrybutem src="image_placeholder.jpg".
Dodaj atrybut alt do każdego obrazka z dokładnym promptem do wygenerowania grafiki.
Umieść podpisy pod grafikami używając odpowiedniego tagu HTML.

Zawartość artykułu ma być zawarta w pełnej strukturze HTML (razem z tagami <html>, <body>, <header>, <article>, <footer> i <img>).
Dodaj kilka nagłówków <h2> w głównej treści artykułu, aby lepiej zorganizować informacje.
Proszę nie dodawać żadnych oznaczeń kodu takich jak trzykrotne cudzysłowy (`).

{content}
'''

article_html = generate_article(prompt)  # Generowanie artykułu na podstawie promptu
print("Wygenerowany artykuł HTML:")  # Wyświetlenie wygenerowanego artykułu
print(article_html)

# Zapisanie wygenerowanego artykułu do pliku artykul.html bez tagów HTML
with open("artykul.html", "w", encoding="utf-8") as file:
    file.write(content)
print("Artykuł został zapisany jako artykul.html")  # Informacja o sukcesie

print("Wstawianie wygenerowanego HTML do szablonu...")  # Informacja o wstawianiu artykułu do szablonu
with open("szablon.html", "r", encoding="utf-8") as file:  # Otwieranie szablonu HTML do odczytu
    template = file.read()  # Odczytanie zawartości szablonu do zmiennej template

final_html = template.replace("<!-- BODY -->", article_html)  # Wstawianie wygenerowanego artykułu w miejsce <!-- BODY -->

print("Zapisanie finalnego pliku HTML...")  # Informacja o zapisywaniu pliku HTML
with open("podglad.html", "w", encoding="utf-8") as file:  # Otwieranie pliku podglad.html do zapisu
    file.write(final_html)  # Zapisanie ostatecznej wersji HTML do pliku

print("Artykuł został zapisany jako podglad.html")  # Informacja o sukcesie

input("Naciśnij Enter, aby zakończyć...")  # Oczekiwanie na naciśnięcie klawisza Enter w celu zakończenia skryptu
