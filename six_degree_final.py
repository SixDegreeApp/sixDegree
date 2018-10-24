from selenium import webdriver
import time
import getpass

username = input('What is your username? ')
password = getpass.getpass('What is your password? ')
userSearch = input('Who\'s the user you\'d like to search? ')

url = 'https://www.instagram.com/accounts/login/'

#driver = webdriver.Chrome("C:\Users\Cole\Downloads\chromedriver")
#Mitch's driver = webdriver.Chrome("C:\Users\Mitch Hansen\Documents\chromedriver")
driver = webdriver.Chrome("/Users/Cole/Downloads/chromedriver")
driver.get(url)

driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)

time.sleep(2)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/button').click()

######      We are now logged in    #######

time.sleep(4)

#userSearch = 'pharrell"
user_url = 'https://www.instagram.com/' + userSearch + '/?__a=1'
driver.get(user_url)

from bs4 import BeautifulSoup

html_soup = BeautifulSoup(driver.page_source, 'html.parser')
infoPage = str(html_soup.pre.contents)

tempID = ""
tempFollowerCount = ""
tempFollowingCount = ""

#find user id
for x in range(infoPage.find('profilePage_') + 12, len(infoPage)):
    if infoPage[x] == "\"":
        break
    tempID += infoPage[x]

#find user follower count
for x in range(infoPage.find('edge_followed_by":{"count":') + 27, len(infoPage)):
    if infoPage[x] == "}":
        break
    tempFollowerCount += infoPage[x]

#find user following count
for x in range(infoPage.find('edge_follow":{"count":') + 22, len(infoPage)):
    if infoPage[x] == "}":
        break
    tempFollowingCount += infoPage[x]

#create the list of followers from id number        THIS WILL ALL BE INSIDE A FOR LOOP FOR EACH 50 ENTRY
iterations = 0
follower_list = []
endCursor = ""
tempNumStore = float(int(tempFollowingCount)/50)
if tempNumStore.is_integer() == False:
    numToIt = int(tempNumStore) + 1
else:
    numToIt = int(tempNumStore)
while (iterations != numToIt+1):
    driver.get('http://instagram.com/graphql/query/?query_hash=58712303d941c6855d4e888c5f0cd22f&variables={"id":"' + tempID + '","first":' + str(4000) + ',"after":"' + endCursor + '"}')
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
    while (infoPage.find('"id":"', counter) != -1):
         for x in range(infoPage.find('"id":"', counter) + 6, len(infoPage)):
             if infoPage[x] == "\"":
                 break
             temp_username += infoPage[x]
         follower_list.append(temp_username)
         temp_username = ""
         counter = infoPage.find('{"id":', counter) + 7#add 2
    iterations+=1

print(len(follower_list))
print(iterations)
#print(*follower_list, sep = '\n')

###########             NOW WE HAVE TO BEGIN BIDIRECTIONAL BREATH FIRST SEARCH          ###########

#My file location "C:\\Users\\Mitch Hansen\\Documents\\6 Degree"
destination = "C:\\Users\\Cole\\source\\repos\\sixDegree\\sixDegree\\"
file = open(destination + userSearch, 'w')
for follower_list in follower_list:
    file.write(follower_list + '\n')
file.close()
print("File has been created!")
