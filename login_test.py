import requests
from bs4 import BeautifulSoup as bs

session = requests.session()

def log_in():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    
    }
    
    data = {
            'username': 'Username',
            'password': 'Password',
            'grant_type': 'password',
            'login_submit': 'Log in'
                
    }
    
    login = session.post("http://instagram.com/accounts/login", data=data, headers=headers)
    
    print login.status_code


log_in()
