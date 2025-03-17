import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose language")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
