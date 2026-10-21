from selenium import webdriver
from selenium.webdriver.common.by import By
#keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/FELIDAE-Size-Plastic-Cricket-Tennis/dp/B0GG7YCTB1/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.ebb2d55c-c635-4819-bd37-52477d9326eb&dib=eyJ2IjoiMSJ9.gu8721NJjgU5AGDZAkNkbeTseDo5J_ZQn3aPO_tHYE8UTqdhAF8fIG1vZOP74NZuxlQx_H1xZ55uR-7vwzHypzv9f9x9hBLpdIhibhI2k_DU2V-cr__8CMtYbP15uAX-OuW0RfIRXW6gnYM_fiawQY9GGFegbPXNs8EzqtOILPZoAk-3J5mF1p4OeqyznrClhQyylaIAZLKWrmt2pmuHibwMwEWvJugQJlb35l3Br8HqCEJokLPKiGgDI4OvsVBCIehkdQfIU6JP3owieS5mK_MADjen7tcXPS7m0SiQc2Q.SGW3_xJLrWHWxQStPYlC0VPSU01jSwYH3xTTL31WIbg&dib_tag=se&pd_rd_r=5eb41041-3b62-40c4-b58f-34a7e0943834&pd_rd_w=7DZAU&pd_rd_wg=OClul&qid=1792571415&refinements=p_36%3A18900-99900&rnid=1318502031&s=sports&sr=1-1&srs=222938380031")

# price_rupee = driver.find_element(By.CLASS_NAME, value="a-price-whole")
pr = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div/div[1]/span[3]/span[2]/span[2]')
print(pr.text)
# print(f" The price is {price_rupee.text}")
driver.close() #close tab
driver.quit() #close browser
