import time
import pytest
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from tests.BaseTest import BaseTest


@pytest.mark.incremental
class Test(BaseTest):

    @pytest.mark.parametrize("url", ["http://127.0.0.1:5000/"])
    def test_search_products(self, url):
        wait = WebDriverWait(self.driver, 100)
        self.driver.get(url)

        # wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@id="hplogo"]'))) #go to product element.

        ################login#################
        loginBtn = self.driver.find_element_by_id('login')
        loginBtn.click()

        username = self.driver.find_element_by_xpath("//input[@id='username']")
        username.click()
        username.send_keys('test')

        password = self.driver.find_element_by_xpath("//input[@id='password']")
        password.click()
        password.send_keys('1234')

        submit = self.driver.find_element_by_xpath("//input[@value='LogIn']")
        submit.click()
        ################login#################

        ################make post twice#################
        try:
            newBtn = self.driver.find_element_by_xpath("//a[@href='/create']")
            newBtn.click()

            title = self.driver.find_element_by_xpath("//input[@id='title']")
            title.click()
            title.send_keys('this is a test')

            body = self.driver.find_element_by_xpath("//textarea[@id='body']")
            body.click()
            body.send_keys('body test')

            save = self.driver.find_element_by_xpath("//input[@value='Save']")
            save.click()
            ##one more
            newBtn.click()
            title.click()
            title.send_keys('this is a test')
            body.click( )
            body.send_keys('body test')
            save.click()
        except StaleElementReferenceException:
            print('same post!!')
        ################make post twice#################

        time.sleep(10)