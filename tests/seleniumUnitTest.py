import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .context import src

class SearchText(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.options = webdriver.ChromeOptions()
        inst.options.add_argument('--ignore-ssl-errors=yes')
        inst.options.add_argument('--ignore-certificate-errors')
        inst.options.add_argument('-timeout=5000')
        inst.driver = webdriver.Remote(
            command_executor='http://172.18.0.3:4444/wd/hub',
            options=inst.options
        )
        inst.driver.maximize_window()
        # navigate to browserstack.com
        inst.driver.get("https://www.stealmylogin.com/demo.html")

    def test_search_by_text(self):

        # click on the Get started for free button
        self.driver.find_element(By.NAME, 'username').send_keys("testusername")
        self.driver.find_element(By.NAME, "password").send_keys("mypassword")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        pageTitle = self.driver.title

        print(pageTitle)
        if pageTitle == "Example Domain":
            print("Page Title Passed")

        assert(pageTitle == "Example Domain")
    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()



if __name__ == '__main__':
    unittest.main()
