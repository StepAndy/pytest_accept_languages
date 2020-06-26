from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
import time


def find_basket(css_selector, browser, request):
    test_clickability = str(request.config.getoption("--tc"))  
    if test_clickability == "yes":
        try:
            WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        except:
            assert False, "Button was not clickable for 30 secs. Make sure you use right selector"

    elif test_clickability == "no":
        add_to_basket_button = browser.find_element_by_css_selector(css_selector)
        assert add_to_basket_button, "Button is not present"
        

def test_baskets_presence(browser, request):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    css_selector = "#add_to_basket_form > [type='submit']"
    try:
        browser.get(link)
        find_basket(css_selector, browser, request)
        time.sleep(30)
    finally:
        browser.quit()
