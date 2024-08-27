from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome()

url = "https://www.divan.ru/category/divany-i-kresla"

driver.get(url)

divans = driver.find_elements(By.CLASS_NAME, 'WdR1o')

parsed_data = []

for divan in divans:
    try:
        price = divan.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH').text
    except:
        print("Произошла ошибка при парсинге")
        continue

    parsed_data.append([price])

driver.quit()

with open("divan.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])
    writer.writerows(parsed_data)