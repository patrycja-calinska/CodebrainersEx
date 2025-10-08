from selenium import webdriver
from time import sleep

#arrange
driver = webdriver.Chrome()
expected_site_title = "Coś więcej niz kodowanie - codebrainers"

#act
driver.get("https://codebrainers.pl/")
site_title = driver.title
print(site_title)

#assert
assert site_title == expected_site_title
#leep(5) # Czekaj 5 sekund
driver.quit()

