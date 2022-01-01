import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'ArchebalT/888.0 (X66; Ybuntu; Linux x86_64; rv:94.0) Fraecko/20100101 Firefox/94.0'
}

def get_location(url):
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    
    ip = soup.find('div', class_='ip').text.strip()
    location = soup.find('div', class_='value-country').text.strip()
    
    print(f'IP: {ip}\nLocation: {location}')


def main():
    get_location(url='https://2ip.ru')
    
    
if __name__ == '__main__':
    main()
    
# beautifulsoup4==4.10.0
# bs4==0.0.1
# certifi==2021.10.8
# charset-normalizer==2.0.7
# idna==3.3
# lxml==4.6.4
# requests==2.26.0
# soupsieve==2.3.1
# urllib3==1.26.7
