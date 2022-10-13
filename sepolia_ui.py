from time import sleep

import sys

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By



if __name__ == '__main__':
    # upload_basic()
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = uc.Chrome(options=options)
    driver.get('https://faucet-sepolia.rockx.com/')
    driver.find_element(By.XPATH, '//input[@placeholder="Paste the tweet URL here"]').send_keys(sys.argv[1])
    driver.find_element(By.XPATH, '//button[text()="Send Me ETH"]').click()
    sleep(3)
    print('===')
    print(driver.page_source)
    print('===')
    text = driver.find_element(By.XPATH, '//div[contains(@class, "arco-message-wrapper-top")]').text
    print(text)

