#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# wait = WebDriverWait(driver, 10)
#
# search = wait.until(
#     EC.element_to_be_clickable((By.ID, "searchInput"))
# )
#
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Step 1: Click the actual search toggle link
search_toggle = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.search-toggle"))
)
search_toggle.click()

# Step 2: Wait until the search input is visible
search = wait.until(
    EC.visibility_of_element_located((By.ID, "searchInput"))
)

# Step 3: Search for Python
search.send_keys("Python")
search.send_keys(Keys.ENTER)

