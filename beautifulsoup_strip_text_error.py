import urllib2
from urllib2 import Request
import re
from bs4 import BeautifulSoup

url = "http://www.sanfoundry.com/c-programming-questions-answers-variable-names-1/"
#url="http://www.sanfoundry.com/c-programming-questions-answers-variable-names-2/"
req = Request(url)
resp = urllib2.urlopen(req)
htmls = resp.read()
c=0;
soup = BeautifulSoup(htmls, 'lxml')
#skipp portion of code
res2 = soup.find('h1',attrs={"class":"entry-title"})
br = soup.find('span',attrs={'class':'IL_ADS'})
br = soup.find('p').text # separate title

for question in soup.find_all(text=re.compile(r"^\d+\.")):
    answers = [br.next_sibling.strip() for br in question.find_next_siblings("br")]
    #s = ''.join([i for i in question if not i.isdigit()])
    if not answers:
        break

    print question.encode('utf-8')
    ul = question.find_next_sibling("ul")
    print(ul.get_text(' ', strip=True))