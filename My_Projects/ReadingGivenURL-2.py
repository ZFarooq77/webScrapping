from bs4 import BeautifulSoup
import requests
import sys
import io
import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download("punkt")
nltk.download("stopwords")

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def extract_data_from_url(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

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
    #Extracting Agenzia
    agency_div = soup.find('div', class_='nd-figure__image in-referent__image')
    # Find the img tag and then get its 'alt' attribute
    agency_name = agency_div.find('img', class_='nd-figure__content')['alt']
    print(agency_name)
    data["Agenzia"] = agency_name
    
    commune = soup.find('h3', class_="in-relatedLinks__titleList").text.strip()
    # print(commune)
    # Split the string into a list of words and select the last one
    last_word = commune.split()[-1]
    data["Comune"] = last_word

    # print(data["Comune"])

    # data["Comune"] = commune

    zona = soup.find('div', class_="in-titleBlock__content").text.strip()
    # print(zona)
    # Split the text by comma and strip whitespace
    parts = [part.strip() for part in zona.split(',')]
    # Extract the text between the first two commas
    if len(parts) > 1:
        text_between_commas = parts[1]
    else:
        text_between_commas = ""
    
    data["Zona"] = text_between_commas 

    # print(text_between_commas)
    
    # extracting the last text after last comma 
    no_of_spans = len(soup.find_all('span', class_="in-location"))
    if no_of_spans > 2:
        adr = soup.find_all('span', class_="in-location")[2].text.strip()
    else:
        adr = "Non specificato"
    # print(adr)
    data["Indirizzo"] = adr
 
    # Extracting the bagni(bathrooms)
    bathrooms = soup.find_all('div', class_="in-feat__data")[2].text.strip()   
    data["Numero bagni"] = bathrooms
    
    # Extracting the vani rooms
    no_of_rooms_vani = soup.find('div', class_="in-feat__data").text.strip()
    data["Numero vani"] = no_of_rooms_vani
    
    # Extracting the camera rooms
    no_of_rooms_c = soup.find_all('dd', class_="in-realEstateFeatures__value")[4].text.strip()
    match = re.search(r'\((\d+)', no_of_rooms_c)
    if match:
        number_after_bracket = match.group(1)
        data["Numero camere"] = number_after_bracket
    else:
        print("Number not found")
    
    # Giardino privato
    # gardens = soup.find('div', class_="nd-badge in-realEstateFeatures__badge").text.strip()    
    # print(gardens)
      
    
    titles = soup.find_all(class_='in-realEstateFeatures__title')
    values = soup.find_all(class_='in-realEstateFeatures__value')
    
    #Finding the index of 'altre caratteristiche' element
    index = find_element_index(titles, "altre caratteristiche")
    
    #Extracting the badge "Giardino" from the values list
    giardino = find_badge_texts(values[index], ["Giardino"])
    # print(giardino)
    data["Giardino"] = giardino
    
    #Extracting the badges "Terrazza", "Balcone", "Terrazzo", "Balcony" from the values list
    terrazzo = find_badge_texts(values[index], ["Terrazza", "Balcone", "Terrazzo", "Balcony"])
    data["Terrazzo"] = terrazzo
    
    #finding the index of 'Posti Auto' element
    posti_auto_index = find_element_index(titles, "Posti Auto")
    #Extracting the value of "Posto auto" from the values list if it exists
    if posti_auto_index == -1:
        posto_auto = "Not specified"
    else:   
        posto_auto = values[posti_auto_index].text.strip()
    
    # inserting the value into the dictionary
    data["Posto auto"] = posto_auto
    data["Garage"] = posto_auto
    
    # inserting the url into the dictionary
    data["Url"] = url
    
    
    # extracting description data
    description = soup.find('div', class_="in-readAll in-readAll--lessContent").text.strip()
    
        
    # Input text - to summarize
    text = description
    # Tokenizing the text
    stopWords = set(stopwords.words("italian"))
    words = word_tokenize(text)

    # Creating a frequency table to keep the
    # score of each word

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    # Creating a dictionary to keep the score
    # of each sentence
    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    # Sort sentenceValue dictionary by its values
    sentenceValue = dict(sorted(sentenceValue.items(), key=lambda item: item[1], reverse=True))

    # Storing sentences into our summary.
    summary = ''
    word_count = 0
    for sentence in sentenceValue:
        if word_count >= 100:
            break
        summary += " " + sentence
        word_count += len(sentence.split())
    # print(summary)
    
    data["Descrizione 100 parole"] = summary

    # extracting commune 2
    com2 = soup.find_all('h3', class_="in-relatedLinks__titleList")[0].text.strip()
    data["Comune2"] = com2

    # extracting provincia
    province = soup.find_all('h3', class_="in-relatedLinks__titleList")[1].text.strip()
    data["Provincia"] = province
    print(province)

    #detecting country using provincia










    mapping = {
        # Add the appropriate mapping based on your HTML structure
        "Riferimento e Data annuncio": "Rif.",
        "tipologia" : "Tipologia",
        "prezzo": "Prezzo richiesta",
        "tipologia": "Tipologia",
        "superficie": "Mq.",        
        "comune": "Comune", 
               
        # "zona": "Zona",        
        # "indirizzo": "Indirizzo",
        # "giardino": "Giardino",
        # "garage": "Garage",
        # "terrazzo": "Terrazzo",
        # "posto auto": "Posto auto",
        # "descrizione": "Descrizione 100 parole",
        # "url": "Url",
        # "nazione": "Nazione",
        # "provincia": "Provincia",
        # "comune": "Comune2",
        # "indirizzo": "Indirizzo3",       
        
        # Add other mappings as needed
    }
    # Create a dictionary that maps the values to the keys
    for title, value in zip(titles, values):
        key = mapping.get(title.text.strip())
        if key in data:
            data[key] = value.text.strip()  
    
    return data


# Find the index of the 'altre caratteristiche' element again
def find_element_index(bs_elements, search_text):
    for index, bs_element in enumerate(bs_elements):
        if bs_element.text.strip() == search_text:
            return index
    return -1

# extracting the badge value of 'altre caratteristiche'
def find_badge_texts(badges, search_texts):
    found_texts = []
    for badge in badges:
        for search_text in search_texts:
            if search_text in badge.text:
                found_texts.append(badge.text)
                break  # Break to avoid adding the same badge text multiple times if it contains more than one search word
    return ", ".join(found_texts) if found_texts else "No"

# Usage example:
# result = find_badge_texts(badges, ["Giardinoa", "Balconed"])
# print(result)



# Example usage with a URL
url = "https://www.immobiliare.it/annunci/108773485/" #  row 2
#url = "https://www.immobiliare.it/annunci/109663467/" #  row 4
#url = "https://www.immobiliare.it/annunci/109636143/" #  row 8

extracted_data = extract_data_from_url(url)
# #print the dictinary one lement in a row
# for key, value in extracted_data.items():
#     print(f"{key}: {value}")    
# print(extracted_data)
