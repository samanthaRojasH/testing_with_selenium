import unittest
from selenium import webdriver
import csv, unittest
from ddt import ddt, data, unpack
from search_page import SearchPage

def get_data(filename):
    rows=[]
    data_file = open(filename, 'r')
    reader = csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)
    return rows

@ddt
class SearchTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        #Change the path with the correct ubication where it is the chromedriver
        self.driver = webdriver.Chrome(executable_path = r'C://Users//saman//OneDrive//Sandra_Rojas//Studies//Selenium_python//chromedriver_win32//chromedriver.exe')

    @data(*get_data('testdata.csv'))
    @unpack

    def test_search(self, search_value, expect_count):
        url = 'http://demo-store.seleniumacademy.com/'
        search = SearchPage(self.driver)
        search.open()
        search.maximize()
        #Look for the testing page
        search.search(url)

        self.assertEqual(url, search.keyword)

        search.click_to_store('#rso > div:nth-child(1) > div > div.NJo7tc.Z26q7c.jGGQ5e > div > a > div > cite')
        search.wait(300)

        search.search(search_value)
        search.click_submit()  
        
        search.wait(300)
        products = search.look_for_xpath('//h2[@class="product-name"]/a')
        
        expect_count = int(expect_count)

        if expect_count > 0:
           self.assertEqual(expect_count, products)
        else:
            message = search.look_for_class_name('note-msg') 
            self.assertEqual('Your search returns no results', message)
        
        print(f'Found {products} products')      


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)