from http import cookiejar
import requests
from bs4 import BeautifulSoup as bs
from requests import cookies
from config import login, proxy


class CSV:
    
    def __init__(self):
        pass

    def fieldnames(self, data):
        pass

    def write(self, data):
        pass


class Parce:

    def __init__(self, url):

        self.login_url = 'https://partners.agromat.ua/user_b2bs/sign_in'
        self.url = url  
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        }

    def login(self):
        s = requests.Session()
        
        r = s.post(self.login_url, headers=self.headers, data=login, proxies=proxy, verify=False)
        q = s.get(self.url, headers=self.headers, proxies=proxy, verify=False)

        print(s.cookies)

        return r

    def html(self, url):
        pass

    def urls(self):
        pass

    def content(self):
        pass

    def parce(self):
        login = self.login()


agro = Parce('https://partners.agromat.ua/')
agro.parce()