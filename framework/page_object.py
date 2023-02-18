import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from framework.config import *
from framework.exceptions import *
class PageObject:
    def __init__(self): # This function open Steam's webside
        "ChromeDriverManager().install()"
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(URL)
        self.search_field = self.find_block('id', 'store_nav_search_term')
    def get_title_url(self):
        return self.browser.current_url
    
    def find_block(self, search_type, block):# This function find block on steam
        if search_type == 'xpath':
            result = self.browser.find_element(By.XPATH, block)
        elif search_type == 'class':
            result = self.browser.find_element(By.CLASS_NAME, block)
        elif search_type == 'id':
            result = self.browser.find_element(By.ID, block)
        return result    


    def find_title_game(self, name_game): # This function find game in steam
        self.search_field.send_keys(name_game)
        self.search_field.send_keys(Keys.RETURN)
        first_game = self.find_block('xpath', "//div[@class='col search_name ellipsis']/span[1]")
        first_game.click()
        return self.browser.title

    def change_language(self, language): # This function change language
        language_list = ['polish', 'english', 'italian', 'german', 'french']
        language_choice_button = self.find_block('id', 'language_pulldown')
        language_choice_button.click()
        if language in language_list:
            result_language = self.find_block('xpath', f"//div/a[@href='?l={language}']") 
            result_language.click()
            time.sleep(3)
            return self.browser.title
        else:
            raise LanguageNotFoundError
    
    def break_search_field(self, text): # This function find game in search field with 
        search_field = self.find_block('id', 'store_nav_search_term')
        search_field.send_keys(text)
        search_field.send_keys(Keys.RETURN)
        error = self.find_block('class', 'search_results_count')
        return error

    def save_check_name_game(self): # This function 
        game_link = self.find_block('class', 'tab_item app_impression_tracked focus[0]')
        name_game = self.find_block('xpath', '//div/class="tab_item_name"[1]')
        game_link.click()
        name_game_2 = self.find_block('id', 'appHubAppName')
        names = [name_game, name_game_2]
        return names
    
    def close_browser(self): # This function close Chrome
        self.browser.close()

    '''
    TODO:
    1. Расписать документацию (О автоматизации, о тестировании, документацию проекта)
    2. Составить тест-план (~15 тестов)
    3. Доработать фреймворк:
       - функция, которая будет искать текст
    4. Выполнить все TODO
    5. Переписать README.md
       - Краткое описание проекта;
         а. Для чего этот проект?
         б. Что он тестирует (какой сайт)?
       - Окружение;
         а. Программное обеспечение (Программирование & Модули)
            - Python
            - selenium
            - time
            - webdriver-manager
            - pytest
         б. ОС (Винда) Пример: Windows 10 Home Edition x64
         в. Программное обеспечение:
            - Браузеры (Хром, Файрфокс);
            - Драйвер для тестирования (Хром драйвер)
        - Как это все установить? Example: https://github.com/CleverRaven/Cataclysm-DDA/blob/master/README.md
        - К кому обращаться за дополнительными вопросами 
    '''