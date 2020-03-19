from selenium import webdriver
from selenium.webdriver import Chrome


path = "D:/chromedriver_win32 (1)/chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("https://www.hdfcbank.com/")
driver.maximize_window()


