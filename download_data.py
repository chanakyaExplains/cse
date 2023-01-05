from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.cse.lk/pages/trade-summary/trade-summary.component.html')
time.sleep(25)

entry_drop=Select(driver.find_element(By.NAME,"DataTables_Table_0_length"))
entry_drop.select_by_visible_text("All")

download_button = driver.find_element(By.ID,"dropdownMenu2")
download_button.click()

format_of_download = driver.find_element(By.XPATH,"/html/body/app-root/div/app-trade-summary/div[2]/div/div[2]/div/div[1]/div[2]/div/ul/li[2]")
format_of_download.click()

time.sleep(20)