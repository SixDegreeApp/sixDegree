from selenium import webdriver
import time

username = 'nylm2017_bellevue'
password = 'coleramos1999'

url = 'https://www.instagram.com/accounts/login/'

#driver = webdriver.Chrome("C:\Users\Cole\Downloads\chromedriver")
driver = webdriver.Chrome("/Users/Cole/Downloads/chromedriver")
driver.get(url)

driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)

time.sleep(2)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/span/button').click()

######      We are now logged in    #######

time.sleep(4)

userSearch = 'maggie_horton11'
user_url = 'https://www.instagram.com/' + userSearch + '/?__a=1'
driver.get(user_url)

from bs4 import BeautifulSoup

html_soup = BeautifulSoup(driver.page_source, 'html.parser')
infoPage = str(html_soup.pre.contents)

tempID = ""
tempFollowerCount = ""
tempFollowingCount = ""

#find user id,follower count, following count
for x in range(infoPage.find('profilePage_') + 12, len(infoPage)):
    if infoPage[x] == "\"":
        break
    tempID += infoPage[x]
for x in range(infoPage.find('edge_followed_by":{"count":') + 27, len(infoPage)):
    if infoPage[x] == "}":
        break
    tempFollowerCount += infoPage[x]
for x in range(infoPage.find('edge_follow":{"count":') + 22, len(infoPage)):
    if infoPage[x] == "}":
        break
    tempFollowingCount += infoPage[x]
print(int(tempFollowerCount)/50)
#create the list of followers from id number        THIS WILL ALL BE INSIDE A FOR LOOP FOR EACH 50 ENTRY
iterations = 0
follower_list = []
endCursor = ""
tempNumStore = float(int(tempFollowerCount)/50)
if tempNumStore.is_integer() == False:
    numToIt = int(tempNumStore) + 1
else:
    numToIt = int(tempNumStore)
while (iterations != numToIt):
    driver.get('http://instagram.com/graphql/query/?query_hash=37479f2b8209594dde7facb0d904896a&variables={"id":"' + tempID + '","first":' + str(50) + ',"after":"' + endCursor + '"}')
    endCursor = ""
    html_soup = BeautifulSoup(driver.page_source, 'html.parser')
    infoPage = str(html_soup.pre.contents)

    #find end cursor
    for x in range(infoPage.find('end_cursor":"') + 13, len(infoPage)):
        if infoPage[x] == "\"":
            break
        endCursor += infoPage[x]


    temp_username = ""
    counter = 0
    while (infoPage.find('"username":"', counter) != -1):
         for x in range(infoPage.find('"username":"', counter) + 12, len(infoPage)):
             if infoPage[x] == "\"":
                 break
             temp_username += infoPage[x]
         follower_list.append(temp_username)
         temp_username = ""
         counter = infoPage.find('"username":', counter) + 13
    iterations+=1

print(len(follower_list))
print(iterations)
