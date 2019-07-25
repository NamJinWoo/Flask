import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from tests.BaseTest import BaseTest


@pytest.mark.incremental
class Test(BaseTest):

    @pytest.mark.parametrize("url", ["http://www.nanocellect.com/"])
    def test_search_products(self, url):
        wait = WebDriverWait(self.driver, 100)
        self.driver.get(url)

        # wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@id="hplogo"]'))) #go to product element.


        firstName = self.driver.find_element_by_name('first_name')
        firstName.clear()
        firstName.send_keys('Jinwoo')

        lastName = self.driver.find_element_by_name('last_name')
        lastName.clear()
        lastName.send_keys('Nam')

        organization = self.driver.find_element_by_name('company')
        organization.clear()
        organization.send_keys('NanoCellect')

        email = self.driver.find_element_by_name('email')
        email.clear()
        email.send_keys('jinwooo.nam@gmail.com')

        phone = self.driver.find_element_by_name('phone')
        phone.clear()
        phone.send_keys('+1 (765) 701-7460')

        city = self.driver.find_element_by_name('city')
        city.clear()
        city.send_keys('San Diego')

        state = self.driver.find_element_by_name('state')
        state.clear()
        state.send_keys('CA')

        zip = self.driver.find_element_by_name('zip')
        zip.clear()
        zip.send_keys('12345')

        select = Select(self.driver.find_element_by_name('00N4100000WnUtk'))
        select.select_by_value('Other')

        description = self.driver.find_element_by_xpath("//textarea[@name='description']")
        description.click()
        description.clear()
        description.send_keys('This is my first selenium test.')

        time.sleep(10)
        #text = self.driver.find_element_by_tag_name("img").id
        #with pytest.raises(AssertionError):
        #    assert text == "hplogo"
        #print("There is no image in here.")

# What is assert?
# A statement for debugging some AssertionErrors.
