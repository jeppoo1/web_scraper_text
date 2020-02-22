
'''
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
driver = Chrome("C:\\WHERE_YOUR_CHROMEDRIVER.exe_IS_LOCATED")
driver.get('https://webscraper.io/test-sites/e-commerce/allinone')
soup = BeautifulSoup(driver.page_source, 'html.parser')

'''

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\WHERE_YOUR_CHROMEDRIVER.exe_IS_LOCATED')
driver.get('https://webscraper.io/test-sites/e-commerce/allinone')


'''
### Web scraper - Throws "This package supports only Linux, MacOSX or Windows platforms" error. 
#### SOLUTION: Do not import chromedriver, just add it to PATH variable, and set webdriver.Chrome("C:/..../PATH/LOCATION_OF_CHROMEDRIVER.EXE")

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("C:\\WHERE_YOUR_CHROMEDRIVER.exe_IS_LOCATED")
driver.get('https://webscraper.io/test-sites/e-commerce/allinone')

soup = bs.BeautifulSoup(driver.page_source, 'html.parser')
'''

'''
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(ChromeDriverManager().install())  # Optional argument, if not specified will search path.
time.sleep(2) # Let the user actually see something!
driver.get('https://webscraper.io/test-sites/e-commerce/allinone')
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup)
'''

## Example for googling automatically
'''driver.get('http://www.google.com/')
time.sleep(5)
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()'''