import sys
sys.stdout.reconfigure(encoding='utf-8')

from selenium import webdriver
from selenium.webdriver.common.by import By


class PracticeFormPage:
    def __init__(self):
        self.URL = "https://demoqa.com/automation-practice-form"
        self.driver = webdriver.Chrome()


    def open_page(self):
        self.driver.get(self.URL)


    def fill_first_name_input(self, first_name):
        self.first_name_input = self.driver.find_element(By.ID, "firstName")
        self.first_name_input.send_keys(first_name)


    def fill_lsat_name_input(self, last_name):
        self.last_name_input = self.driver.find_element(By.ID, "lastName")
        self.last_name_input.send_keys(last_name)


    def fill_user_email_input(self, email_address):
        self.email_address_input = self.driver.find_element(By.ID, "userEmail")
        self.email_address_input.send_keys(email_address)


    def fill_whole_practice_form(self, data_object):
        self.fill_first_name_input(data_object.first_name)
        self.fill_lsat_name_input(data_object.last_name)
        self.fill_user_email_input(data_object.email_address)


