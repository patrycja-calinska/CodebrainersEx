import sys

sys.stdout.reconfigure(encoding='utf-8')

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# arrange
driver = webdriver.Chrome()
url = "https://demoqa.com/"
excpected_site_title = "DEMOQA"

# act
driver.get(url)
site_title = driver.title
card_list_of_elements = driver.find_elements(By.TAG_NAME, "h5")
card_element_forms = card_list_of_elements[1]
card_element_forms.click()
driver.implicitly_wait(2)
element_of_menu_list_practice_form = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div/ul/li/span')

# assert
assert site_title == excpected_site_title
assert element_of_menu_list_practice_form.text == "Practice Form"
element_of_menu_list_practice_form.click()

practice_form_first_name_input = driver.find_element(By.ID, "firstName")
practice_form_first_name_input.send_keys("Jan")


practice_form_last_name_input = driver.find_element(By.ID, "lastName")
practice_form_last_name_input.send_keys("Kowalski")


sleep(100)

# the end
input("moj input")
driver.quit()