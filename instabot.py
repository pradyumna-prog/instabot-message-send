from selenium import webdriver 
from time import sleep
from credentials import username, password

def startInsta(driver):
    driver.get("https://instagram.com/")
    sleep(5)
    #entering username
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)
    #entering password
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    #clicking login
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
    sleep(5)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    sleep(5)
    #clicking not now on turn on notification
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

def getFollowersList(driver):
    #clicking on my profile
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a').click()
    sleep(1)
    #clicking on followers
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
def message(driver):
    #search person
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys('tripathishivanshi')
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
driver = webdriver.Chrome()
sleep(1)
startInsta(driver)
sleep(5)
message(driver)
