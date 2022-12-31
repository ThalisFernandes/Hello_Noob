from cmath import e
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
navegador = webdriver.Chrome(executable_path='/home/bizonho/Videos/chromedriver_linux64/chromedriver')

def troller_bot():
    navegador.get('http://www.omegle.com')
    time.sleep(2)

    navegador.find_element(By.XPATH,'//*[@id="chattypetextcell"]').click()
    time.sleep(1)
    navegador.find_element(By.XPATH, '/html/body/div[7]/div/p[1]/label/input').click()
    navegador.find_element(By.XPATH, '/html/body/div[7]/div/p[2]/label/input').click()
    time.sleep(1)
    navegador.find_element(By.XPATH, '/html/body/div[7]/div/p[3]/input').click()
    time.sleep(1)

    while True:
        time.sleep(3)
        navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea').send_keys('Oi')
        navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[3]/div/button').click()
        time.sleep(2)
        navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea').send_keys('Sou M e Vc?')
        navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[3]/div/button').click()
        time.sleep(4)
        navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea').send_keys('tem insta? o meu é kari_1606')
        navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[3]/div/button').click()
        time.sleep(3)
        navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea').send_keys('Me add lá pra conversar.')
        navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[3]/div/button').click()
        time.sleep(2)
        navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea').send_keys('Tô afim de conversar, tas afim?')
        navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[3]/div/button').click()
        time.sleep(4)
        navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[1]/div/button').click()
        navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[1]/div/button').click()
        time.sleep(1)
        navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[1]/div/button').click()


troller_bot()
