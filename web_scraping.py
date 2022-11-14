from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.kubii.fr/")
search_bar = driver.find_element(By.ID,"search_query_top")
search_bar.send_keys("ARDUINO")
search_btn = driver.find_element(By.CLASS_NAME,"button-search")
search_btn.click()
driver.close()
