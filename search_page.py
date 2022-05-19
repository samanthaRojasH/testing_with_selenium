from ast import Return
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(object):
    #Start with google, in order to look for the testing page 
    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://google.com'
        self.search_locator = 'q'

    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME,'q')))
        return True

    @property
    #Look for the testing page 
    def keyword(self):
        input_field = self._driver.find_element_by_name('q')
        return input_field.get_attribute('value')

    def open(self):
        self._driver.get(self._url)

    def title(self):
        self._driver.get(self.title)

    def maximize(self):
        self._driver.maximize_window()

    def wait(self,seconds):
        self._driver.implicitly_wait(seconds)
    
    def type_search(self, keyword):
        input_field = self._driver.find_element_by_name('q')
        input_field.send_keys(keyword)

    def click_submit(self):
        input_field = self._driver.find_element_by_name('q')
        input_field.submit()
    
    #Go to the testing page
    def click_to_store(self, keyword):
        click_on = self._driver.find_element_by_css_selector(keyword)
        click_on.click()

    #Look for id
    def look_for_id(self,keyword,text):
        self._driver.find_element_by_id(keyword).send_keys(text)        

    #Look for CLASS_NAME
    def look_for_class_name(self,keyword):
        self._driver.find_element_by_class_name(keyword)

    #Look for special XPATH 
    def look_for_xpath(self,keyword):
        look = 0
        loops = self._driver.find_elements_by_xpath(keyword)
        for i in loops:
            look = look + 1
        return look
    
    #Look for normal XPATH 
    def look_for_n_xpath(self,keyword):
        look = self._driver.find_element_by_xpath(keyword)
        look.click()

    #Look for link_text
    def look_for_link_text(self,keyword):
        look = self._driver.find_element_by_link_text(keyword)    
        look.click()
  
    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()