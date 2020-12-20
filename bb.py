import time 
# importing webdriver from selenium 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

a = "https://meet.google.com/zpk-nqix-vib"

options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--window-size=1200,900")
options.add_argument("user-agent='User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'")
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,     # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 2,
     "profile.default_content_setting_values.notifications": 2,
     "profile.default_content_setting_values.popups":2
  })


# Here Chrome will be used 
driver = webdriver.Chrome('/home/swapnil/Desktop/sele/chromedriver',options=options)
driver.get('https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3A8761f44b2df242a2%2C10%3A1605194839%2C16%3Aa5c0f97ced3a97a0%2Cd6e1862c7d914c10f6439ba9b16cdacfc72fa9b10b30b7638c85ccda496f2a69%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22568af41449fc46548320092241478f27%22%7D&response_type=code&flowName=GeneralOAuthFlow')

#Logs in the stackoverflow
username=driver.find_element_by_id('identifierId')
username.click()
username.send_keys('shindeswapnil57260@gmail.com')

next=driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
next.click()
time.sleep(3)
password=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.click()
password.send_keys('9382084913swapnil')
next=driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
next.click()

time.sleep(3) 

#URL of website 
url = f"{a}"

# Opening the website 
driver.get(url)
time.sleep(4)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(3)
# geeting the button by class name 
driver.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]").click()