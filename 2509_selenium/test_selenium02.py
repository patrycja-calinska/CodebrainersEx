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
card_element_elements = driver.find_element(By.TAG_NAME, "h5")
card_element_elements.click()

# assert
assert site_title == excpected_site_title
input("moj input")
driver.quit()