'''
fixture
plugings-------
hookings
'''

import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    #setup:- precondition
    driver = webdriver.Chrome()
    yield driver
    #teardown:- postcondition
    driver.quit()

