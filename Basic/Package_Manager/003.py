import requests
from bs4 import BeautifulSoup

arkPage = requests.get("https://ark.intel.com/content/www/kr/ko/ark/products/134876/intel-core-i5-8300h-processor-8m-cache-up-to-4-00-ghz.html")
arkPageSoup = BeautifulSoup(arkPage.text, 'html.parser')

ProcessorNumber = arkPageSoup.find('span', {'data-key' : 'ProcessorNumber'}).text
print("모델명 : ", ProcessorNumber.strip())

passPage = requests.get("https://www.cpubenchmark.net/cpu.php?cpu=Intel+Core+i5-8300H+%40+2.30GHz&id=3254")
passPageSoup = BeautifulSoup(passPage.text, 'html.parser')

preTag = passPageSoup.find('div', {'class' : 'speedicon'})
targetTag = preTag.findNext('span').text
print("패스마크 점수 : ", targetTag)
