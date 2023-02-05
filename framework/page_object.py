from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from framework.config import *
class PageObject:
    def __init__(self): # This function open Steam's webside
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get(URL)
        self.search_field = self.browser.find_element(By.ID, 'store_nav_search_term')
    def get_title_url(self):
        return self.browser.current_url
    
    def find_block(self, search_type, block):
        # TODO: Надо добавить проверки для класса, id
        if search_type == 'xpath':
            result = self.browser.find_element(By.XPATH, block)
        return result
    def find_title_game(self, name_game): # This function find game in steam
        self.search_field.send_keys(name_game)
        self.search_field.send_keys(Keys.ARROW_DOWN)
        self.search_field.send_keys(Keys.RETURN)
        first_game = self.find_block('xpath', "//div[@class='col search_name ellipsis']/span[1]")
        first_game.click()
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