from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from framework.config import *
class PageObject:
    def __init__(self): # This function open Steam's webside
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get(URL)
        self.field = self.browser.find_element(By.XPATH, '//input[id="store_nav_search_term"]')
    def get_title_url(self):
        return self.browser.current_url
        # TODO - сделать функцию find_GTAV универсальной (аля find_game)
    def find_games(self, name_game): # This function find game in steam
        field = self.browser.find_element(By.XPATH, '//input[id="store_nav_search_term"]')
        field.send_keys(name_game)
        field.send_keys(Keys.ARROW_DOWN)
        field.send_keys(Keys.RETURN)
        return self.browser.title
    def close_browser(self): # This function close Chrome
        self.browser.close()

    '''
    TODO:
    1. Расписать универсиальные и общие методы (поиск блока, поиск текста, кликнуть на кнопку, ввести данные)
    2. Разобраться с github и отправить проект в него
    3. Разобраться с типами фикстур (о scope (function, module, session))
    4. Переписать фикстуру с применением yield (open_browser)
    5. Расписать документацию (О автоматизации, о тестировании, документацию проекта)
    '''