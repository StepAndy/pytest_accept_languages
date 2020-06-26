# Внимание!
В тесте двухуровненвые вложенности и две опции. 
Просто было интересно реализовать именно так.
Для более воспринимаемой версии можно заменить весь код test_items.py на:
```
import time

def add_to_basket(browser):
    add_to_basket_button = browser.find_element_by_css_selector("#add_to_basket_form > [type='submit']")
    assert add_to_basket_button, "Button is not present"


def test_with_lang_opt(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    try:
        browser.get(link)
        add_to_basket(browser)  
		time.sleep(30)
    finally:
        browser.quit()
```
В ней проверяется только видимость элемента без учета кликабельности.

# Справка:

При запуске нужно обязательно использовать опцию "--language". Пример запуска из командной строки:
> pytest --language=es

Также, можно включить проверку кликабельности "--tc" (test clickability; По умолчанию = no) 
> pytest --language=es --tc=yes

