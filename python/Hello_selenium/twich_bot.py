from ast import Bytes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from create_document import *

random_messages = ['manda um salve ai vey namoral', 'namoral vey manda um salve aew', 'manda salve pro bot plz', 'manda salve ai pro meu bot blz', 'Manda salve pro meu bot', 'Manda salve pro meu bot', 'Pichei sai correndo pau no cu de quem ta lendo.', 'piripi piridama comi teu cu na cama', 'Ei meu nome é dãi o macho da tua mãe', 'Ta na hora do porn http://www.xvideos.com', 'tá na hora do porn http://www.xhammster.com', 'Manda conta da Brazzers ai quem tiver', 'Os russo tão metendo bala na ucrania', 'Powwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww']


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('http://www.vivastreet.com.br')
time.sleep(1)
select = Select(driver.find_element(By.XPATH, '//*[@id="vs-cat-dropdown-1"]'))
time.sleep(2)
select.select_by_visible_text('Alugar casas - Apartamentos')
estado = Select(driver.find_element(By.XPATH, '//*[@id="vs_geo_dropdown_1"]'))
estado.select_by_visible_text('Pernambuco')
driver.find_element(By.XPATH,'//*[@id="static_home__category__form"]/fieldset/p[4]/input[1]').click()
time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="accept-disclaimer"]').click()


current_location = driver.current_url

create_element(current_location)

time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="vs_content"]/div[7]/ul/li[3]/a').click()


