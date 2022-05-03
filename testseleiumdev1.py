from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.chrome(ChromeDriverManager("87.0.4280.141").install())

driver.get("https://google.com")
time.sleep(2)
driver.close()
driver.quit()