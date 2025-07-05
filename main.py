import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.translate import translate_title
from utils.analyze import analyze_words
from selenium.webdriver.chrome.options import Options

URL = "https://elpais.com/opinion/"
HEADERS = []
ARTICLES = []

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

try:
    driver.get(URL)
    time.sleep(3)
    articles = driver.find_elements(By.CSS_SELECTOR, "article")[:5]
    for article in articles:
        title_el = article.find_element(By.TAG_NAME, "h2")
        content_el = article.find_element(By.TAG_NAME, "p")
        img_el = article.find_elements(By.TAG_NAME, "img")

        title = title_el.text.strip()
        content = content_el.text.strip()
        HEADERS.append(title)
        ARTICLES.append((title, content))

        # Save image if available
        if img_el:
            img_url = img_el[0].get_attribute("src")
            img_data = requests.get(img_url).content

       import os

# Ensure the images directory exists before writing
os.makedirs("images", exist_ok=True)

# Sanitize and prepare a safe filename
safe_title = title[:15].strip().replace(" ", "_").replace("/", "-")
filename = f"images/{safe_title}.jpg"

# Save the image content safely
with open(filename, "wb") as f:
    f.write(image_content)

            with open(f"images/{title[:15].replace(' ', '_')}.jpg", "wb") as f:
                f.write(img_data)
finally:
    driver.quit()

print("Spanish Titles:")
for title, content in ARTICLES:
    print(f"Title: {title}\nContent: {content}\n")

print("\nTranslated Titles:")
translated = [translate_title(t) for t in HEADERS]
for t in translated:
    print(t)

print("\nRepeated Words:")
print(analyze_words(translated))
