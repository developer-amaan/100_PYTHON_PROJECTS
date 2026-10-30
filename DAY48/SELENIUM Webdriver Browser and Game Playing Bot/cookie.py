from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")
language_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".langSelectButton.title"))
)
language_button.click()
cookie = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID, "bigCookie"))
)
try:
    while True:
        cookie.click()
except KeyboardInterrupt:
    print("Stopped clicking.")

