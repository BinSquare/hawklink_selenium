from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait 
import time


"""path_to_chromedriver = '/Users/Caius/Desktop/chromdriver/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser.implicitly_wait(10)
"""

elements = {"login": '//*[@id="mainContent"]/a',
            "loginBtn": 'input[type=\"submit\"]',
            "administration": '//*[@id="navbar"]/ul/li[6]/a',
            "request_list": '//*[@id="mainNav"]/nav/ul/li[3]/a',
            "request_listop": '//*[@id="ddm-2"]/ul/li[1]/a',
            "all_requests": ''
            }

ignore_ext = []

log = open('log.txt', 'w')

browser = webdriver.Firefox()

url = 'https://iit.collegiatelink.net/'
sut = url
to_be_scraped = []
scraped = []


def hawklink():
    browser.get(url)

    browser.find_element_by_xpath(elements['login']).click()

    browser.find_element_by_id('Username').send_keys('Username')

    browser.find_element_by_id('Password').send_keys('Password')

    browser.find_element_by_css_selector(elements['loginBtn']).click()

    browser.find_element_by_xpath(elements['administration']).click()
    browser.find_element_by_xpath(elements['request_list']).click()
    browser.find_element_by_xpath(elements['request_listop']).click()


def uniqify(seq):
    keys_ini = {}
    for i in seq:
        keys[i] = 1
    return keys.keys()


def scraper(site):
    links = getlinks(site)
    scraped.append(site)
    badlinks = testlinks(links)
    if badlinks:
        for link in badlinks:
            print "* Bad link on \"%s\" detected: \"%s\"" % (site, link)
            log.write("* Bad link on \"%s\" detected: \"%s\"" % (site, link))
            links.remove(link)
    log.write('Done scraping %s\n' % (site))
    log.flush()
    return links


def getlinks(site):
    print "Testing %s\n" % (site)
    driver.get(site)
    print "  driver.get successful\n"
    elements = driver.find_elements_by_xpath("//a")
    print "  driver.find_elements_by_xpath successful\n"
    links = []
    for link in elements:
        try:
            if str(link.get_attribute("href"))[0:4] == "http":
                links.append(str(link.get_attribute("href")))
        except StaleElementReferenceException:
            log.write("Stale element reference found!\n")
            log.flush()
    links = uniqify(links)
    return links


def crawler():
    while to_be_scraped:
        site = to_be_scraped.pop(0)
        links = scraper(site)
        for link in links:
            if not link[0:(len(sut))] == sut:
                print "%s not at sut" % (link)
                continue
            elif link in scraped:
                print "%s has already been scraped" % (link)
                continue
            elif link in to_be_scraped:
                print "%s is already on the queue" % (link)
                continue
            elif ignore(link):
                print "%s is being ignored" % (link)
                continue
            else:
                print "adding %s to the queue" % (link)
                to_be_scraped.append(link)


to_be_scraped.append(sut)
driver = webdriver.Firefox()
hawklink()
crawler()
log.close