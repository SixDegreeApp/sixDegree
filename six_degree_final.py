#Once logged in, how to scrape follower list
from requests import get

url = 'https://www.instagram.com/espn/following/?hl=en'

response = get(url)

print(response.text[:500])

from bs4 import BeautifulSoup

html_soup = BeautifulSoup(response.text, 'html.parser')
follower_containers = html_soup.find_all('div', class_ = 'FPmhX')
print(type(follower_containers))
print(len(follower_containers))
