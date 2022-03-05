from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

exe_file = Service('chromedriver.exe')
driver = webdriver.Chrome(service=exe_file)

driver.get('https://account.protonmail.com/signup?language=en')

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div[1]/div[3]/div/div/main/div[2]/form/div[1]/iframe")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username"))).send_keys("hola_mundo")

driver.switch_to.default_content()

input_password = driver.find_element(By.ID, "password")
input_password.send_keys('holaMundo')

input_repassword = driver.find_element(By.ID, "repeat-password")
input_repassword.send_keys('holaMundo')
