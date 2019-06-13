from selenium import webdriver
import HtmlTestRunner
from ddt import ddt,file_data
import unittest

@ddt
class TestDDTDataFile(unittest.TestCase):

    def setUp(self):
        path="chromedriver"
        self.driver=webdriver.Chrome(path)
        url ="https://www.facebook.com/login"
        self.driver.get(url)


    @file_data('mydatafile.json')
    def test_login(self,x):
        self.login(x[0],x[1],x[2])

    def login(self,username,password,expected):
        self.driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='pass']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='loginbutton']").click()

        isLoggedIn=self.driver.current_url=="https://www.facebook.com/"
        if isLoggedIn ==True:
            isLoggedIn="true"
        else:
            isLoggedIn="false"

        self.assertEqual(isLoggedIn,expected)

    def tearDown(self):
        self.driver.close()


if __name__ =='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))


