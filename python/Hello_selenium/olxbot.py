from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup as bs4


def build_document(arr):
    return 0




navegador = webdriver.Chrome(executable_path='/home/bizonho/Videos/chromedriver_linux64/chromedriver')
navegador.get('https://pe.olx.com.br/')
time.sleep(1)
navegador.find_element(By.XPATH, '//*[@id="left-side-main-content"]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/a').click()
navegador.find_element(By.XPATH, '//*[@id="left-side-main-content"]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[3]/a/div/span[1]').click()
url = navegador.current_url
html = requests.get(str(url)).content

soup = bs4(html, 'lxml')
body = soup.find_all("ad-list")

print(body)





