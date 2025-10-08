import sys
sys.stdout.reconfigure(encoding='utf-8')

from selenium import webdriver
from selenium.webdriver.common.by import By

class PracticeFormPage:

    def init(self, dataObject):
        self.driver = webdriver.Chrome()
        self.driver.get(dataObject.URL)
        self.first_name_input = self.
        self.last_name_input = self.driver.find_element(By.ID, "lastName")
        self.email_input = self.driver.find_element(By.ID, "userEmail")