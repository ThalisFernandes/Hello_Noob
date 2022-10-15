from bs4 import BeautifulSoup
import requests
def create_element(url):
    request = requests.get(str(url))
    html = request.text
    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())
    with open('content.txt', 'wb') as arquivo:
        for line in soup.find_all('li'):
            print(f'{line}')
            arquivo.write(line)



