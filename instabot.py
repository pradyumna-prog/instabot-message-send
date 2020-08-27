from selenium import webdriver
from time import sleep
from credentials import password

def startInsta(browser, username):
    browser.get("https://instagram.com/")
    sleep(5)
    #entering username
    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
    #entering password
    sleep(1)
    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    #clicking login
    sleep(1)
    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    #click on save info not now
    sleep(4)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    sleep(3)
    #clicking not now on turn on notification
    browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

def message(browser):
    #search person
    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(input())
    sleep(2)
    #click on name
    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/div/span').click()
    sleep(3)
    #click message box
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/button').click()
    sleep(3)
    #send msg
    c = 30
    while c:
        browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys('{}\n'.format(c))
        sleep(1)
        c-=1

def getList(browser, request):
    li_index = 0
    if request.lower() == "followers" : li_index = 2
    elif request.lower() == "following" : li_index = 3
    else:
        print("Wrong Input")
        return None
    #clicking on my profile picture
    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
    sleep(1)
    #clicking on profile
    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div').click()
    #clicking on followers
    sleep(4)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li['+str(li_index)+']/a').click()
    #slecting the box containing lis with followers
    sleep(3)
    followers_box = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
    #scorlling the box to last
    pheight, height = 0, 1
    while(pheight != height):
        pheight = height
        height = browser.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, followers_box)
        sleep(5)
    #fetching name
    followers_links = followers_box.find_elements_by_tag_name("a")
    followers = []
    for f in followers_links:
        followers.append(f.text)
    #closing the followers box
    browser.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
    #clicking Instagram
    sleep(2)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div/img').click()

    return followers

browser = webdriver.Chrome()
browser.maximize_window()
sleep(1)
startInsta(browser, 'pd_pradyumna')
sleep(5)
followers = getList(browser, "Followers")
following = getList(browser, "Following")
unfollowers = list(set(following) - set(followers))
sleep(2)

# s = "".join(unfollowers)
# browser.get("localhost/instabot/index.php?list="+s)