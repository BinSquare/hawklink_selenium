from selenium import webdriver


"""path_to_chromedriver = '/Users/Caius/Desktop/chromdriver/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser.implicitly_wait(10)
"""


def hawklink():
    browser = webdriver.Firefox()

    url = 'https://iit.collegiatelink.net/'
    browser.get(url)

    browser.find_element_by_xpath('//*[@id="mainContent"]/a').click()

    browser.find_element_by_id('Username').clear()
    browser.find_element_by_id('Username').send_keys('username')

    browser.find_element_by_id('Password').clear()
    browser.find_element_by_id('Password').send_keys('password')

    browser.find_element_by_css_selector('input[type=\"submit\"]').click()

    browser.find_element_by_xpath('//*[@id="navbar"]/ul/li[6]/a').click()
    browser.find_element_by_xpath('//*[@id="mainNav"]/nav/ul/li[3]/a').click()
    browser.find_element_by_xpath('//*[@id="ddm-2"]/ul/li[1]/a').click()


def crawler():
    pass

hawklink()