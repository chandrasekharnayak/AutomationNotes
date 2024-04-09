import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains


def test_instagram_login(browser):
    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com/')

    username= 'treenetra_education'
    password = 'Education$108'

    username_input = browser.find_element(By.XPATH,"//input[@name='username']")
    password_input = browser.find_element(By.XPATH, "//input[@type='password']")
    username_input.send_keys(username)
    password_input.send_keys(password)

    #submit the form
    password_input.send_keys(Keys.RETURN)

    login = browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
    ActionChains(browser).move_to_element(login).click().perform()
    time.sleep(5)

