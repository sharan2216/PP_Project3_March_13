from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pytest


driver = webdriver.Chrome()
driver.get("https://demos.telerik.com/kendo-ui/treeview/animation")
driver.maximize_window()
time.sleep(3)
driver.execute_script("window.scrollBy(0,500)")
time.sleep(2)
act = ActionChains(driver)
ele = driver.find_element(By.XPATH, "//span[normalize-space()='Furniture']")
act.double_click(ele).perform()
time.sleep(5)