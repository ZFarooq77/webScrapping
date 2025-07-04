from bs4 import BeautifulSoup
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def extract_data_from_url(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'lxml')

    data = {
        "Rif.": None,
        "Agenzia": None,
        "Prezzo richiesta": None,
        "Tipologia": None,
        "Mq.": None,
        "Comune": None,
        "Zona": None,
        "Indirizzo": None,
        "Numero camere": None,
        "Numero vani": None,
        "Numero bagni": None,
        "Giardino": None,
        "Garage": None,
        "Terrazzo": None,
        "Posto auto": None,
        "Descrizione 100 parole": None,
        "Url": None,
        "Nazione": None,
        "Provincia": None,
        "Comune2": None,
        "Indirizzo3": None
    }

    # Here, add your BeautifulSoup code to populate the data dictionary.
    #data["Rif."] = soup.find("tag", {"attribute": "value"}).get_text(strip=True)
    
    titles = soup.find_all(class_='in-realEstateFeatures__title')
    values = soup.find_all(class_='in-realEstateFeatures__value')

    for title, value in zip(titles, values):
        print(f"Title: {title.text}: Value: {value.text}")
        
    return data

# Example usage with a URL
url = "https://www.immobiliare.it/annunci/108773485/"

extracted_data = extract_data_from_url(url)
print(extracted_data)

