from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
from keys import keys
from bs4 import BeautifulSoup
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

# navigation elements
elements = {"login": '//*[@id="mainContent"]/a',
            "loginBtn": 'input[type=\"submit\"]',
            "administration": '//*[@id="navbar"]/ul/li[5]/a',
            "request_list": '//*[@id="mainNav"]/nav/ul/li[3]/a',
            "request_listop": '//*[@id="ddm-2"]/ul/li[1]/a',
            "all_requests": '//*[@id="page"]/section/ul/li[2]/a',
            "second_page": '//*[@id="RequestsGrid"]/div/div/span[2]/a[1]',
            "next_page": '//*[@id="RequestsGrid"]/div/div/span[2]/a[3]',
            "page_content": '//*[@id="page"]/section'
            }


# initiates webdriver with firefox
browser = webdriver.Firefox()

url = 'https://iit.collegiatelink.net/'


# using Gspread to authenticate with google's stupid fucking Oauth2 api designed only for use by the select few who made it.
# credits to Gspread code goes to the author of the Gspread documentation

json_key = json.load(open('hawklink_service.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

gc = gspread.authorize(credentials)

worksheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1hVeCLk54DWloZeao5k3FgIYGFepUZpx1P6Ylsi5pYdI/edit?usp=sharing").sheet1

# test updating a cell in sheet1

worksheet.update_cell('1', '1', 'test64')
worksheet.update_cell('1', '2', 'amount approved')
worksheet.update_cell('1', '3', 'date')
worksheet.update_cell('1', '4', 'type')
worksheet.update_cell('1', '5', 'status')
worksheet.update_cell('1', '6', 'organization')
worksheet.update_cell('1', '7', 'keywords')
worksheet.update_cell('1', '8', 'purchase number')
worksheet.update_cell('1', '9', 'additional info')


# Selenium navigating to the goddamn anti-crawler website to crawl the damn thing. Can't stop me hawklink, up yours! ..|.. 


def hawklink_nav():
    browser.get(url)

    browser.find_element_by_xpath(elements['login']).click()

    browser.find_element_by_id('Username').send_keys(keys['username'])

    browser.find_element_by_id('Password').send_keys(keys['password'])

    browser.find_element_by_css_selector(elements['loginBtn']).click()

    browser.find_element_by_xpath(elements['administration']).click()
    browser.find_element_by_xpath(elements['request_list']).click()
    browser.find_element_by_xpath(elements['request_listop']).click()
    browser.find_element_by_xpath(elements['all_requests']).click()

"""
def page_parse():
    souped = BeautifulSoup(browser.page_source, "html5lib")
    for tr_tag in souped.find_all('tr'):
        print tr_tag.text, tr_tag.next_sibling
        for tr_tag.text in this
    pass
"""
cell_row = 1


def rows():
    """souped = BeautifulSoup(browser.page_source, "html5lib")"""
    elem = browser.find_element_by_xpath(elements['page_content'])
    print elem.tag_name
    souped = BeautifulSoup(elem.get_attribute('innerHTML'), "html5lib")
    print souped
    rows = souped.findChildren(['tr'])
    global cell_row
    for row in rows:
        cell_col = 1
        i = 0
        cell_dict = []
        cells = row.findChildren('td')
        for cell in cells:
            """print cell.string"""
            try:
                cell_dict.append(cell.string or cell.a.string)
            except Exception, e:
                cell_dict.append("none")
            worksheet.update_cell(str(cell_row), str(cell_col), cell_dict[i])
            i += 1
            """print i"""
            cell_col += 1
        print " "
        """print cell_dict"""
        cell_row += 1
        print cell_row


# unique identification
"""    def uniqify(seq):
        keys_ini = {}
        for i in seq:
            keys[i] = 1
        return keys.keys()"""


def second_page():
    browser.find_element_by_xpath(elements['second_page']).click()
    pass


def next_page():
    browser.find_element_by_xpath(elements['next_page']).click()
    pass


def next_parse():
    next_page()
    time.sleep(5)
    rows()
    pass

# main execution fuctions
hawklink_nav()
rows()
second_page()
time.sleep(3)
rows()
# repeats the same parsing for next_page() and row() for 10 times,
for num in xrange(1, 11):
    next_parse()
    pass

print cell_row
browser.quit()
