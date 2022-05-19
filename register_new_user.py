import unittest
from venv import create
from selenium import webdriver
from search_page import SearchPage


class RegisterNewUser(unittest.TestCase):

    @classmethod
    def setUp(self):
        #Change the path with the correct ubication where it is the chromedriver
        self.driver = webdriver.Chrome(executable_path = r'C://Users//saman//OneDrive//Sandra_Rojas//Studies//Selenium_python//chromedriver_win32//chromedriver.exe')
       
    def test_new_user(self):
        url = 'http://demo-store.seleniumacademy.com/'
        search = SearchPage(self.driver)
        search.open()
        search.maximize()
        #Look for the testing page
        search.search(url)

        self.assertEqual(url, search.keyword)

        search.click_to_store('#rso > div:nth-child(1) > div > div.NJo7tc.Z26q7c.jGGQ5e > div > a > div > cite')
        search.wait(300)

        search.look_for_n_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]')
        search.look_for_link_text('Log In')
        
        search.look_for_n_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a')
        
        search.look_for_id('firstname','TestSam')
        
        search.look_for_id('middlename','TestSam')
       
        search.look_for_id('lastname','TestSam')

        search.look_for_id('email_address','TestSam@gmail.com')

        search.look_for_id('is_subscribed','Test')

        search.look_for_id('password','Test12345*')

        search.look_for_id('confirmation','Test12345*') 
        search.wait(3600)     
        
        search.look_for_n_xpath('//*[@id="form-validate"]/div[2]/button/span/span') 
                 

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
        