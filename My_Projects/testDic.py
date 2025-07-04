from bs4 import BeautifulSoup

# Assuming 'elements' is your list of <dt> elements
elements = [
    '<dt class="in-realEstateFeatures__title">Riferimento e Data annuncio</dt>',
    '<dt class="in-realEstateFeatures__title">contratto</dt>',
    '<dt class="in-realEstateFeatures__title">tipologia</dt>',
    '<dt class="in-realEstateFeatures__title">superficie</dt>',
    '<dt class="in-realEstateFeatures__title">locali</dt>',
    '<dt class="in-realEstateFeatures__title">piano</dt>',
    '<dt class="in-realEstateFeatures__title">totale piani edificio</dt>',
    '<dt class="in-realEstateFeatures__title">Posti Auto</dt>',
    '<dt class="in-realEstateFeatures__title">altre caratteristiche</dt>',
    '<dt class="in-realEstateFeatures__title">prezzo</dt>',
    '<dt class="in-realEstateFeatures__title">cauzione</dt>',
    '<dt class="in-realEstateFeatures__title">anno di costruzione</dt>',
    '<dt class="in-realEstateFeatures__title">stato</dt>',
    '<dt class="in-realEstateFeatures__title">riscaldamento</dt>',
    '<dt class="in-realEstateFeatures__title">Climatizzatore</dt>',
    '<dt class="in-realEstateFeatures__title">certificazione energetica</dt>'
]  # Your BeautifulSoup elements list

elements_html = ' '.join(elements)  # Join the list into a single string
soup = BeautifulSoup(elements_html, 'html.parser')

# Now you can find elements using BeautifulSoup methods
dt_elements = soup.find_all('dt')  # This will give you a list of BeautifulSoup Tag objects

# To demonstrate, let's find the index of the 'altre caratteristiche' element again
def find_element_index(bs_elements, search_text):
    for index, bs_element in enumerate(bs_elements):
        if bs_element.text.strip() == search_text:
            return index
    return -1

index = find_element_index(dt_elements, "altre caratteristiche")
print(index)


# from bs4 import BeautifulSoup

# html_content = '<dd class="in-realEstateFeatures__value in-realEstateFeatures__badgeContainer"><div class="nd-badge in-realEstateFeatures__badge">Porta blindata</div><div class="nd-badge in-realEstateFeatures__badge">Balcone</div><div class="nd-badge in-realEstateFeatures__badge">Giardino privato</div></dd>'
# soup = BeautifulSoup(html_content, 'html.parser')

# badges = soup.find_all('div', class_="nd-badge in-realEstateFeatures__badge")


# def find_badge_texts(badges, search_texts):
#     found_texts = []
#     for badge in badges:
#         for search_text in search_texts:
#             if search_text in badge.text:
#                 found_texts.append(badge.text)
#                 break  # Break to avoid adding the same badge text multiple times if it contains more than one search word
#     return ", ".join(found_texts) if found_texts else "No"

# # Usage example:
# result = find_badge_texts(badges, ["Giardinoa", "Balconed"])
# print(result)



# def find_badge_text(badges, search_text):
#     for badge in badges:
#         if search_text in badge.text:
#             return badge.text
#     return "No"

# # Use the function like this:
# result = find_badge_text(badges, "Giardino")
# print(result)


# # Example call to the function
# find_badge_text(badges, "Giardino")

