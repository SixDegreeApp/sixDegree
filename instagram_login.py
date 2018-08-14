import requests
import json

BASE_URL = 'https://www.instagram.com'
LOGGIN_URL = BASE_URL + 'accounts/login/?hl=en'
USERNAME = 'ENTER_USERNAME'
PASSWD = 'ENTER_PASSWORD_HERE'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

session = requests.Session()
session.headers = {'user-agent' : USER_AGENT}
session.headers.update({'Referer' : BASE_URL})

req = session.get(BASE_URL)
session.headers.update({'X-CSRFToken' : req.cookies['csrftoken']})
login_data = {'username' : USERNAME, 'password' : PASSWD}
login = session.post(LOGGIN_URL, data = login_data, allow_redirects=True)
session.headers.update({'X-CSRFToken' : login.cookies['csrftoken']})
cookies = login.cookies
login_text = json.loads(login.text)

print(login_text)
