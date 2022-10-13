from time import sleep

import sys

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
driver = uc.Chrome(options=options, use_subprocess=True)
driver.get('https://faucet-sepolia.rockx.com/')
driver.find_element(By.XPATH, '//input[@placeholder="Paste the tweet URL here"]').send_keys(sys.argv[1])
driver.find_element(By.XPATH, '//button[text()="Send Me ETH"]').click()
sleep(3)
text = driver.find_element(By.XPATH, '//div[contains(@class, "arco-message-wrapper-top")]').text
print(text)
