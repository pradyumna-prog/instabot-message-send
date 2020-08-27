from selenium import webdriver 
from time import sleep
from credentials import username, password

def startInsta(driver):
    driver.get("https://instagram.com/")
    sleep(5)
    #entering username
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
    #entering password
    sleep(1)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    #clicking login
    sleep(1)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    #click on save info not now
    sleep(4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    sleep(3)
    #clicking not now on turn on notification
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

def message(driver):
    #search person
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(input())
    sleep(2)
    #click on name
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/div/span').click()
    sleep(3)
    #click message box
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/button').click()
    sleep(3)
    #send msg
    c = 30
    while c:
        driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys('{}\n'.format(c))
        sleep(1)
        c-=1

def getFollowersList(driver):
    #clicking on my profile picture
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
    sleep(1)
    #clicking on profile
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div').click()
    #clicking on followers
    sleep(3)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
    sleep(3)
    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(12)
    ul = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul')
    followers_li = ul.find_elements_by_tag_name("li")
    followers = []
    for f in followers_li:
        followers.append(f.text.split('\n')[1])
    return followers
driver = webdriver.Chrome()
driver.maximize_window()
sleep(1)
startInsta(driver)
sleep(5)
getFollowersList(driver)