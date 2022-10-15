from xml.etree.ElementTree import tostring
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

email_lista = ['teste@gmai.com 31231283910','thalis@gmail.com 312312930192', 'josedasnavas123@gmail.com 23192310239102391','papa123@gmail.com sdasdlasdals','th@123@outlook.com nnaksdla998312930']
navegador = webdriver.Chrome(executable_path='/home/bizonho/Videos/chromedriver_linux64/chromedriver')
navegador.get('http://127.0.0.1:5500/index.html')

time.sleep(5)
for line in email_lista:
    email,  password = line.split(' ')[0],line.split(' ')[1]
    time.sleep(3)
    navegador.find_element(By.XPATH, '/html/body/div/input[1]').send_keys(email)
    time.sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div/input[2]').send_keys(password)
    time.sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div/input[3]').click()




